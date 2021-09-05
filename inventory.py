from tkinter import*
from tkinter import messagebox
winds= Tk()
winds.title("Manager")
winds.geometry("1000x400")
winds.configure(bg='green4')

def Insert_data():
   
   ID = str(Enter_id.get())
   Prd_name = str(Enter_name.get())
   SP= str(Enter_sp.get())
   QTY=str(Enter_qt.get())


   if (len(SP) > 0 and len(QTY) > 0 and len(Prd_name) > 0 and len(ID) > 0):
      check = open('Managedata.txt', 'a')
      check1 = open('Managedata.txt', 'r')
      test= check1.read()
      
      if ID in test :  
         messagebox.showwarning("title", "number already exists")

      else:
         check.write(f"\t\t{ID}\t\t{Prd_name}\t\t{SP}\t {QTY}\n") 
         messagebox.showinfo("Info", "information is executed")
   elif (len(ID) == 0 or len(Prd_name) == 0 or len(SP) == 0 or len(QTY) == 0):
      messagebox.showwarning("warning","Entries are empty")
    
   Enter_id.delete(0, END)
   Enter_name.delete(0,END)
   Enter_sp.delete(0, END)
   Enter_qt.delete(0, END)

def Info_view():
    c = 0
    file= open("Managedata.txt", "r")
    for content in file:
        c += 1
        text1.insert(INSERT, c)
        text1.insert(INSERT, content)
    file.close()   

def clear():
   text1.delete(0.0, END)  

frame=LabelFrame(winds,text="Inventory Management",width=50, height=50,background="SeaGreen1")
frame.pack(expand="yes", fill="both", pady=5, side="left")

frame1=LabelFrame(winds,text="Product List",width=300, height=20,background="SeaGreen1")
frame1.pack(expand="yes", fill="both", pady=5, side="right")

Item_no= Label(frame1, text="Item no:", relief="solid", width=15)
Item_no.place(x=0,y=1)

Productid=Label(frame1,text="product id:",relief="solid",width=15)
Productid.place(x=110,y=1)

Name=Label(frame1,text="Name:",relief="solid", width=15)
Name.place(x=220,y=1)

Selling_Price=Label(frame1,text="Selling price",relief="solid", width=15)
Selling_Price.place(x=330,y=1)

Quantity1=Label(frame1,text="Quantity:",relief="solid", width=15)
Quantity1.place(x=440,y=1)

text1=Text(frame1,width=70,height=20)
text1.place(x=0,y=30)

product_id=Label(winds,text="Product id:",bg="SeaGreen1",)
product_id.place(x=15,y=30)
Enter_id=Entry(winds,width=25,borderwidth=2)
Enter_id.place(x=15,y=50)

product_name=Label(winds,text="Product Name:",bg="SeaGreen1")
product_name.place(x=15,y=70)
Enter_name=Entry(winds,width=25,borderwidth=2)
Enter_name.place(x=15,y=90)

selling_price=Label(winds,text="Selling price:",bg="SeaGreen1")
selling_price.place(x=15,y=110)
Enter_sp=Entry(winds,width=25,borderwidth=2)
Enter_sp.place(x=15,y=130)

quantity =Label(winds,text="Quantity:",bg="SeaGreen1")
quantity.place(x=15,y=150)
Enter_qt=Entry(winds,width=25,borderwidth=2)
Enter_qt.place(x=15,y=170)

Insert_button=Button(frame,text="Insert",borderwidth=1,bg="cyan",fg="blue4",padx=2,pady=2,command=Insert_data)
Insert_button.place(x=10,y=190)

Show_button=Button(frame,text="show",borderwidth=1,bg="cyan",fg="blue4",command=Info_view)
Show_button.place(x=60,y=190)

Clear_button=Button(frame,text="Clear",borderwidth=1,bg="cyan",fg="blue4",command=clear)
Clear_button.place(x=110,y=190)

Exit_button=Button(frame,text="Exit",borderwidth=1,bg="cyan",fg="blue4",command=winds.quit)
Exit_button.place(x=160,y=190)

winds.mainloop()
