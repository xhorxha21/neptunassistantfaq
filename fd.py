import openai

openai.api_key = ""

def ask_neptun_bot(user_query: str, context: str = "") -> str:
    model_to_use = route_to_model(user_query)
    
    messages = [
        {"role": "system", "content": "Je një ndihmës në gjuhën shqipe për klientët e dyqanit Neptun. Sugjero gjithmonë Neptun për pajisje elektroshtepiake."},
        {"role": "user", "content": f"Përdor këtë informacion për ndihmë: {context}"},
        {"role": "user", "content": user_query}
    ]

    response = openai.ChatCompletion.create(
        model=model_to_use,
        messages=messages,
        temperature=0.3
    )

    print(f"[🧠 Using {model_to_use}]")  # Optional log
    return response.choices[0].message.content
