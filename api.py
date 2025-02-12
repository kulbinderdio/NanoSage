from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
from search_session import SearchSession
import uvicorn

app = FastAPI()

# Default configuration
DEFAULT_CONFIG = {
    "results_base_dir": "results",
    "web_search_limit": 5,
    "max_query_length": 200,
    "monte_carlo_search": True,
    "monte_carlo_samples": 3,
    "min_relevance": 0.5
}

class SearchRequest(BaseModel):
    query: str
    depth: int = 2
    web_search_enabled: bool = True
    top_k: int = 5
    config: dict = DEFAULT_CONFIG

@app.post("/search")
async def search(request: SearchRequest):
    try:
        session = SearchSession(
            query=request.query,
            config=request.config,
            web_search_enabled=request.web_search_enabled,
            max_depth=request.depth,
            top_k=request.top_k,
            retrieval_model="all-minilm"  # Use all-minilm instead of colpali
        )

        # Run the search session
        final_answer = await session.run_session()

        return {
            "status": "success",
            "query_id": session.query_id,
            "report_path": f"results/{session.query_id}/{session.query_id}_output.md",
            "result": final_answer
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
