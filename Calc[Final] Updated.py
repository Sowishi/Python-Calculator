from tkinter import *
root = Tk()
e = Entry(root,width = 30, borderwidth = 10,bg = "black", fg = "white")
def click(n):
	e.insert(END,n)
def clear():
	e.delete(0,END)
def equal():
	try:
		num = str(e.get())
		e.delete(0,END)
		e.insert(0,eval(num))
	except ZeroDivisionError:
		e.insert(0,"Zero Division Error")
	except:
		e.insert(0,"Invalid input")
def neg():
	num = int(e.get())
	times_2 = num * 2
	e.delete(0,END)
	e.insert(END,num-times_2)
def dele():
	e.delete(0,1)
button_1 = Button(root, text = "1", padx =40, pady = 20,bg = "black", fg = "white",command =lambda: click(1) )

button_2 = Button(root, text = "2", padx =40, pady = 20,bg = "black", fg = "white", command =lambda: click(2) )

button_3 = Button(root, text = "3", padx =40, pady = 20, bg = "black", fg = "white",command =lambda: click(3) )

button_4 = Button(root, text = "4", padx =40, pady = 20, bg = "black", fg = "white",command =lambda: click(4) )

button_5 = Button(root, text = "5", padx =40, pady = 20, bg = "black", fg = "white",command =lambda: click(5) )

button_6 = Button(root, text = "6", padx =40, pady = 20, bg = "black", fg = "white",command =lambda: click(6) )

button_7 = Button(root, text = "7", padx =40, pady = 20, bg = "black", fg = "white",command =lambda: click(7) )

button_8 = Button(root, text = "8", padx =40, pady = 20, bg = "black", fg = "white",command =lambda: click(8) )

button_9 = Button(root, text = "9", padx =40, pady = 20, bg = "black", fg = "white",
command =lambda: click(9) )

button_0 = Button(root, text = "0", padx =115, pady = 20, bg = "black", fg = "white",command =lambda: click(0) )

button_add = Button(root, text = "+", padx =40, pady = 20,bg = "black", fg = "orange", command =lambda: click("+"))

button_minus = Button(root, text = "-", padx =43, pady = 20,bg = "black", fg = "orange", command =lambda: click("-"))

button_mult = Button(root, text = "*", padx =40, pady = 20,bg = "black", fg = "orange", command =lambda: click("*"))

button_div = Button(root, text = "/", padx =40, pady = 20, bg = "black", fg = "orange",command =lambda: click("/"))

button_equal = Button(root, text = "=", padx =40, pady = 20, command =equal,bg = "orange", fg = "white")

button_clear = Button(root, text = "C", padx =40, pady = 20,borderwidth = 3, bg = "black", fg = "white",command=clear)

button_neg = Button(root,text = "+/-",padx = 30, pady = 20, bg = "black", fg = "white",command = neg)

button_del = Button(root,text = "del",padx = 30, pady = 20,bg = "black", fg = "white", command = dele)

button_dot = Button(root,text= ".", padx = 44, pady = 20,bg = "black", fg = "white",command=lambda:click("."))



button_1.grid(row =4, column =0)
button_2.grid(row = 4, column =1)
button_3.grid(row =4, column =2)

button_4.grid(row =3, column =0)
button_5.grid(row =3, column =1)
button_6.grid(row =3, column =2)

button_7.grid(row =2, column =0)
button_8.grid(row =2, column =1)
button_9.grid(row =2, column =2)

button_0.grid(row = 5, column = 0, columnspan = 2)
button_add.grid(row = 1, column = 3)
button_minus.grid(row = 2, column = 3)
button_mult.grid(row= 3,  column = 3)
button_div.grid(row= 4, column = 3)
button_equal.grid(row = 5, column = 3)
button_clear.grid(row= 1, column = 0)
button_neg.grid(row = 1 , column = 1)
button_del.grid(row = 1,column = 2)
button_dot.grid(row = 5, column = 2)

e.grid(row = 0, column = 0,columnspan = 4, padx = 10, pady = 10)
root.mainloop()