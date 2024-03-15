from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

root =Tk()                                  
root.title("Unautomated Wordle")             #titlul

root.geometry("400x400")    #dimensiunea de inceput
root.minsize(400, 400)      #dimensiunea minima
root.maxsize(400, 400)      #dimensiunea maxima

#culorile folosite

bg_color="#e6ffff"
root.config(background=bg_color)

#variabile

entr = []                                   #matricea cu entry-points
text = []                                   #matricea necesara pt. litere

nume_fisier_cuvinte ="cuvinte.txt"
cuvant_random = ""          #cuvantul care trebuie ghicit
padx_casute = 3             #pad x dintre casute/entry-uri
pady_casute = 3             #pad y dintre casute/entry-uri
cnt = 0                     #numarul de incercari

#generare cuvant random

nr_cuvant=random.randint(1,11454)
contor=0
file = open(nume_fisier_cuvinte, "r")
for x in file:
  contor+=1
  if contor==nr_cuvant:
    cuvant_random=x
    break

#functii

#erorile posibile

def eroare(x):
    if x==1 :    
        messagebox.showwarning("Error 1", "Se pot introduce doar litere!")
    if x==2 :
        messagebox.showwarning("Error 2", "Nu poti lasa casute necompletate!")
    if x==3 :
        messagebox.showwarning("Error 3", "Nu poti introduce mai mult de o litera pe casuta!")
    if x==4 :
        messagebox.showwarning("Error 4", "Cuvantul introdus nu exista in lista de cuvinte acceptate!")

    #stergere
    for i in range (0,5):
        entr[0][i].delete(0,END) 

    return


#functia de verificare a cuvantului introdus

def verificare():
    
    for i in range (5):
        litera=str(entr[0][i].get())
        
        if len(litera)==0 :
            eroare(2)
            return False

        if len(litera) > 1:
            eroare(3)
            return False

        if litera.isalpha() == False: 
            eroare(1)
            return False

    #cuvant_format este de fapt cuvantul pe care incearca utilizatorul sa l introduca

    cuvant_format= entr[0][0].get()+entr[0][1].get()+entr[0][2].get()+entr[0][3].get()+entr[0][4].get()+"\n"
    cuvant_format= cuvant_format.upper()
    
    #aici se verifica daca exista cuvantul in lista de cuvinte accepate

    file = open(nume_fisier_cuvinte, "r")
    for x in file:
        if x==cuvant_format : return True
    
    eroare(4)
    return False

#algoritmul care simuleaza de fapt jocul

def move():

    #verificare daca textul introdus respecta conditiile necesare

    if verificare() == False:
        return

    #marire contor nr. cuvinte

    global cnt
    cnt += 1
    count.config(text=str(cnt))


    #fiecare casuta copiaza litera de deasupra ei 

    for i in range(4, 0, -1):
        for j in range(4, -1, -1):                                  
            text[i-1][j-1].set(entr[i-1][j].get().upper())              

    #pt fieacare litera, algoritmul ii gaseste cate o culoare

    for i in range(1,5):
        for j in range (0,5):
            if entr[i][j].get() == cuvant_random[j]:
                entr[i][j].config(disabledbackground="lightgreen")
            else:
                if entr[i][j].get() in cuvant_random and entr[i][j].get() not in " ":
                    entr[i][j].config(disabledbackground="yellow")
                else: entr[i][j].config(disabledbackground="lightgrey")
    
    #verificare daca a fost ghicit cuvantul

    ok = True
    for j in range (0,5):
        if entr[1][j].get() != cuvant_random[j]:
            ok = False

    #daca a fost gasit cuvantul, programul se opreste si afiseaza mesajul cu felicitari

    if ok == True:
        buton.config(state="disabled")
        mesaj_final.config(text=str("Felicitari, ai ghicit din "+ str(cnt) + " incercari!"))
        mesaj_final.grid(row=8, column= 1, columnspan=10)
        for i in range (0,5):
            entr[0][i].delete(0,END) 
            entr[0][i].config(state="disabled")

        return

    #preluare cuvant de pe linia 0

    cuvant=""
    for i in range(0,5):
        cuvant += (entr[1][i].get())
    cuvant=cuvant.upper()

    #stergerea liniei nr 0

    for i in range(5):
        entr[0][i].delete(0,END)                          

#bind pt. tasta enter

def key_bind_enter(event):
    move() 
    event.widget.tk_focusNext().focus()

#bind pt. orice litera <=> tab

def key_bind_tab(event):
    var=event.keysym_num
    if  var>= ord("A") and var<= ord("Z") or var>= ord("a") and var<= ord("z"):
        event.widget.tk_focusNext().focus()

#key binding

root.bind('<Return>' , key_bind_enter)      #bind-ul pentru enter care activeaza functia move()
root.bind_all('<Key>', key_bind_tab)        #bind-ul pt orice litera introdusa              
    
    
    
#label-uri folosite:

spatiu = Label(root, width=12, bg=bg_color)          
header = Label(root, text="             Introdu un cuvant!",font=("arial",12), bg=bg_color)
counter = Label(root, text="Numarul de \n incercari:", font=("arial",12 ), bg=bg_color)
count = Label(root, text=str(cnt), font=("arial",12 ), bg=bg_color)
mesaj_final = Label(root, text=str("Felicitari, ai ghicit din "+ str(cnt) + " incercari!"), font=("arial",12), bg=bg_color)

#
cvnt = Label(root, text=cuvant_random, bg=bg_color)
#


#butoane

buton = Button(root, text="Start", command=move)


#crearea matricei text, necesara pt preluare literelor de pe pozitii i-1

for i in range(0, 5):
    lin=[]
    for j in range(0,5):
        var=StringVar()
        lin.append(var)
    text.append(lin)


#crearea grid-ului de entry points

for i in range(1,6):
    linie_entr = [] 
    if i==1:
        for j in range(1,6):
            ent=Entry(root,width=2,font=("arial",24),state="normal", justify="center" )
            linie_entr.append(ent)
        entr.append(linie_entr)
    else:
        for j in range(1,6):
            ent= Entry(root,width=2,font=("arial",24,),state="disabled", justify="center",
                         textvariable=text[i-2][j-2], disabledbackground="lightgray",fg="black")
            linie_entr.append(ent)
        entr.append(linie_entr)


# afisare grid

spatiu.grid(row=0, column=0)
header.grid(row=0, column=1, columnspan=4)

for i in range(1,6):
    for j in range(1,6):    
            entr[i-1][j-1].grid(row=i, column=j, padx=padx_casute, pady=pady_casute)

spatiu.grid(row=6)
counter.grid(row=7, column=1,columnspan=2)
count.grid(row=7, column=3)
buton.grid(row=7, column=4, columnspan=3)


#linia de jos e folosita pt teste
#daca o scoti din comentariu, interfata o sa ti afiseze
#cuvantul pe care ar trebui jucatorul sa-l ghiceasca

#cvnt.grid(row=9)
#

root.mainloop()

