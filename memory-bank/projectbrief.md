# NanoSage Project Brief

## Project Overview
NanoSage is an advanced recursive search and report generation system that runs locally using small language models. It's designed to provide structured, in-depth research capabilities by implementing a multi-source, relevance-driven, recursive search pipeline.

## Core Goals
1. Provide deep research capabilities using local compute
2. Generate well-organized, comprehensive reports
3. Implement intelligent recursive search with relevance tracking
4. Balance exploration vs exploitation in research paths
5. Maintain efficiency with small, local models

## Key Requirements

### Functional Requirements
1. Query Enhancement
   - Chain-of-thought query enhancement
   - Subquery generation and relevance filtering

2. Search & Retrieval
   - Web-based search capabilities
   - Local document corpus support
   - Relevance scoring and filtering

3. Knowledge Management
   - Dynamic knowledge base construction
   - Document embedding and retrieval
   - Context preservation across searches

4. Report Generation
   - Structured markdown output
   - Table of Contents (TOC) based on search graph
   - RAG-based summaries using local models

### Technical Requirements
1. Python 3.8+ environment
2. Local model support (Gemma 2B)
3. GPU acceleration capability (optional)
4. Ollama integration for model serving
5. Efficient resource usage for laptop deployment

## Success Criteria
1. Generate detailed, well-organized research reports
2. Maintain search relevance through recursive exploration
3. Operate efficiently on consumer hardware
4. Produce human-readable, markdown-formatted output
5. Support both web and local document sources

## Constraints
1. Must run on consumer laptops
2. Limited to small, efficient models
3. Resource-aware processing
4. Local-first architecture

## Project Scope
### In Scope
- Query enhancement and refinement
- Web and local document search
- Knowledge base construction
- Report generation with TOC
- RAG-based summarization
- Monte Carlo search exploration

### Out of Scope
- Large language model deployment
- Real-time collaboration
- External API dependencies
- Distributed processing

## Timeline
Project is in active development with ongoing improvements to:
- Search algorithms
- Model integration
- Report generation
- Performance optimization

## Stakeholders
- End users requiring deep research capabilities
- Developers building on the platform
- Contributors to the open source project

This brief serves as the foundation for NanoSage's development and evolution, guiding technical decisions and feature implementation while maintaining focus on the core goal of providing powerful, local-first research capabilities.
