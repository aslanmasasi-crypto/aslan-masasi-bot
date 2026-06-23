import os
import feedparser
from instagrapi import Client

# 1. Instagram Giriş Ayarları
cl = Client()
USERNAME = os.getenv("INSTA_USER")
PASSWORD = os.getenv("INSTA_PASS")

def paylas():
    # Galatasaray haberleri için örnek RSS (Kendi linkini buraya yapıştır)
    RSS_URL = "https://www.google.com/alerts/feeds/12345/67890" 
    feed = feedparser.parse(RSS_URL)
    
    # Sadece en son gelen haberi al
    if not feed.entries:
        print("Yeni haber yok.")
        return

    son_haber = feed.entries[0]
    baslik = son_haber.title
    link = son_haber.link
    
    # 2. Instagram'a Giriş Yap ve Paylaş
    try:
        cl.login(USERNAME, PASSWORD)
        caption = f"{baslik}\n\nDetaylar için profildeki linke tıkla! 🦁 #Galatasaray #AslanMasası"
        # Not: instagrapi ile sadece metin paylaşılmaz, fotoğraf gerekir.
        # Eğer haberin görselini çekemiyorsan, sabit bir "Aslan Masası" görseli kullan.
        cl.photo_upload("haber_gorseli.jpg", caption)
        print("Paylaşım başarılı!")
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    paylas()
