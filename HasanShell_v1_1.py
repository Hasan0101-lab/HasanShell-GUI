import os
import getpass
import subprocess

def shell_komut_tetikle(girdi):
    """GUI veya Terminalden gelen girdi paketini HasanShell zırhıyla çalıştırır."""
    girdi = girdi.strip()
    if not girdi:
        return ""
        
    # Ekran temizleme emri verilirse GUI'ye özel kod gönder
    if girdi.lower() in ["cls", "clear"]:
        return "CLS_EMRI"
        
    # HasanShell'in meşhur cd tırnak temizleme zırhı çalışıyor
    if girdi.startswith("cd "):
        hedef_dizin = girdi[3:].strip().strip('"').strip("'")
        try:
            os.chdir(hedef_dizin)
            return f"Dizin değiştirildi: {os.getcwd()}\n"
        except FileNotFoundError:
            return f"[Error]: Dizin bulunamadı -> '{hedef_dizin}'\n"
        except Exception as e:
            return f"[Error]: {e}\n"
            
    try:
        # Komut çalışır ve çıktıyı GUI'ye döndürmek için yakalar
        sonuc = subprocess.run(girdi, shell=True, text=True, capture_output=True)
        
        # Çıktıları birleştirip tek bir paket halinde GUI'ye fırlatıyoruz
        çıktı = sonuc.stdout + sonuc.stderr
        
        if sonuc.returncode != 0 and not sonuc.stderr:
            çıktı += f"\n[HasanShell]: Komut {sonuc.returncode} hata kodu ile tamamlandı.\n"
            
        return çıktı
    except Exception as hata:
        return f"[System Error]: {hata}\n"

# Eğer bu dosya doğrudan terminalde çalıştırılırsa saf haliyle çalışmaya devam eder
if __name__ == "__main__":
    if os.name == 'nt': os.system("") # Windows ANSI aktif etme hilesi
    os.system('cls' if os.name == 'nt' else 'clear')
    print("HasanShell [Version 1.1]\nCopyright (c) 2026 Hasan Enes Koç (Hasan Developer). All rights reserved.\n")
    while True:
        try:
            girdi = input(f"{getpass.getuser()}@HasanShell [{os.getcwd()}] > ")
            if girdi.lower() in ["exit", "cikis"]: break
            cevap = shell_komut_tetikle(girdi)
            if cevap != "CLS_EMRI": print(cevap)
            else: os.system('cls' if os.name == 'nt' else 'clear')
        except KeyboardInterrupt: break