# AGENTS.md
## Proje Amacı
Bu projede kullanıcıdan alınan bir görselin içeriği Türkçe olarak açıklanmalı ve açıklama bir Mermaid diyagramına dönüştürülmelidir. Çıktı Türkçe olmalıdır.

## Ortam ve Kurulum
- Python 3.9+
- langchain
- openai (veya başka bir LLM servisi)
- streamlit (web arayüzü için)
- mermaid (diyagram dönüşümü ve gösterimi için)

## Gerekli paketler: 
pip install langchain openai streamlit

## Geliştirme Adımları
1. Kullanıcıdan görsel alın.
2. Görseli OCR (Optik Karakter Tanıma) ile metne çevir.
3. Agent (LLM) ile metni yorumlayıp Türkçe bir diyagram açıklaması oluştur.
4. Açıklamayı Mermaid diyagram koduna dönüştür.
5. Diyagramı Türkçe olarak streamlit arayüzünde göster.
