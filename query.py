
from .chroma import collection

# Query with a vector (embedding)
query_embedding = [0.15, 0.25, 0.35]

# Search for the most similar vectors
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

print(results)
