# Görselden Mermaid

Bu uygulama, kullanıcıdan alınan bir görseldeki metni OCR ile çıkarır,
Türkçeye çevirir ve bir Mermaid diyagramı oluşturur. Streamlit arayüzü ile
sonuçlar Türkçe olarak gösterilir.

## Kurulum

Tesseract OCR'yi kurun:

```bash
sudo apt-get install tesseract-ocr
```

Gerekli Python paketlerini yükleyin:

```bash
pip install -r requirements.txt
```

OpenAI API anahtarınızı `OPENAI_API_KEY` ortam değişkeni olarak ayarlayın.

## Çalıştırma

```bash
streamlit run app.py
```
