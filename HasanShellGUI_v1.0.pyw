import tkinter as tk
from tkinter import font
import os
import getpass


import HasanShell_v1_1 as HasanShell 

class HasanShellGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("HasanShell GUI v1.0")
        self.root.geometry("850x550")
        self.root.configure(bg="#1e1e1e") # Modern Koyu Tema

        self.custom_font = font.Font(family="Consolas", size=11)
        
        # --- ÜST PANEL: TELİF MÜHRÜ ---
        self.ust_panel = tk.Frame(root, bg="#2d2d2d", height=40)
        self.ust_panel.pack(fill=tk.X, side=tk.TOP)
        
        self.ust_etiket = tk.Label(
            self.ust_panel, 
            text=f" 💻 {getpass.getuser()}@HasanShell | Copyright (c) 2026 Hasan Enes Koç (Hasan Developer)", 
            fg="#a9b7c6", bg="#2d2d2d", font=self.custom_font
        )
        self.ust_etiket.pack(side=tk.LEFT, padx=10, pady=8)

        # --- ORTA PANEL: ÇIKTI EKRANI ---
        self.scrollbar = tk.Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.cikti_ekrani = tk.Text(
            root, bg="#1e1e1e", fg="#a9b7c6", insertbackground="white",
            selectbackground="#2f65ca", font=self.custom_font, 
            yscrollcommand=self.scrollbar.set, bd=0, highlightthickness=0
        )
        self.cikti_ekrani.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        self.scrollbar.config(command=self.cikti_ekrani.yview)

        # İlk Başlangıç Logları
        self.cikti_yazdir("HasanShell [Version 1.0] - Görsel Arayüz Katmanı\n")
        self.cikti_yazdir("Copyright (c) 2026 Hasan Enes Koç (Hasan Developer). All rights reserved.\n")
        self.cikti_yazdir("Sistem Çekirdeği: HasanShell_v1.1.py başarıyla bağlandı.\n") # Düzeltildi ✅
        self.cikti_yazdir("-" * 80 + "\n\n")

        # --- ALT PANEL: GİRDİ SATIRI ---
        self.alt_panel = tk.Frame(root, bg="#252526")
        self.alt_panel.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=10)

        self.prompt_etiket = tk.Label(self.alt_panel, text=" > ", fg="#6246ea", bg="#252526", font=self.custom_font)
        self.prompt_etiket.pack(side=tk.LEFT, padx=5)

        self.giris_kutusu = tk.Entry(
            self.alt_panel, bg="#2d2d2d", fg="#ffffff", insertbackground="#6246ea", font=self.custom_font,
            bd=0, highlightthickness=1, highlightbackground="#3e3e42", highlightcolor="#6246ea"
        )
        self.giris_kutusu.pack(fill=tk.X, expand=True, side=tk.LEFT, ipady=8, padx=5)
        
        # Enter'a basınca komutu tetikle
        self.giris_kutusu.bind("<Return>", self.girdiyi_hasanshelle_gonder)
        self.giris_kutusu.focus_set()

    def cikti_yazdir(self, metin):
        self.cikti_ekrani.insert(tk.END, metin)
        self.cikti_ekrani.see(tk.END)

    def girdiyi_hasanshelle_gonder(self, event):
        girdi = self.giris_kutusu.get().strip()
        self.giris_kutusu.delete(0, tk.END)

        if not girdi: return
        if girdi.lower() in ["cikis", "exit"]:
            self.root.quit()
            return

        # Kullanıcının yazdığı komutu önce ekrana bas
        self.cikti_yazdir(f"{getpass.getuser()}@HasanShell [{os.getcwd()}] > {girdi}\n")

        # --- DÜZELTİLEN BORU HATTI (PIPELINE) ---
        # Yukarıdaki büyük harfli takma isme (HasanShell) tam uyumlu hale getirildi ✅
        cevap = HasanShell.shell_komut_tetikle(girdi)

        # Çekirdekten gelen özel emirlere göre GUI aksiyon alıyor
        if cevap == "CLS_EMRI":
            self.cikti_ekrani.delete("1.0", tk.END)
        else:
            # HasanShell çekirdeğinin ürettiği saf cevabı ekrana yazdırıyor
            self.cikti_yazdir(cevap + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = HasanShellGUI(root)
    root.mainloop()
