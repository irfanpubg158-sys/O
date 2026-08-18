# tek_ai.py - TekAI yapay zeka sınıfı
import random
import datetime
import json
import os

class TekAI:
    def __init__(self):
        self.ad = "TekAI"
        self.veri = {}
        self.dosya = "tekai_veri.json"
        self.yukle()
    
    def yukle(self):
        if os.path.exists(self.dosya):
            with open(self.dosya, "r", encoding="utf-8") as f:
                self.veri = json.load(f)
        else:
            self.veri = {"sohbet": {}, "hatirla": []}
    
    def kaydet(self):
        with open(self.dosya, "w", encoding="utf-8") as f:
            json.dump(self.veri, f, indent=2, ensure_ascii=False)
    
    def cevapla(self, mesaj):
        mesaj = mesaj.lower().strip()
        
        if "saat" in mesaj:
            return datetime.datetime.now().strftime("%H:%M")
        if "tarih" in mesaj:
            return datetime.datetime.now().strftime("%d.%m.%Y")
        if "hatırla" in mesaj:
            self.veri["hatirla"].append(mesaj.replace("hatırla", "").strip())
            self.kaydet()
            return "Hatırladım!"
        if "hatırladıkların" in mesaj:
            if self.veri["hatirla"]:
                return "Hatırladıklarım: " + ", ".join(self.veri["hatirla"][-5:])
            return "Henüz bir şey hatırlamıyorum."
        if mesaj in self.veri["sohbet"]:
            return random.choice(self.veri["sohbet"][mesaj])
        if "öğren" in mesaj:
            try:
                anahtar, cevap = mesaj.replace("öğren", "").split("=")
                anahtar = anahtar.strip()
                cevap = cevap.strip()
                if anahtar not in self.veri["sohbet"]:
                    self.veri["sohbet"][anahtar] = []
                self.veri["sohbet"][anahtar].append(cevap)
                self.kaydet()
                return f"Öğrendim: {anahtar} → {cevap}"
            except:
                return "Öğren formatı: öğren kelime=cevap"
        return f"Bilmiyorum. Bana 'öğren {mesaj}=cevap' yazarak öğretebilirsin."
    
    def baslat(self):
        print(f"\n{self.ad} Hazır!")
        while True:
            gir = input("Sen: ")
            if gir.lower() in ["çık", "exit", "kapat"]:
                print("Görüşürüz!")
                break
            print(f"{self.ad}: {self.cevapla(gir)}")
