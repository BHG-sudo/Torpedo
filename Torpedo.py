from tkinter import *
from tkinter import ttk
import time
import random

def jatek_vege(vége):
    root = Tk()
    root.title("Torpedo")
    root.geometry("1100x160")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    if  vége == "nyert":
        ttk.Label(frm, text="Gratulálok nyertél!", font=("calibre", 100, "normal")).grid(column=1, row=1)
    elif vége == "vesztett":
        ttk.Label(frm, text="Veszítettél!", font=("calibre", 100, "normal")).grid(column=1, row=1)
    root.update()
    time.sleep(5)
    root.destroy()  

def palya_generalas(palya_dict: dict, hajo_dict: dict, flotta):
    palya = []
    if flotta == True:
        for cell ,state in palya_dict.items():
            if state == 0 and hajo_dict.get(cell) == 0:
                palya.append("0")
            if state == 0 and hajo_dict.get(cell) == 1:
                palya.append("8")
            if state == 1 and hajo_dict.get(cell) == 1:
                palya.append("#")
            if state == 1 and hajo_dict.get(cell) == 0:
                palya.append("X")
    else:
        for cell ,state in palya_dict.items():
            if state == 0 and hajo_dict.get(cell) == 0:
                palya.append("0")
            if state == 0 and hajo_dict.get(cell) == 1:
                palya.append("0")
            if state == 1 and hajo_dict.get(cell) == 1:
                palya.append("#")
            if state == 1 and hajo_dict.get(cell) == 0:
                palya.append("X")
    return palya

def frissit():
    ellen_palya = palya_generalas(ellen_palya_dict, ellen_hajo_dict, False)
    jatekos_palya = palya_generalas(jatekos_palya_dict, jatekos_hajo_dict, True)
    counter = 0
    for i in range(10):
        for j in range(10):
            cell = f"{label[j]}{i+1}"
            gombok[cell].configure(text=ellen_palya[counter])
            szoveg[cell].configure(text=jatekos_palya[counter])
            counter += 1
    if ellen_palya.count("#") == 17:
        jatek_vege("nyert")
        root.destroy()
    if jatekos_palya.count("#") == 17:
        jatek_vege("vesztett")
        root.destroy()

def jatekos_tamad(cell):
    ellen_palya_dict[cell] = 1
    rand = random.randint(0, len(ai_tamadasa))
    ai_tamad = ai_tamadasa[rand]
    jatekos_palya_dict[ai_tamad] = 1
    ai_tamadasa.pop(rand)
    frissit()

label = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

ai_tamadasa = []

while len(ai_tamadasa) != 100:
    rand = random.randint(0, 9)
    ah = label[rand] + str(random.randint(1, 10))
    if ah not in ai_tamadasa:
        ai_tamadasa.append(ah)

ellen_palya_dict = {"A1": 0, "B1": 0, "C1": 0, "D1": 0, "E1": 0, "F1": 0, "G1": 0, "H1": 0, "I1": 0, "J1": 0,
                    "A2": 0, "B2": 0, "C2": 0, "D2": 0, "E2": 0, "F2": 0, "G2": 0, "H2": 0, "I2": 0, "J2": 0,
                    "A3": 0, "B3": 0, "C3": 0, "D3": 0, "E3": 0, "F3": 0, "G3": 0, "H3": 0, "I3": 0, "J3": 0,
                    "A4": 0, "B4": 0, "C4": 0, "D4": 0, "E4": 0, "F4": 0, "G4": 0, "H4": 0, "I4": 0, "J4": 0,
                    "A5": 0, "B5": 0, "C5": 0, "D5": 0, "E5": 0, "F5": 0, "G5": 0, "H5": 0, "I5": 0, "J5": 0,
                    "A6": 0, "B6": 0, "C6": 0, "D6": 0, "E6": 0, "F6": 0, "G6": 0, "H6": 0, "I6": 0, "J6": 0,
                    "A7": 0, "B7": 0, "C7": 0, "D7": 0, "E7": 0, "F7": 0, "G7": 0, "H7": 0, "I7": 0, "J7": 0,
                    "A8": 0, "B8": 0, "C8": 0, "D8": 0, "E8": 0, "F8": 0, "G8": 0, "H8": 0, "I8": 0, "J8": 0,
                    "A9": 0, "B9": 0, "C9": 0, "D9": 0, "E9": 0, "F9": 0, "G9": 0, "H9": 0, "I9": 0, "J9": 0,
                   "A10": 0, "B10": 0, "C10": 0, "D10": 0, "E10": 0, "F10": 0, "G10": 0, "H10": 0, "I10": 0, "J10": 0}

