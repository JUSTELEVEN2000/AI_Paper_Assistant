# AI Paper Assistant

A RAG-powered academic research assistant that enables semantic search, paper summarization, hypothesis extraction, and methodology analysis from PDF documents.

## Overview

AI Paper Assistant is a RAG-based research assistant that helps researchers analyze academic papers efficiently.

The system allows users to upload PDF papers and perform:

- Paper summarization
- Research question extraction
- Hypothesis identification
- Methodology analysis
- Question answering with citation-based retrieval

## Tech Stack

- Python
- RAG Architecture
- FAISS
- BM25
- Sentence Transformers
- Large Language Models (LLM)
- PDF Processing

## Features

### 1. PDF Paper Processing

- Extract text from academic papers
- Split documents into semantic chunks
- Store metadata for retrieval

### 2. Hybrid Retrieval System

The system combines:

Vector similarity search
BM25 keyword retrieval

to improve academic paper retrieval performance.

### 3. Reranking

Retrieved documents are reranked to improve relevance before generation.

### 4. RAG Question Answering

Users can ask questions such as:

What are the main contributions?
What hypotheses are proposed?
What methodology is used?

The system retrieves relevant paper sections and generates answers using LLM.

### 5. Research Analysis Tools

Supported functions:

Summary generation
Hypothesis extraction
Methodology extraction
Academic Q&A

### 6. Evaluation

Includes retrieval evaluation components:

Retrieval metrics
Answer evaluation

---

## Architecture

```text
PDF
 |
 v
PDF Loader
 |
 v
Chunking
 |
 +----------------+
 |                |
BM25          Embedding
 |                |
 +-------+--------+
         |
         v
 Hybrid Retriever
         |
         v
 Query Reranker
         |
         v
 LLM Generation
         |
         v
 Answer
 ```

---

 ## Project Structure

```text
AI_Paper_Assistant
├── app.py
├── papers
├── rag
│   ├── embedding.py
│   ├── retriever.py
│   ├── bm25.py
│   ├── reranker.py
│   ├── query_rewriter.py
│   ├── query_router.py
│   └── vector_store.py
│
├── services
│   ├── summarize.py
│   ├── hypothesis.py
│   ├── methodology.py
│
├── evaluation
│
├── src
│
└── utils
```

## Installation

### Clone repository:

```bash
git clone https://github.com/yourname/AI_Paper_Assistant.git
```

### Create environment:

```bash
python -m venv .venv

source .venv/bin/activate
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run:

```bash
python app.py
```

## Example Result

### Question:

What are the main contributions?

### Output:

The study contributes by examining the relationship between
share repurchases and corporate investment in Japan...

## Future Improvements
Multi-paper knowledge base
Web paper search integration
Agent-based workflow
Better evaluation framework