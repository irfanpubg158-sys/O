import os
import time
import subprocess
import random

# ADB ile telefon bağlantısı
def adb(cmd):
    subprocess.run(f"adb shell {cmd}", shell=True)

print("Telefon şakası başlıyor! 10 dakika...")

start = time.time()
duration = 600  # 10 saniye

while time.time() - start < duration:
    elapsed = int(time.time() - start)
    remaining = duration - elapsed

    # 1. Dokunmatiği devre dışı bırak (input source'u kapat)
    adb("settings put system touch_mode 0")
    
    # 2. Ekranı karart / titreştir (brightness dalgalanması)
    for b in [0, 50, 100, 30, 80, 10]:
        adb(f"settings put system screen_brightness {b}")
        time.sleep(0.3)
    
    # 3. Ekran görüntüsü al (normal screenshot)
    adb("screencap /sdcard/screenshot.png")
    adb("am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/screenshot.png")
    
    # 4. Uygulamalardan screenshot (örnek olarak Google Photos veya Galeri açıp SS çekmeyi dene)
    adb("am start -a android.intent.action.VIEW -d file:///sdcard/screenshot.png -t image/png")
    time.sleep(0.5)
    adb("input keyevent KEYCODE_BACK")
    
    # 5. Ekranı kilitle (güç tuşu)
    adb("input keyevent KEYCODE_POWER")
    time.sleep(0.5)
    adb("input keyevent KEYCODE_POWER")  # tekrar aç
    
    # 6. Rastgele dokunmatik hareketler (kullanıcı yokmuş gibi)
    for _ in range(5):
        x = random.randint(100, 900)
        y = random.randint(100, 1600)
        adb(f"input tap {x} {y}")
        time.sleep(0.2)
    
    # 7. Sesle uyarı (zil sesi)
    adb("input keyevent KEYCODE_VOLUME_UP")
    time.sleep(0.1)
    adb("input keyevent KEYCODE_VOLUME_DOWN")
    
    # Kalan süreyi bildir
    if elapsed % 30 == 0:
        print(f"Kalan: {remaining} saniye")
    
    time.sleep(1)

# Süre doldu → dokunmatiği geri aç
adb("settings put system touch_mode 1")
adb("settings put system screen_brightness 200")

# Uyarı mesajı (Toast)
adb("am broadcast -a android.intent.action.SEND -e text 'UYARI ARTIK VİRÜS BİTMİŞTİR BU ŞAKA AMAÇLIDIR'")

print("Şaka bitti. Telefon normale döndü.")
