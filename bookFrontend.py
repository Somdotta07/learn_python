from tkinter import *
import tkinter.font as font
import bookBackend

def get_selected_row(event):
    try:
        global selected_tuple
        index= list.curselection()[0]
        selected_tuple=list.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[3])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[2])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass
    


   
def view_books():
    list.delete(0, END)
    for row in bookBackend.view():
        list.insert(END, row)

def search_book():
    list.delete(0, END)
    for row in bookBackend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list.insert(END, row)

def add_book():
    bookBackend.add(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list.delete(0, END)
    list.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_book():
    bookBackend.delete(selected_tuple[0])

def update_book():
    bookBackend.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

window= Tk()

window.wm_title("BookStore")

myFont = font.Font(family='Courier',weight="bold")
#Labels for Entry
l1=Label(window, text="Title")
l1.grid(row=0, column=0)
l1['font'] = myFont

l2=Label(window, text="Author")
l2.grid(row=0, column=2)
l2['font'] = myFont

l3=Label(window, text="Year")
l3.grid(row=1, column=0)
l3['font'] = myFont

l4=Label(window, text="ISBN")
l4.grid(row=1, column=2)
l4['font'] = myFont

# Entry for books
title_text = StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)
year_text = StringVar()
e2=Entry(window,textvariable=year_text )
e2.grid(row=1, column=1)
author_text = StringVar()
e3=Entry(window,textvariable=author_text )
e3.grid(row=0, column=3)
isbn_text = StringVar()
e4=Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

#List view
list= Listbox(window, width=35, height=7)
list.grid(row=2,column=0, rowspan=6, columnspan=2)

#Scrollbar
sb= Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

list.configure(yscrollcommand=sb.set)
sb.configure(command=list.yview)

list.bind('<<ListboxSelect>>', get_selected_row)

#My buttons
b1=Button(window, text="View all", bg="blue", fg='white', width=12, command=view_books)
b1.grid(row=2, column=3)
b1['font'] = myFont

b2=Button(window, text="Search", background="blue" , fg='white', width=12, command=search_book)
b2.grid(row=3, column=3)
b2['font'] = myFont

b3=Button(window, text="Add", background="blue", width=12, fg='white', command=add_book)
b3.grid(row=4, column=3)
b3['font'] = myFont

b4=Button(window, text="Update", background="blue" , width=12, fg='white', command=update_book)
b4.grid(row=5, column=3)
b4['font'] = myFont

b5=Button(window, text="Delete", background="red", width=12, fg='white', command=delete_book)
b5.grid(row=6, column=3)
b5['font'] = myFont

b6=Button(window, text="Close" , width=12, command=window.destroy)
b6.grid(row=7, column=3)
b6['font'] = myFont
window.mainloop()