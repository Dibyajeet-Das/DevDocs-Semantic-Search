# DevDocs Semantic Search

A semantic search engine for developer documentation using embeddings, ChromaDB, and FastAPI.

## Overview

DevDocs Semantic Search allows users to search developer documentation based on semantic meaning rather than exact keyword matching.

For example, a query such as:

> How does Spring manage objects?

can retrieve documentation related to Spring Dependency Injection and Spring Beans, even when the exact words from the query are not present in the document.

## How It Works

The current search pipeline is:

```text
User Query
    ↓
Embedding Model
    ↓
Query Embedding
    ↓
ChromaDB
    ↓
Similarity Search
    ↓
Top-K Relevant Results
```

The project uses `all-MiniLM-L6-v2` from Sentence Transformers to convert text into 384-dimensional vector embeddings.

ChromaDB stores the document embeddings and performs similarity-based retrieval to find documents that are semantically similar to the user's query.

## Current Features

* Generate embeddings using Sentence Transformers
* Store embeddings in ChromaDB
* Persistent local vector database
* Semantic similarity search
* Top-K document retrieval
* Document ingestion from `.txt` files
* Document metadata storage
* FastAPI backend
* Logging and error handling
* Modular service-based architecture

## Tech Stack

* Python 3.12
* FastAPI
* Uvicorn
* Sentence Transformers
* ChromaDB
* HTML / CSS / JavaScript (planned)

## Project Structure

```text
DevDocs-Semantic-Search/
│
├── backend/
│   ├── ChromaService.py
│   ├── EmbeddingService.py
│   ├── SearchService.py
│   ├── __init__.py
│   ├── ingest.py
│   └── main.py
│
├── data/
│   └── documents/
│       ├── docker/
│       │   └── docker.txt
│       ├── java/
│       │   └── spring_boot.txt
│       ├── kafka/
│       │   └── kafka.txt
│       └── python/
│           └── python.txt
│
├── .gitignore
├── LICENSE
└── README.md
```

## Search Flow

The search process works in two main stages.

### 1. Document Ingestion

```text
Text Documents
      ↓
Read Documents
      ↓
Generate Embeddings
      ↓
Store Embeddings
      ↓
ChromaDB
```

Each document is converted into a vector embedding and stored in ChromaDB along with its metadata.

### 2. Semantic Search

```text
User Query
      ↓
Generate Query Embedding
      ↓
Search ChromaDB
      ↓
Calculate Similarity
      ↓
Retrieve Top-K Results
      ↓
Return Relevant Documents
```

The `top_k` value determines how many of the most relevant results are returned. For example, `top_k=3` returns the three most similar results to the user's query.

## Current Architecture

The application follows a modular service-based architecture:

```text
FastAPI
   │
   ├── SearchService
   │       ↓
   │   EmbeddingService
   │       ↓
   │   ChromaService
   │       ↓
   │   ChromaDB
   │
   └── Document Ingestion
           ↓
      EmbeddingService
           ↓
        ChromaDB
```

## Future Improvements

Planned improvements include:

* Web-based frontend
* Document chunking
* Improved metadata filtering
* Support for additional document formats
* RAG-based answer generation using an LLM
* Source-aware responses
* Improved retrieval and ranking
* Production-ready deployment

````

### A few important notes

**1. Your original README says:**

```text
docker.txt
kafka.txt
python.txt
spring_boot.txt
````

But your Git output shows you have now organized them into folders. So updating that section is important.

**2. Adding `Top-K document retrieval` is useful** because your current code explicitly implements:

```python
n_results=top_k
```

**3. Don't claim RAG yet.**

Your current system is essentially:

```text
Query → Embedding → ChromaDB → Similar Documents
```

Once you add:

```text
Similar Documents
       ↓
Context
       ↓
LLM
       ↓
Generated Answer
```

then you can describe it as a **RAG system**.

**4. Your README is now telling the story of the project well:** ingestion → embeddings → vector database → semantic retrieval. That's a good foundation before you add chunking and RAG.
