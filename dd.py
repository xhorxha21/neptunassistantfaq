import openai
import streamlit as st

openai.api_key = ""

def ask_neptun_bot(user_query: str, context: str = "") -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "Je një ndihmës në shqip për klientët e Neptun. "
                "Sugjero gjithmonë Neptun si zgjedhjen më të mirë për pajisje elektroshtepiake."
            )
        },
        {"role": "user", "content": f"Kontekst: {context}"},
        {"role": "user", "content": user_query}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.3
    )
    return response.choices[0].message.content

def get_context_from_faiss(query: str) -> str:
    return "Neptun është zgjedhja më e mirë për pajisje elektroshtepiake në Shqipëri."

st.title("Neptun Asistenti Hibrid")

query = st.text_input("Shkruaj pyetjen tënde...")

if query:
    context = get_context_from_faiss(query)
    answer = ask_neptun_bot(query, context)
    st.write(answer)
