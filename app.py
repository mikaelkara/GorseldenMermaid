import json
from typing import Dict

import openai
import pytesseract
import streamlit as st
from PIL import Image


def translate_to_turkish(text: str) -> str:
    """Translate arbitrary text into Turkish using OpenAI."""
    if not text.strip():
        return ""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Sen metinleri Türkçeye çeviren bir çeviri asistanısın."
                ),
            },
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message["content"].strip()


def diagram_from_text(text: str) -> Dict[str, str]:
    """Generate diagram type, Turkish description and Mermaid code."""
    prompt = (
        "Aşağıdaki metne göre diyagramın türünü belirle, "
        "kısa bir Türkçe açıklama yaz ve buna uygun Mermaid kodu üret. "
        "Sonucu JSON olarak {type, description, mermaid} formatında ver.\n"
        f"Metin: {text}"
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    content = response.choices[0].message["content"].strip()
    return json.loads(content)


st.set_page_config(page_title="Görselden Mermaid")
st.title("Görselden Mermaid Diyagramı")

uploaded = st.file_uploader("Bir görsel yükleyin", type=["png", "jpg", "jpeg"])

if uploaded:
    image = Image.open(uploaded)
    st.image(image, caption="Yüklenen Görsel", use_column_width=True)

    extracted = pytesseract.image_to_string(image)
    turkish_text = translate_to_turkish(extracted)

    result = diagram_from_text(turkish_text)

    st.subheader("Diyagram Türü")
    st.write(result.get("type", ""))

    st.subheader("Açıklama")
    st.write(result.get("description", ""))

    st.subheader("Mermaid Kod")
    code = result.get("mermaid", "")
    st.code(code, language="markdown")
    st.markdown(f"```mermaid\n{code}\n```")
