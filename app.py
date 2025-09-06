import json
from typing import Dict

import pytesseract
import streamlit as st
from PIL import Image
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)


def translate_to_turkish(text: str) -> str:
    """Metni OpenAI üzerinden Türkçeye çevir."""
    if not text.strip():
        return ""
    messages = [
        SystemMessage(content="Sen metinleri Türkçeye çeviren bir çeviri asistanısın."),
        HumanMessage(content=text),
    ]
    return llm.invoke(messages).content.strip()


def diagram_from_text(text: str) -> Dict[str, str]:
    """Diyagram türü, Türkçe açıklama ve Mermaid kodu üret."""
    prompt = (
        "Aşağıdaki metne göre diyagramın türünü belirle, "
        "kısa bir Türkçe açıklama yaz ve buna uygun Mermaid kodu üret. "
        "Sonucu JSON olarak {type, description, mermaid} formatında ver.\n"
        f"Metin: {text}"
    )
    messages = [HumanMessage(content=prompt)]
    try:
        content = llm.invoke(messages).content.strip()
        return json.loads(content)
    except Exception:
        return {"type": "", "description": "", "mermaid": ""}


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