ellen_hajo_dict = {"A1": 0, "B1": 0, "C1": 0, "D1": 0, "E1": 0, "F1": 0, "G1": 0, "H1": 1, "I1": 1, "J1": 1,
                   "A2": 0, "B2": 0, "C2": 0, "D2": 0, "E2": 0, "F2": 0, "G2": 0, "H2": 0, "I2": 0, "J2": 0,
                   "A3": 1, "B3": 1, "C3": 1, "D3": 0, "E3": 0, "F3": 0, "G3": 0, "H3": 0, "I3": 0, "J3": 0,
                   "A4": 0, "B4": 0, "C4": 0, "D4": 0, "E4": 0, "F4": 0, "G4": 1, "H4": 0, "I4": 0, "J4": 0,
                   "A5": 0, "B5": 0, "C5": 0, "D5": 0, "E5": 0, "F5": 0, "G5": 1, "H5": 0, "I5": 0, "J5": 0,
                   "A6": 0, "B6": 0, "C6": 0, "D6": 0, "E6": 0, "F6": 0, "G6": 1, "H6": 0, "I6": 0, "J6": 0,
                   "A7": 0, "B7": 0, "C7": 0, "D7": 1, "E7": 0, "F7": 0, "G7": 1, "H7": 0, "I7": 0, "J7": 0,
                   "A8": 0, "B8": 0, "C8": 0, "D8": 1, "E8": 0, "F8": 0, "G8": 1, "H8": 0, "I8": 0, "J8": 0,
                   "A9": 0, "B9": 0, "C9": 0, "D9": 0, "E9": 0, "F9": 0, "G9": 0, "H9": 0, "I9": 0, "J9": 0,
                  "A10": 1, "B10": 1, "C10": 1, "D10": 1, "E10": 0, "F10": 0, "G10": 0, "H10": 0, "I10": 0, "J10": 0}

jatekos_palya_dict= {"A1": 0, "B1": 0, "C1": 0, "D1": 0, "E1": 0, "F1": 0, "G1": 0, "H1": 0, "I1": 0, "J1": 0,
                     "A2": 0, "B2": 0, "C2": 0, "D2": 0, "E2": 0, "F2": 0, "G2": 0, "H2": 0, "I2": 0, "J2": 0,
                     "A3": 0, "B3": 0, "C3": 0, "D3": 0, "E3": 0, "F3": 0, "G3": 0, "H3": 0, "I3": 0, "J3": 0,
                     "A4": 0, "B4": 0, "C4": 0, "D4": 0, "E4": 0, "F4": 0, "G4": 0, "H4": 0, "I4": 0, "J4": 0,
                     "A5": 0, "B5": 0, "C5": 0, "D5": 0, "E5": 0, "F5": 0, "G5": 0, "H5": 0, "I5": 0, "J5": 0,
                     "A6": 0, "B6": 0, "C6": 0, "D6": 0, "E6": 0, "F6": 0, "G6": 0, "H6": 0, "I6": 0, "J6": 0,
                     "A7": 0, "B7": 0, "C7": 0, "D7": 0, "E7": 0, "F7": 0, "G7": 0, "H7": 0, "I7": 0, "J7": 0,
                     "A8": 0, "B8": 0, "C8": 0, "D8": 0, "E8": 0, "F8": 0, "G8": 0, "H8": 0, "I8": 0, "J8": 0,
                     "A9": 0, "B9": 0, "C9": 0, "D9": 0, "E9": 0, "F9": 0, "G9": 0, "H9": 0, "I9": 0, "J9": 0,
                    "A10": 0, "B10": 0, "C10": 0, "D10": 0, "E10": 0, "F10": 0, "G10": 0, "H10": 0, "I10": 0, "J10": 0}

