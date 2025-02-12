#!/bin/bash

# Default arguments if none provided
if [ "$#" -eq 0 ]; then
    # Set default query for testing
    QUERY="What is quantum computing?"
    # Run with default arguments
    python main.py --query "$QUERY" \
        --web_search \
        --max_depth 2 \
        --top_k 5 \
        --retrieval_model all-minilm
else
    # Run with provided arguments
    python main.py --retrieval_model all-minilm "$@"
fi
