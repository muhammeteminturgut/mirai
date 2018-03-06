def main():
    menu_goruntule()
    binary_dosya=dosya_binconvert()
    imei_okuyucu(binary_dosya)


def menu_goruntule():
    print("________________________________________________")
    print("Memin's IMEI Repair And Install (MIRAI 未来)")
    print("Version 1.0 // Coded In TURKEY")
    print("Coded by Muhammet Emin TURGUT")
    print("________________________________________________")

def dosya_binconvert():
    try:
        dosya_adi=input("Please enter *.xqcn file name: ")
        dosya = open(dosya_adi,"r")
        veriler = dosya.read()
        dosya.close()
        print("File Loaded Successfully")
    except:
        print("File Not Found")
        kritik_cikis()
    return veriler

def imei_okuyucu(binary_dosya):
    sorgu=0
    while sorgu<1:
        gir_imei = input("Write your old IMEI Number: ")
        if gir_imei.isdigit() and len(gir_imei)==15:
            islenmis_eski_imei = imei_isleyici(gir_imei)
            sorgu+=1
        else:
            print("Invalid IMEI Number please try again.")
    sorgu=0
    while sorgu<1:
        gir_imei = input("Write your new IMEI Number: ")
        if gir_imei.isdigit() and len(gir_imei)==15:
            islenmis_yeni_imei = imei_isleyici(gir_imei)
            sorgu+=1
        else:
            print("Invalid IMEI Number please try again.")
    yeni_binary = degistirici(islenmis_eski_imei, islenmis_yeni_imei, binary_dosya)
    kaydet(yeni_binary)

def degistirici(islenmis_eski_imei,islenmis_yeni_imei,binary_dosya):
    if islenmis_eski_imei in binary_dosya:
        print("IMEI Number Found in Backup File Yay!")
        binary_dosya = binary_dosya.replace(islenmis_eski_imei, islenmis_yeni_imei)
        print("IMEI Number Changed Successfully")
        return binary_dosya
    else:
        print("IMEI Number Not Found in Backup File")
        kritik_cikis()


def imei_isleyici(eski_imei):
    liste = list()
    islenmis_liste = [0]*9
    imei=""
    for aktarici in eski_imei:
        liste.append(aktarici)
    islenmis_liste[0]="08 "
    islenmis_liste[1] = liste[0]+"A "
    islenmis_liste[2] = liste[2]+liste[1]+" "
    islenmis_liste[3] = liste[4]+liste[3]+" "
    islenmis_liste[4] = liste[6]+liste[5]+" "
    islenmis_liste[5] = liste[8]+liste[7]+" "
    islenmis_liste[6] = liste[10] + liste[9] + " "
    islenmis_liste[7] = liste[12] + liste[11] + " "
    islenmis_liste[8] = liste[14] + liste[13] + " "
    for islenmis_imei in islenmis_liste:
        imei=imei+islenmis_imei
    print("IMEI Converted Successfully: ",imei)
    return imei

def kaydet(yeni_binary):
    try:
        dosya_adi=input("Please enter new file name: ")
        dosya = open(dosya_adi+".xqcn","w")
        dosya.write(yeni_binary)
        print("File Saved")
    except:
        kritik_cikis()

def kritik_cikis():
    print("Failed!")
    exit()

main()