jatekos_hajo_dict = {"A1": 0, "B1": 0, "C1": 0, "D1": 0, "E1": 0, "F1": 0, "G1": 0, "H1": 0, "I1": 0, "J1": 0,
                   "A2": 0, "B2": 1, "C2": 0, "D2": 0, "E2": 0, "F2": 0, "G2": 0, "H2": 0, "I2": 0, "J2": 0,
                   "A3": 0, "B3": 1, "C3": 0, "D3": 0, "E3": 0, "F3": 0, "G3": 1, "H3": 0, "I3": 0, "J3": 0,
                   "A4": 0, "B4": 1, "C4": 0, "D4": 0, "E4": 0, "F4": 0, "G4": 1, "H4": 0, "I4": 0, "J4": 0,
                   "A5": 0, "B5": 1, "C5": 0, "D5": 0, "E5": 1, "F5": 0, "G5": 1, "H5": 0, "I5": 0, "J5": 0,
                   "A6": 0, "B6": 1, "C6": 0, "D6": 0, "E6": 1, "F6": 0, "G6": 0, "H6": 0, "I6": 0, "J6": 0,
                   "A7": 0, "B7": 0, "C7": 0, "D7": 0, "E7": 0, "F7": 0, "G7": 0, "H7": 0, "I7": 0, "J7": 0,
                   "A8": 0, "B8": 0, "C8": 0, "D8": 0, "E8": 0, "F8": 0, "G8": 0, "H8": 0, "I8": 0, "J8": 0,
                   "A9": 0, "B9": 1, "C9": 1, "D9": 1, "E9": 0, "F9": 0, "G9": 0, "H9": 0, "I9": 0, "J9": 0,
                  "A10": 0, "B10": 0, "C10": 0, "D10": 0, "E10": 0, "F10": 0, "G10": 1, "H10": 1, "I10": 1, "J10": 1}

ellen_palya = palya_generalas(ellen_palya_dict, ellen_hajo_dict, False)
jatekos_palya = palya_generalas(jatekos_palya_dict, jatekos_hajo_dict, True)

root = Tk()
root.title("Torpedo")
root.geometry("1280x720")
root.configure(bg="wheat")
gombok = {}
szoveg = {}

jatekos_frame = Frame(root, bg="wheat")
jatekos_frame.grid(column=0, row=0, padx=20, pady=20)

random_frame = Frame(root, bg="wheat")
random_frame.grid(column=1, row=0, padx=20, pady=20)


ellenfel_frame = Frame(root, bg="wheat")
ellenfel_frame.grid(column=2, row=0, padx=20, pady=20)

counter = 0
for i in range(10):
    Label(jatekos_frame, text=label[i], font=("Arial", 14, "bold"), bg="wheat").grid(column=i+1, row=0)
    Label(jatekos_frame, text=i+1, font=("Arial", 14, "bold"), bg="wheat").grid(column=0, row=i+1)
    for j in range(10):
        cell = f"{label[j]}{i+1}"
        lbl = Label(jatekos_frame, text=jatekos_palya[counter], font=("Arial", 14, "bold"),bg="wheat", width=2, height=1, borderwidth=2)
        lbl.grid(column=1+j, row=1+i, padx=1, pady=1)
        szoveg[cell] = lbl

Label(random_frame, text="Játekos", font=("Arial", 20, "bold"), bg="wheat", padx=10).grid(column=0, row=0)
Label(random_frame, text="VS", font=("Arial", 50, "bold"), bg="wheat", padx=10).grid(column=1, row=0)
Label(random_frame, text="Ellenfél", font=("Arial", 20, "bold"), bg="wheat", padx=10).grid(column=2, row=0)


counter = 0
for i in range(10):
    Label(ellenfel_frame, text=label[i], font=("Arial", 14, "bold"), bg="wheat").grid(column=i+1, row=0)
    Label(ellenfel_frame, text=i+1, font=("Arial", 14, "bold"), bg="wheat").grid(column=0, row=i+1)
    for j in range(10):
        cell = f"{label[j]}{i+1}"
        btn = Button(ellenfel_frame, text=ellen_palya[counter], width=2, height=1, font=("Arial", 14, "bold"),bg="wheat", command=lambda c=cell: jatekos_tamad(c))
        btn.grid(column=1+j, row=1+i, padx=1, pady=1)
        gombok[cell] = btn  
        counter += 1

root.mainloop()