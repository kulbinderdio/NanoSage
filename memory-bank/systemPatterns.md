# NanoSage System Patterns

## Architecture Overview

### Core Components
1. **SearchSession Orchestrator**
   - Central controller managing the entire search pipeline
   - Handles initialization, search execution, and result aggregation
   - Maintains state through query lifecycle

2. **Knowledge Base**
   - Document storage and retrieval system
   - Embedding-based search capabilities
   - Supports both local and web documents

3. **TOC Tree**
   - Hierarchical representation of search paths
   - Tracks relevance scores and summaries
   - Guides report structure

## Design Patterns

### 1. Pipeline Pattern
```mermaid
flowchart TD
    A[Query Input] --> B[Query Enhancement]
    B --> C[Subquery Generation]
    C --> D[Recursive Search]
    D --> E[Knowledge Base]
    E --> F[Report Generation]
```

- Sequential processing stages
- Clear data flow between components
- Modular stage implementation

### 2. Composite Pattern (TOC Tree)
```mermaid
flowchart TD
    Root[TOC Root] --> Branch1[Branch 1]
    Root --> Branch2[Branch 2]
    Branch1 --> Leaf1[Leaf 1.1]
    Branch1 --> Leaf2[Leaf 1.2]
    Branch2 --> Leaf3[Leaf 2.1]
```

- TOCNode structure for search hierarchy
- Recursive composition of search results
- Maintains parent-child relationships

### 3. Strategy Pattern
- Configurable retrieval models
- Pluggable RAG implementations
- Flexible search strategies

### 4. Factory Pattern
- Model loading and initialization
- Document embedding creation
- Result aggregation

## Key Technical Decisions

### 1. Embedding Architecture
- Late interaction scoring for relevance
- Efficient document representation
- Model-agnostic design

### 2. Search Strategy
```mermaid
flowchart TD
    A[Enhanced Query] --> B{Monte Carlo Sampling}
    B --> C[Relevance Scoring]
    C --> D{Threshold Check}
    D -->|Pass| E[Expand Search]
    D -->|Fail| F[Skip Branch]
```

- Monte Carlo subquery sampling
- Relevance-based pruning
- Depth-limited recursion

### 3. Resource Management
- Configurable device targeting (CPU/GPU)
- Chunked text processing
- Efficient memory usage

### 4. Model Integration
- Local model deployment (Gemma 2B)
- Ollama integration
- Flexible model selection

## Component Relationships

### 1. Search Session Flow
```mermaid
flowchart TD
    A[SearchSession] --> B[Query Enhancement]
    A --> C[Knowledge Base]
    A --> D[Web Search]
    B --> E[TOC Construction]
    C --> F[Local Retrieval]
    D --> G[Web Retrieval]
    E --> H[Report Generation]
    F --> H
    G --> H
```

### 2. Knowledge Base Integration
```mermaid
flowchart TD
    A[Documents] --> B[Embedding]
    B --> C[Knowledge Base]
    C --> D[Search]
    D --> E[Retrieval]
```

### 3. Report Generation Pipeline
```mermaid
flowchart TD
    A[TOC Tree] --> D[Final Report]
    B[Web Results] --> D
    C[Local Results] --> D
```

## Implementation Patterns

### 1. Async Processing
- Asynchronous web searches
- Concurrent document processing
- Non-blocking operations

### 2. Error Handling
- Graceful degradation
- Robust web scraping
- Safe embedding generation

### 3. Configuration Management
- YAML-based configuration
- Command-line arguments
- Environment-aware settings

### 4. Data Flow
```mermaid
flowchart TD
    A[Raw Data] --> B[Preprocessing]
    B --> C[Embedding]
    C --> D[Storage]
    D --> E[Retrieval]
    E --> F[Summarization]
```

## System Constraints

### 1. Resource Limitations
- Memory-aware processing
- Configurable batch sizes
- Device-specific optimizations

### 2. Model Constraints
- Small model focus
- Local execution
- Efficient inference

### 3. Search Boundaries
- Depth limits
- Relevance thresholds
- Result count caps

## Evolution Patterns

### 1. Extensibility Points
- Model integration interface
- Search strategy plugins
- Report format customization

### 2. Scalability Considerations
- Modular component design
- Configurable resource usage
- Flexible deployment options

### 3. Maintenance Patterns
- Clear component boundaries
- Consistent error handling
- Comprehensive logging

This document captures the key architectural patterns and design decisions in NanoSage, serving as a reference for understanding and extending the system.
