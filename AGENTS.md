# AGENTS.md

## Proje Amacı

Google Colab ortamında, kullanıcıdan alınan görsel, yapay zeka ile analiz edilecek; içerik dili ne olursa olsun, sosyal medya için Türkçe ve Mermaid diyagramına uygun bir çıktı üretilecek.

## Ortam ve Gereksinimler

- Google Colab (Çevrim içi çalışma)
- Python 3.9+
- langchain
- openai veya Gemini/Gemma API'si
- pillow (görsel işlemleri için)
- tesseract veya uygun OCR kütüphanesi

Gerekli komutlar: !pip install langchain openai pillow pytesseract

## Agent Görev Akışı

1. Colab arayüzünden görseli al.
2. Görsel içeriğini OCR ile metne dönüştür.
3. Metin dili Türkçe değilse, Türkçeye çevir.
4. Metni ve görselin genel yapısını analiz ederek tipini belirle (akış, tablo, süreç diyagramı vb.).
5. Sosyal medya uygun kısa, net, Türkçe açıklama hazırla.
6. Açıklamayı Türkçe Mermaid diyagramına dönüştür.
7. Diyagram kodunu ve Türkçe açıklamayı çıktı olarak göster.

## Sosyal Medya Uyum Kuralları

- Çıktı net, kısa ve anlaşılır olmalı.
- Teknik jargon olabildiğince sadeleştirilmeli.
- Türkçe başlık ve hashtag önerileri agent tarafından hazırlanmalı.
