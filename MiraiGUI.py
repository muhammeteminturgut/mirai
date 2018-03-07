from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
def main():
    #Temel Pencere Ayarları
    pencere = tk.Tk()
    pencere.iconbitmap('favicon.ico')
    pencere.wm_title("Mirai 1.0 (未来)")
    pencere.resizable(False, False)

    global yedekVerisi
    yedekVerisi="None"
    def binarydosya():
        global yedekVerisi
        konum = askopenfilename(filetype=(("Qualcomm Backup File", "*.xqcn;*.qcn"),) )
        if konum is "":
            return
        else:
            konumText.set(konum)
            dosya = open(konum,"r")
            yedekVerisi = dosya.read()
            dosya.close()

    def eskiImeiLimit(*args):
        deger = eskiimei.get()
        if len(deger) > 15: eskiimei.set(deger[:15])

    def yeniImeiLimit(*args):
        deger = yeniimei.get()
        if len(deger) > 15: yeniimei.set(deger[:15])

    def hakkinda():
        tk.messagebox.showinfo("About", "Memin's IMEI Repair And Install ( Mirai  未来 ) Version 1.0 GUI. For Devices with Qualcomm Snapdragon processors.")
        tk.messagebox.showinfo("About", "Coded In TURKEY | Coded by Muhammet Emin TURGUT | Coded with Pure Python 3")

    def imei_okuyucu(yedekVerisi):
        gir_imei = eskiimei.get()
        if gir_imei.isdigit() and len(gir_imei) == 15:
            islenmis_eski_imei = imei_isleyici(gir_imei)
        else:
            tk.messagebox.showerror("Error", "Invalid old IMEI number please try again.")
        gir_imei = yeniimei.get()
        if gir_imei.isdigit() and len(gir_imei) == 15:
            islenmis_yeni_imei = imei_isleyici(gir_imei)
        else:
            tk.messagebox.showerror("Error", "Invalid new IMEI number please try again.")
        degistirici(islenmis_eski_imei, islenmis_yeni_imei, yedekVerisi)

    def kaydet(yeni_binary):
        try:
            dosya = asksaveasfile(mode='w', defaultextension=".xqcn", filetypes=(("Qualcomm Backup File", "*.xqcn"),))
            if dosya is None:
                return
            dosya.write(yeni_binary)
            dosya.close()
            tk.messagebox.showinfo("Yay!", "New IMEI wrote successfully.")
        except:
            tk.messagebox.showerror("Error", "File save Error!")

    def imei_isleyici(eski_imei):
        liste = list()
        islenmis_liste = [0] * 9
        imei = ""
        for aktarici in eski_imei:
            liste.append(aktarici)
        islenmis_liste[0] = "08 "
        islenmis_liste[1] = liste[0] + "A "
        islenmis_liste[2] = liste[2] + liste[1] + " "
        islenmis_liste[3] = liste[4] + liste[3] + " "
        islenmis_liste[4] = liste[6] + liste[5] + " "
        islenmis_liste[5] = liste[8] + liste[7] + " "
        islenmis_liste[6] = liste[10] + liste[9] + " "
        islenmis_liste[7] = liste[12] + liste[11] + " "
        islenmis_liste[8] = liste[14] + liste[13] + " "
        for islenmis_imei in islenmis_liste:
            imei = imei + islenmis_imei
        return imei

    def degistirici(islenmis_eski_imei, islenmis_yeni_imei, binary_dosya):
        if islenmis_eski_imei in binary_dosya:
            binary_dosya = binary_dosya.replace(islenmis_eski_imei, islenmis_yeni_imei)
            kaydet(binary_dosya)
        else:
            tk.messagebox.showerror("Error", "IMEI Number Not Found in Backup File.")


    #Grup 1
    grup1 = LabelFrame(pencere, text=" File: ")
    grup1.grid(row=1, columnspan=7, sticky='SWEN',padx=10, pady=10, ipadx=5, ipady=5)
    konumText = StringVar()
    ttk.Label(grup1, text = " xqcn File: ").grid(row=0,column=0)
    ttk.Entry(grup1,textvariable=konumText).grid(row=0,column=1)
    ttk.Button(grup1, text="Browse", command=binarydosya, width=10).grid(row=0,column=2,padx=5)
    #Grup 2
    grup2 = LabelFrame(pencere, text=" IMEI Settings: ")
    grup2.grid(row=2, columnspan=7, sticky='SWEN',padx=10,ipadx=5, ipady=5)
    eskiimei = StringVar()
    eskiimei.trace('w', eskiImeiLimit)
    yeniimei= StringVar()
    yeniimei.trace('w', yeniImeiLimit)
    ttk.Label(grup2,text=" Old IMEI: ",width=15).grid(row=0,column=0)
    ttk.Label(grup2,text=" New IMEI: ",width=15).grid(row=1,column=0,ipady=5)
    ttk.Entry(grup2,textvariable=eskiimei).grid(row=0,column=1)
    ttk.Entry(grup2, textvariable=yeniimei).grid(row=1, column=1)
    #Alt Pencere
    ttk.Button(pencere, text="Replace", command=lambda: imei_okuyucu(yedekVerisi), width=10).grid(row=3, column=0, pady=5, padx=8,ipadx=31)
    ttk.Button(pencere, text="About", command=hakkinda, width=10).grid(row=3, column=3, pady=5,ipadx=31)
    #Pencere Ortalayıcı
    pencere.attributes('-alpha', 0.0)
    pencere.update_idletasks()
    width = pencere.winfo_width()
    frm_width = pencere.winfo_rootx() - pencere.winfo_x()
    win_width = width + 2 * frm_width
    height = pencere.winfo_height()
    titlebar_height = pencere.winfo_rooty() - pencere.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = pencere.winfo_screenwidth() // 2 - win_width // 2
    y = pencere.winfo_screenheight() // 2 - win_height // 2
    pencere.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    pencere.deiconify()
    pencere.attributes('-alpha', 1.0)
    ###############################
    tk.messagebox.showwarning("DISCLAIMER", "This program is for EDUCATIONAL PURPOSES ONLY. Don't use them for illegal activities. You are responsable for your actions!")
    tk.mainloop()

main()