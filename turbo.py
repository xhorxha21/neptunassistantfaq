def route_to_model(query: str) -> str:
    query_lower = query.lower()
    if any(keyword in query_lower for keyword in ["oferta", "krahasim", "cilësia", "me i miri", "detaje", "avantazhet"]):
        return "gpt-4"  
    return "gpt-3.5-turbo"  
