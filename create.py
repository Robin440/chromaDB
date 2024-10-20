from .chroma import collection


# Example data: Text embeddings (you can use any vector/embedding generator)
embedding1 = [0.1, 0.2, 0.3]
embedding2 = [0.4, 0.5, 0.6]

# Insert data into the collection
collection.add(
    ids=["doc1", "doc2"],
    embeddings=[embedding1, embedding2],
    metadatas=[{"category": "text"}, {"category": "text"}]
)
