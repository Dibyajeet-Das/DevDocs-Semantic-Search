# DevDocs Semantic Search

DevDocs Semantic Search is a small project I am building to understand how **semantic search and vector databases work in real applications**.

The main idea is to allow developers to search documentation using the **meaning of a query**, instead of depending only on exact keyword matching.

For example, if the documentation contains information about **Spring Dependency Injection and Beans**, a query such as:

> How does Spring manage objects?

can still find that documentation even though the exact words from the query may not appear in the document.

## Why I Built This

I built this project as a hands-on way to learn how modern AI search systems work.

Instead of only learning concepts such as embeddings, vector databases, and similarity search theoretically, I am implementing them step by step in a small working project.

The current version focuses mainly on:

* Creating text embeddings
* Storing embeddings in a vector database
* Performing semantic similarity search
* Understanding how Top-K retrieval works
* Building APIs around the search functionality

## How It Works

The current search flow is:

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
Top-K Relevant Documents
```

For example:

```text
User:
"How does Spring manage objects?"
        ↓
Embedding Model
        ↓
Query Vector
        ↓
ChromaDB
        ↓
Find similar document vectors
        ↓
Return the most relevant documents
```

The project currently uses `all-MiniLM-L6-v2` from Sentence Transformers.

This model converts text into **384-dimensional vector embeddings**.

These vectors are stored in ChromaDB and are used to perform similarity-based searches.

## Current Features

* Generate embeddings using Sentence Transformers
* Store embeddings in ChromaDB
* Persistent local vector database
* Semantic similarity search
* Top-K document retrieval
* Ingest `.txt` documentation files
* Store document metadata
* FastAPI backend
* Logging and exception handling
* Modular service-based architecture

## Current Search Implementation

The search functionality uses a `top_k` value to control how many relevant results should be returned.

For example:

```python
search(query_embedding, top_k=3)
```

means:

> Search the vector database and return the 3 most similar results to the user's query.

Here, `top_k` refers to **retrieval results**, not token probabilities or LLM text generation.

## Document Ingestion

The project currently reads developer documentation from `.txt` files.

The documents are organized by technology:

```text
data/
└── documents/
    ├── docker/
    │   └── docker.txt
    ├── java/
    │   └── spring_boot.txt
    ├── kafka/
    │   └── kafka.txt
    └── python/
        └── python.txt
```

The basic ingestion flow is:

```text
Documentation
     ↓
Read Text
     ↓
Generate Embedding
     ↓
Store in ChromaDB
     ↓
Store Metadata
```

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

## Current Architecture

The backend is separated into different services so that each part of the system has a clear responsibility.

```text
                    FastAPI
                       │
              ┌────────┴────────┐
              ↓                 ↓
       SearchService         Ingestion
              │                 │
              ↓                 ↓
      EmbeddingService   EmbeddingService
              │                 │
              └────────┬────────┘
                       ↓
                  ChromaService
                       ↓
                    ChromaDB
```

### Main Components

**EmbeddingService**

Responsible for loading the embedding model and converting text into vectors.

```python
self.model = SentenceTransformer("all-MiniLM-L6-v2")
```

**ChromaService**

Responsible for interacting with ChromaDB, including storing and retrieving vector data.

**SearchService**

Responsible for taking the user's query embedding and retrieving the most relevant documents from ChromaDB.

**ingest.py**

Responsible for reading documentation files and adding their embeddings and metadata to the vector database.

**main.py**

Contains the FastAPI application and API endpoints used to interact with the backend.

## What I Plan to Add Next

This project is still under development. The next steps are focused on moving from basic semantic search toward a more complete **RAG (Retrieval-Augmented Generation)** system.

Planned improvements include:

* Document chunking
* Better metadata filtering
* Support for more document formats
* Improved retrieval and ranking
* Connecting an LLM to the retrieved documents
* RAG-based answer generation
* Returning the source documents used to generate an answer
* Building a simple web frontend
* Eventually exploring production-ready vector search and deployment

## Learning Goal

The goal of this project is not just to build a search application, but to understand what happens behind the scenes in a modern AI-powered search system:

```text
Text
 ↓
Embedding
 ↓
Vector
 ↓
Vector Database
 ↓
Similarity Search
 ↓
Relevant Context
 ↓
LLM
 ↓
Final Answer
```

I am building the project step by step so that each part of the pipeline can be understood and tested independently.
