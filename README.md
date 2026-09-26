# DevDocs Semantic Search

A semantic search engine for developer documentation using embeddings, ChromaDB, and FastAPI.

## Overview

DevDocs Semantic Search allows users to search developer documentation based on
semantic meaning rather than exact keyword matching.

For example, a query such as:

> How does Spring manage objects?

can retrieve documentation related to Spring Dependency Injection and beans,
even when the exact words from the query are not present in the document.

## How It Works

The current search pipeline is:

User Query
    ↓
Sentence Transformer
    ↓
Query Embedding
    ↓
ChromaDB
    ↓
Similarity Search
    ↓
Relevant Documents

The project uses `all-MiniLM-L6-v2` to convert text into 384-dimensional
vector embeddings.

ChromaDB stores the document embeddings and performs similarity search.

## Current Features

- Generate embeddings using Sentence Transformers
- Store embeddings in ChromaDB
- Persistent local vector database
- Semantic similarity search
- Document ingestion from `.txt` files
- Metadata storage for documents
- FastAPI backend
- Logging and error handling
- Modular service-based architecture

## Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- Sentence Transformers
- ChromaDB
- HTML / CSS / JavaScript (planned)

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
│       ├── docker.txt
│       ├── kafka.txt
│       ├── python.txt
│       └── spring_boot.txt
│
├── .gitignore
├── LICENSE
└── README.md
