def get_context_from_faiss(query: str) -> str:
    # This assumes you’ve done FAISS embedding before
    # See earlier steps for embedding setup
    query_emb = get_embedding(query, model="text-embedding-3-small")
    D, I = index.search(np.array([query_emb]), 3)
    context_rows = df.iloc[I[0]]
    return "\n".join(context_rows["combined"].tolist())
