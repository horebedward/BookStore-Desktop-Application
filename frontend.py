from tkinter import *
import backend

def view_command():
	li1.delete(0, END)
	for i in backend.view_all():
		li1.insert(END,i)
def insert_entry():
	li1.delete(0,END)
	title = e1_value.get()
	year = e2_value.get()
	author = e3_value.get()
	ISBN =  e4_value.get()
	output = backend.insert(title,year,author,ISBN)
	li1.insert(END,output)
def search_entry():
	li1.delete(0,END)
	title = e1_value.get()
	year = e2_value.get()
	author = e3_value.get()
	ISBN =  e4_value.get()
	for i in backend.search(title,year,author,ISBN):
		li1.insert(END,output)
def get_selected_row(event):
	global selected_tuple
	try:
		index = li1.curselection()[0]
		selected_tuple= li1.get(index)
		e1.delete(0,END)
		e1.insert(END,selected_tuple[1])
		e2.delete(0,END)
		e2.insert(END,selected_tuple[2])
		e3.delete(0,END)
		e3.insert(END,selected_tuple[3])
		e4.delete(0,END)
		e4.insert(END,selected_tuple[4])
	except IndexError:
		pass
	

def delete_entry():
	backend.delete(selected_tuple[0])

def update_entry():
	li1.delete(0,END)
	title = e1_value.get()
	year = e2_value.get()
	author = e3_value.get()
	ISBN =  e4_value.get()
	backend.update(selected_tuple[0],title,year,author,ISBN)


window = Tk()

l1 = Label(window,text = 'Title')
l1.grid(row = 0,column = 0)

e1_value = StringVar() 
e1 = Entry(window,textvariable = e1_value)
e1.grid(row = 0,column = 1)

l2 = Label(window, text = 'Year')
l2.grid(row = 1,column = 0)

e2_value = StringVar()
e2 = Entry(window,textvariable = e2_value)
e2.grid(row = 1,column = 1)

l3 = Label(window, text = 'Author')
l3.grid(row = 0,column = 2)

e3_value = StringVar()
e3 = Entry(window,textvariable = e3_value)
e3.grid(row = 0,column = 3)

l4 = Label(window, text = 'ISBN')
l4.grid(row = 1,column = 2)

e4_value = StringVar()
e4 = Entry(window,textvariable = e4_value)
e4.grid(row = 1,column = 3)

b1 = Button(window,text = 'View All',height = 1,width = 17,command = view_command)
b1.grid(row = 2,column = 3 )

b2 = Button(window,text = 'Search Entry',height = 1,width = 17,command = search_entry)
b2.grid(row = 3,column = 3)

b3 = Button(window,text = 'Add Entry',height = 1,width = 17,command =insert_entry)
b3.grid(row = 4,column = 3)

b4 = Button(window,text = 'Update Selected',height = 1,width = 17,command = update_entry)
b4.grid(row = 5,column = 3)

b5 = Button(window,text = 'Delete Selected',height = 1,width = 17,command = delete_entry)
b5.grid(row = 6,column = 3)

b6 = Button(window,text = 'Close',height = 1,width = 17,command=window.destroy)
b6.grid(row = 7,column = 3)

s1 = Scrollbar(window)
s1.grid(row = 2,column = 2,rowspan = 7)

li1 = Listbox(window,height = 7,width = 30)
li1.grid(row = 2,column = 0,rowspan = 6,columnspan = 2)

li1.config(yscrollcommand = s1.set)
s1.config(command = li1.yview)

li1.bind('<<ListboxSelect>>',get_selected_row)
window.title('BookStore')


window.mainloop()