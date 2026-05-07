import tkinter as tk

sklep=tk.Tk()
sklep.title("Sklep internetowy")
sklep.geometry("400x500")


produkty={
    "Kanapa":4000,
    "Łóżko": 5000,
    "Zmywarka":2500,
    "Pralka":1800,
    "Lodówka":3200,
}
koszyk={}
rabat_kod="5398"
rabat_procent=25
def dodaj_do_koszyka():
    wybrany_produkt=lista_produkty.get(tk.ACTIVE)
    cena_produktu=produkty[wybrany_produkt]
    if wybrany_produkt not in koszyk:
        koszyk[wybrany_produkt]=(cena_produktu,1)
    else:
        koszyk[wybrany_produkt]=(cena_produktu,koszyk[wybrany_produkt][1]+1)

    aktualizuj_koszyk()

def usun_z_koszyka():
    wybrany_produkt=lista_produkty.get(tk.ACTIVE)
    if wybrany_produkt in koszyk and koszyk[wybrany_produkt][1]>1:
        koszyk[wybrany_produkt]=(koszyk[wybrany_produkt][0],koszyk[wybrany_produkt][1]-1)
    elif wybrany_produkt in koszyk:
        del koszyk[wybrany_produkt]
    aktualizuj_koszyk()

def rabat():
    kod=entry_rabat.get()
    if kod==rabat_kod:
        for produkt, (cena,ilosc) in koszyk.items():
            nowa_cena=cena-(cena*rabat_procent/100)
            koszyk[produkt]=(nowa_cena,ilosc)
            aktualizuj_koszyk()

def usun_caly():
    koszyk.clear()
    aktualizuj_koszyk()

def aktualizuj_koszyk():
    text_koszyk.delete(1.0,tk.END)
    text_koszyk.insert(tk.END,"Koszyk: \n" )
    suma_cen=0
    for produkt,(cena,ilosc) in koszyk.items():
        text_koszyk.insert(tk.END,f"{produkt} - {cena} zł x {ilosc} \n")
        suma_cen+=cena*ilosc
    text_koszyk.insert(tk.END,f"\n Suma cen: {suma_cen} zł")

def zapis_do_pliku():
    global suma_cen
    with open("koszyk.txt","w",encoding="utf-8") as plik:
        plik.write("Zawartosc koszyka:/n")
        for produkt,(cena,ilosc) in koszyk.items():
            plik.write(f"{produkt}- {cena} zł {ilosc} \n")

label_wybor=tk.Label(sklep,text="Wybierz produkt:")
label_wybor.pack()

lista_produkty=tk.Listbox(sklep,selectmode=tk.SINGLE,width=25,height=9,justify="center",foreground="blue")
for produkt in produkty:
    lista_produkty.insert(tk.END,produkt)
lista_produkty.pack()

button_dodaj=tk.Button(sklep,text="Dodaj produkt do koszyka",font=10,background="red",border=3,command=dodaj_do_koszyka)
button_dodaj.pack()

button_usun=tk.Button(sklep,text="Usuń z koszyka",font=10,background="yellow",border=3,command=usun_z_koszyka)
button_usun.pack()

button_usun_cale=tk.Button(sklep,text="Usuń wszystko",font=10,background="purple",border=3,command=usun_caly)
button_usun_cale.pack()

label_rabat=tk.Label(sklep,text="kod rabatowy:")
label_rabat.pack()

entry_rabat=tk.Entry(sklep)
entry_rabat.pack()

button_rabat=tk.Button(sklep,text="Użyj rabatu",font=10,background="orange",border=3,command=rabat)
button_rabat.pack()
button_zapisz=tk.Button(sklep,text="zapisz do pliku",font=10,background="gray",border=3,command=zapis_do_pliku)
button_zapisz.pack()

text_koszyk=tk.Text(sklep,height=10,width=30,foreground="green")
text_koszyk.pack()



sklep.mainloop()