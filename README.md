# ChromaDB Project

This is a sample project to store and query text using a vector database (ChromaDB) and `SentenceTransformer` for embedding generation. It demonstrates how to create a collection, store text embeddings, and query for the most similar document based on a user input.

## Features
- Store document text as vector embeddings in ChromaDB.
- Query the most similar text to a given input.
- Colorful output using `termcolor`.

## Prerequisites
Before you begin, ensure you have the following installed on your system:
- Python 3.7 or above
- `pip` package manager

## Setup Instructions

### 1. Create a Virtual Environment

For **Windows**:
```bash
python -m venv chroma_env
chroma_env\Scripts\activate
```
For Linux/Mac:

```bash
python3 -m venv chroma_env
source chroma_env/bin/activate
```
### 2. Install the Required Libraries
Once the virtual environment is activated, install the required dependencies by running:

```bash
pip install -r requirements.txt
```
Make sure your requirements.txt includes the following:

```txt
chromadb
sentence-transformers
termcolor
```

### 3. Run the Program
To run the script, simply execute the following command in your terminal or command prompt:

```bash
python script_name.py
```
Replace script_name.py with the actual name of your Python file.

### 4. Usage
When you run the program, you'll be prompted to enter a query. The program will search for the most similar document in the collection based on the query text and display the result.

Example Output:

```mathematica
Enter your query: What is RAG?
Query is: What is RAG?
Most Matching Document:
Document ID: doc1
Text: Experimenting with RAG (Retrieval-Augmented Generation) for Text Fine-Tuning!.
Similarity Score: 0.85
```
## Acknowledgments
- ChromaDB for providing a lightweight vector database solution.
- Hugging Face's SentenceTransformers for easy-to-use text embeddings.
- Termcolor for making the output more visually appealing.
