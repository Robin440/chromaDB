import chromadb
from sentence_transformers import SentenceTransformer
from termcolor import colored  # Import termcolor for colored output

# Load a pre-trained model for text embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize ChromaDB client
client = chromadb.Client()

# Create a new collection
collection = client.create_collection("my_collection")

# Convert and store document embeddings using SentenceTransformer
doc_texts = ["Experimenting with RAG (Retrieval-Augmented Generation) for Text Fine-Tuning!.",
             "Today is 20th October 2024 and it's Sunday."]
doc_embeddings = [model.encode(text).tolist() for text in doc_texts]

# Insert the embeddings into the collection
collection.add(
    ids=["doc1", "doc2"],
    embeddings=doc_embeddings,
    metadatas=[{"text": doc_texts[0]}, {"text": doc_texts[1]}]  # Store actual text in metadata
)

# Ask the user for a query  
query_text = input(colored("Enter your query: ", "green"))  # Input prompt in green

# Generate a query embedding using the same model
query_embedding = model.encode(query_text).tolist()

# Search for the most similar vectors in the collection
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

# Extract and print only the most matching result
most_similar_index = 0  # The first result is the most similar
document_id = results['ids'][0][most_similar_index]
document_text = results['metadatas'][0][most_similar_index]['text']
similarity_score = 1 - results['distances'][0][most_similar_index]

# Print the most relevant document in green
print((f"Query is: {query_text}"))
print(colored("Most Matching Document:", "green"))
print((f"Document ID: {document_id}"))
print((f"Text: {document_text}"))
print(colored(f"Similarity Score: {similarity_score:.2f}", "red"))
