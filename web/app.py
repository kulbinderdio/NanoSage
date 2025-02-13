from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import markdown
import os
import requests
import json

app = Flask(__name__)
CORS(app)

API_URL = "http://api:8000"
RESULTS_DIR = "/app/results"

def get_markdown_content(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            html_content = markdown.markdown(content)
            return html_content
    except FileNotFoundError:
        return None

def get_query_from_report(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            lines = content.split('\n')
            # Look for the Enhanced Query section
            for i, line in enumerate(lines):
                if '**Enhanced Query**' in line or 'Enhanced Query' in line:
                    # Look at the next few lines to find the query
                    for next_line in lines[i+1:i+5]:  # Check next 4 lines
                        if next_line.strip() and not next_line.startswith('#') and not next_line.startswith('*'):
                            return next_line.strip()
    except (FileNotFoundError, StopIteration):
        return None

@app.route('/')
def index():
    # List all markdown files in the results directory
    reports = []
    if os.path.exists(RESULTS_DIR):
        for query_dir in os.listdir(RESULTS_DIR):
            dir_path = os.path.join(RESULTS_DIR, query_dir)
            if os.path.isdir(dir_path):
                for file in os.listdir(dir_path):
                    if file.endswith('_output.md'):
                        report_path = os.path.join(dir_path, file)
                        query = get_query_from_report(report_path)
                        reports.append({
                            'id': query_dir,
                            'path': os.path.join(query_dir, file),
                            'query': query or f"Report {query_dir}"  # Fallback to Report ID if query not found
                        })

    return render_template('index.html', reports=reports)

@app.route('/report/<query_id>')
def view_report(query_id):
    file_path = os.path.join(RESULTS_DIR, query_id, f"{query_id}_output.md")
    content = get_markdown_content(file_path)
    query = get_query_from_report(file_path)

    if content is None:
        return "Report not found", 404

    return render_template('report.html', content=content, report_id=query_id, query=query or f"Report {query_id}")

@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    try:
        response = requests.post(f"{API_URL}/search", json=data, timeout=290)  # Set slightly below Gunicorn timeout
        return jsonify(response.json())
    except requests.exceptions.Timeout:
        return jsonify({"error": "Search request timed out. Please try again."}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
