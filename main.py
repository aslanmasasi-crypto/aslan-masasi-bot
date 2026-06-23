import os
from instagrapi import Client
import requests
from PIL import Image

# Instagram'a giriş
cl = Client()
cl.login(os.getenv("INSTA_USER"), os.getenv("INSTA_PASS"))

# 1. Haber fotoğrafını indir
img_url = "BURAYA_HABER_FOTOĞRAF_LİNKİNİ_YAPIŞTIR"
response = requests.get(img_url, stream=True)
with open('haber.jpg', 'wb') as f:
    f.write(response.content)

# 2. İşlemleri yap
haber = Image.open('haber.jpg').convert("RGBA")
sablon = Image.open('sablon.png').convert("RGBA")

# Haber fotoğrafını 1080x1080 yap ve çerçeveyi üzerine yapıştır
haber = haber.resize((1080, 1080))
haber.paste(sablon, (0, 0), sablon)

# Kaydet
haber.convert("RGB").save('post.jpg')

# 3. Paylaş
cl.photo_upload("post.jpg", "Aslan Masası Gündem! #Galatasaray #Transfer #AslanMasası #Cimbom #Keşfet ")
