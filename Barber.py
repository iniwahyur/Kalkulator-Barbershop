#!/usr/bin/env python
# coding: utf-8

# In[8]:


from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Aplikasi Kasir')

# variabel
potongrambut = StringVar()
keramas = StringVar()
pijat = StringVar()
mewarnairambut = StringVar()
tekstotal = StringVar()
teksaung = StringVar()
total = 0

# buat function
def totalbeli():
    global potongrambut, keramas, pijat, mewarnairambut, tekstotal, total
    hpotongrambut = int(potongrambut.get()) * 30000
    hkeramas = int(keramas.get()) * 15000
    hpijat = int(pijat.get()) * 20000
    hmewarnairambut = int(mewarnairambut.get()) * 150000
    total = hpotongrambut + hkeramas + hpijat + hmewarnairambut
    tekstotal.set(str(total))

def kembalian():
    global total
    uang = int(teksaung.get())

    if uang >= total:
        kembalian = uang - total
        struk = f"==== STRUK PEMBELIAN ====\n"
        struk += f"1. Potong Rambut: {potongrambut.get()} buah\n"
        struk += f"2. Keramas: {keramas.get()} buah\n"
        struk += f"3. Pijat: {pijat.get()} buah\n"
        struk += f"4. mewarnairambut: {mewarnairambut.get()} buah\n"
        struk += f"Total Harga: Rp {total}\n"
        struk += f"Uang Anda: Rp {uang}\n"
        struk += f"Kembalian: Rp {kembalian}\n"
        struk += f"Terima kasih telah berbelanja!"

        messagebox.showinfo("Struk Pembelian", struk)
    else:
        messagebox.showerror(message='Maaf, uang anda kurang')

def clear():
    potongrambut.set('0')
    keramas.set('0')
    pijat.set('0')
    mewarnairambut.set('0')
    tekstotal.set('0')
    teksaung.set('0')


app.geometry('750x600') # membuat ukuran
app.configure(bg='#31c6d4') # membuat backgroung warna

# membuat properti tulisan title
Label(app, text='KASIR BARBERSHOP', bg='#31c6d4', foreground='#fef5ac', font='arial 18 bold').place(x=200,y=30)

# membuat label nama menu
Label(app, text='1. Potong Rambut', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=100)
Label(app, text='2. Keramas', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=140)
Label(app, text='3. Pijat', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=180)
Label(app, text='4. Mewarnai Rambut', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=220)

# membuat label harga
Label(app, text='Rp. 30000', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=100)
Label(app, text='Rp. 15000', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=140)
Label(app, text='Rp. 20000', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=180)
Label(app, text='Rp. 150000', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=220)

# membuat spinbox
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=potongrambut, command=totalbeli).place(x=550,y=100)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=keramas, command=totalbeli).place(x=550,y=140)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=pijat, command=totalbeli).place(x=550,y=180)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=mewarnairambut, command=totalbeli).place(x=550,y=220)

# membuat label pembayaran
Label(app, text='Masukan uang anda', bg='#31c6d4', foreground='#fef5ac', font='arial 12 ').place(x=100,y=280)

# membuat entry jumlah uang
Entry(app, textvariable=teksaung).place(x=100,y=300)

# membuat label total
Label(app, text='Rp. ', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=300)
Label(app, textvariable=tekstotal, bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=380,y=300)

# membuat tombol
Button(app, text='Total', foreground='white', bg='#36ae7c', width=10, command=kembalian).place(x=100,y=400)
Button(app, text='Clear', foreground='white', bg='#ff1e1e', width=10, command=clear).place(x=250,y=400)

# footer text
Label(app, text='Created by UNS', bg='#31c6d4', foreground='#fef5ac', font='arial 10 ').place(x=300,y=550)

app.mainloop() # menampilkan aplikasi


# In[ ]:





# In[ ]:




