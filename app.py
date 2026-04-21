import streamlit as st
from config import get_client
from prompt_template import build_prompt


def generate_explanation(topic):
    client = get_client()
    prompt = build_prompt(topic)

    response = client.chat.completions.create(
        model="groq/compound-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


st.title("EasyExplain AI")

topic = st.text_input("Enter a topic")

if st.button("Generate"):
    if topic:
        result = generate_explanation(topic)
        st.write(result)