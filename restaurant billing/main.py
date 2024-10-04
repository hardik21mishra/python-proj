from tkinter import *
import random
import os
import sys
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#0A7CFF")
        self.root.title("Restaurant Billing System - by hardik")
        title=Label(self.root,text="Restaurant Billing System",bd=12,relief=RIDGE,font=("Arial Black",20),bg="#A569BD",fg="white").pack(fill=X)
        
        #===================================variables=======================================================================================
        self.nutella=IntVar()
        self.noodles=IntVar()
        self.lays=IntVar()
        self.oreo=IntVar()
        self.muffin=IntVar()
        self.silk=IntVar()
        self.namkeen=IntVar()
        self.atta=IntVar()
        self.pasta=IntVar()
        self.rice=IntVar()
        self.oil=IntVar()
        self.sugar=IntVar()
        self.dal=IntVar()
        self.tea=IntVar()
        self.soap=IntVar()
        self.shampoo=IntVar()
        self.lotion=IntVar()
        self.cream=IntVar()
        self.foam=IntVar()
        self.mask=IntVar()
        self.sanitizer=IntVar()
        self.total_sna=StringVar()
        self.total_gro=StringVar()
        self.total_hyg=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()
       
        #==========================================customer details label frame=================================================
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="#A569BD",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)
        cust_name=Label(details,text="Name",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=0,padx=15)

        cust_entry=Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)

        contact_name=Label(details,text="Contact No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=2,padx=10)

        contact_entry=Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)

        bill_name=Label(details,text="Bill.No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=4,padx=10)

        bill_entry=Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)
        #=======================================Resturant Menu=================================================================
        snacks=LabelFrame(self.root,text="Starter",font=("Arial Black",12),bg="#E5B4F3",fg="#6C3483",relief=GROOVE,bd=10)
        snacks.place(x=5,y=180,height=380,width=325)

        item1=Label(snacks,text="Samosa",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.nutella).grid(row=0,column=1,padx=10)

        item2=Label(snacks,text="Paneer Tikka",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.noodles).grid(row=1,column=1,padx=10)

        item3=Label(snacks,text="Chicken Tikka",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.lays).grid(row=2,column=1,padx=10)

        item4=Label(snacks,text="Vegetable Pakora",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.oreo).grid(row=3,column=1,padx=10)

        item5=Label(snacks,text="Papdi Chaat",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.muffin).grid(row=4,column=1,padx=10)

        item6=Label(snacks,text="Tomato Soup",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item6_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.silk).grid(row=5,column=1,padx=10)

        item7=Label(snacks,text="Masala Papad",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item7_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.namkeen).grid(row=6,column=1,padx=10)
        #=================================== Main Course =====================================================================================
        grocery=LabelFrame(self.root,text="Main Course",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        grocery.place(x=340,y=180,height=380,width=325)

        item8=Label(grocery,text="Butter Chicken",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item8_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.atta).grid(row=0,column=1,padx=10)

        item9=Label(grocery,text="Pasta",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item9_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.pasta).grid(row=1,column=1,padx=10)

        item10=Label(grocery,text="Basmathi Rice",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item10_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.rice).grid(row=2,column=1,padx=10)

        item11=Label(grocery,text="Paneer Masala",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item11_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.oil).grid(row=3,column=1,padx=10)

        item12=Label(grocery,text="Palak Paneer",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item12_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.sugar).grid(row=4,column=1,padx=10)

        item13=Label(grocery,text="Daal",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item13_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.dal).grid(row=5,column=1,padx=10)

        item14=Label(grocery,text="Chole Bhuture",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item14_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.tea).grid(row=6,column=1,padx=10)
        #========================================Snacks===============================================================================
        hygine=LabelFrame(self.root,text="Snacks",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        hygine.place(x=677,y=180,height=380,width=325)

        item15=Label(hygine,text="Noodles",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item15_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.soap).grid(row=0,column=1,padx=10)

        item16=Label(hygine,text="Aloo Tikki Chaat",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item16_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.shampoo).grid(row=1,column=1,padx=10)

        item17=Label(hygine,text="Dahi Vada",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item17_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.lotion).grid(row=2,column=1,padx=10)

        item18=Label(hygine,text="Pav Bhaji",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item18_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.cream).grid(row=3,column=1,padx=10)

        item19=Label(hygine,text="Bhel Puri",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item19_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.foam).grid(row=4,column=1,padx=10)

        item20=Label(hygine,text="Soup",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item20_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.mask).grid(row=5,column=1,padx=10)

        item21=Label(hygine,text="Pokara",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item21_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.sanitizer).grid(row=6,column=1,padx=10)
        
        
        #=====================================================billarea==============================================================================
        
        billarea=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        billarea.place(x=1010,y=188,width=330,height=372)

        bill_title=Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)

        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        
        #=================================================billing menu=========================================================================================
       
        billing_menu=LabelFrame(self.root,text="Billing Summery",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#A569BD",fg="white")
        billing_menu.place(x=0,y=560,relwidth=1,height=137)

        total_snacks=Label(billing_menu,text="Total Snacks Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=0)
        total_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_sna).grid(row=0,column=1,padx=10,pady=7)

        total_grocery=Label(billing_menu,text="Total Grocery Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=0)
        total_grocery_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_gro).grid(row=1,column=1,padx=10,pady=7)


        total_hygine=Label(billing_menu,text="Total Beauty & Hygine Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=0)
        total_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_hyg).grid(row=2,column=1,padx=10,pady=7)

        tax_snacks=Label(billing_menu,text="Snacks Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=2)
        tax_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.a).grid(row=0,column=3,padx=10,pady=7)

        tax_grocery=Label(billing_menu,text="Grocery Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=2)
        tax_grocery_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.b).grid(row=1,column=3,padx=10,pady=7)


        tax_hygine=Label(billing_menu,text="Beauty & Hygine Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=2)
        tax_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.c).grid(row=2,column=3,padx=10,pady=7)

        button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="#6C3483")
        button_frame.place(x=830,width=500,height=95)

        button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:total(self)).grid(row=0,column=0,padx=12)
        button_clear=Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:clear(self)).grid(row=0,column=1,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",width=8,command=lambda:exit1(self)).grid(row=0,column=2,padx=10,pady=6)
        intro(self)


def total(self):
    if (self.c_name.get=="" or self.phone.get()==""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.nu=self.nutella.get()*120
    self.no=self.noodles.get()*40
    self.la=self.lays.get()*10
    self.ore=self.oreo.get()*20
    self.mu=self.muffin.get()*30
    self.si=self.silk.get()*60
    self.na=self.namkeen.get()*15
    total_snacks_price=(
                self.nu+
                self.no+
                self.la+
                self.ore+
                self.mu+
                self.si+
                self.na)
    self.total_sna.set(str(total_snacks_price)+" Rs")
    self.a.set(str(round(total_snacks_price*0.05,3))+" Rs")

    self.at=self.atta.get()*42
    self.pa=self.pasta.get()*120
    self.oi=self.oil.get()*113
    self.ri=self.rice.get()*160
    self.su=self.sugar.get()*55
    self.te=self.tea.get()*480
    self.da=self.dal.get()*76
    total_grocery_price=(
        self.at+
        self.pa+
        self.oi+
        self.ri+
        self.su+
        self.te+
        self.da)

    self.total_gro.set(str(total_grocery_price)+" Rs")
    self.b.set(str(round(total_grocery_price*0.01,3))+" Rs")

    self.so=self.soap.get()*30
    self.sh=self.shampoo.get()*180
    self.cr=self.cream.get()*130
    self.lo=self.lotion.get()*500
    self.fo=self.foam.get()*85
    self.ma=self.mask.get()*100
    self.sa=self.sanitizer.get()*20

    total_hygine_price=(
        self.so+
        self.sh+
        self.cr+
        self.lo+
        self.fo+
        self.ma+
        self.sa)

    self.total_hyg.set(str(total_hygine_price)+" Rs")
    self.c.set(str(round(total_hygine_price*0.10,3))+" Rs")
    self.total_all_bill=(total_snacks_price+
                total_grocery_price+
                total_hygine_price+
                (round(total_grocery_price*0.01,3))+
                (round(total_hygine_price*0.10,3))+
                (round(total_snacks_price*0.05,3)))
    self.total_all_bil=str(self.total_all_bill)+" Rs"
    billarea(self)
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO SUPER MARKET\n\tPhone-No.739275410")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")
def billarea(self):
    intro(self)
    if self.nutella.get()!=0:
        self.txtarea.insert(END,f"Nutella\t\t {self.nutella.get()}\t{self.nu}\n")
    if self.noodles.get()!=0:
        self.txtarea.insert(END,f"Noodles\t\t {self.noodles.get()}\t{self.no}\n")
    if self.lays.get()!=0:
        self.txtarea.insert(END,f"Lays\t\t {self.lays.get()}\t{self.la}\n")
    if self.oreo.get()!=0:
        self.txtarea.insert(END,f"Oreo\t\t {self.oreo.get()}\t{self.ore}\n")
    if self.muffin.get()!=0:
        self.txtarea.insert(END,f"Muffins\t\t {self.muffin.get()}\t{self.mu}\n")
    if self.silk.get()!=0:
        self.txtarea.insert(END,f"Silk\t\t {self.silk.get()}\t{self.si}\n")
    if self.namkeen.get()!=0:
        self.txtarea.insert(END,f"Namkeen\t\t {self.namkeen.get()}\t{self.na}\n")
    if self.atta.get()!=0:
        self.txtarea.insert(END,f"Atta\t\t {self.atta.get()}\t{self.at}\n")
    if self.pasta.get()!=0:
        self.txtarea.insert(END,f"Pasta\t\t {self.pasta.get()}\t{self.pa}\n")
    if self.rice.get()!=0:
        self.txtarea.insert(END,f"Rice\t\t {self.rice.get()}\t{self.ri}\n")
    if self.oil.get()!=0:
        self.txtarea.insert(END,f"Oil\t\t {self.oil.get()}\t{self.oi}\n")
    if self.sugar.get()!=0:
        self.txtarea.insert(END,f"Sugar\t\t {self.sugar.get()}\t{self.su}\n")
    if self.dal.get()!=0:
        self.txtarea.insert(END,f"Daal\t\t {self.dal.get()}\t{self.da}\n")
    if self.tea.get()!=0:
        self.txtarea.insert(END,f"Tea\t\t {self.tea.get()}\t{self.te}\n")
    if self.soap.get()!=0:
        self.txtarea.insert(END,f"Soap\t\t {self.soap.get()}\t{self.so}\n")
    if self.shampoo.get()!=0:
        self.txtarea.insert(END,f"Shampoo\t\t {self.shampoo.get()}\t{self.sh}\n")
    if self.lotion.get()!=0:
        self.txtarea.insert(END,f"Lotion\t\t {self.lotion.get()}\t{self.lo}\n")
    if self.cream.get()!=0:
        self.txtarea.insert(END,f"Cream\t\t {self.cream.get()}\t{self.cr}\n")
    if self.foam.get()!=0:
        self.txtarea.insert(END,f"Foam\t\t {self.foam.get()}\t{self.fo}\n")
    if self.mask.get()!=0:
        self.txtarea.insert(END,f"Mask\t\t {self.mask.get()}\t{self.ma}\n")
    if self.sanitizer.get()!=0:
        self.txtarea.insert(END,f"Sanitizer\t\t {self.sanitizer.get()}\t{self.sa}\n")

    self.txtarea.insert(END,f"------------------------------------\n")
    if self.a.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Snacks Tax : {self.a.get()}\n")
    if self.b.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Grocery Tax : {self.b.get()}\n")
    if self.c.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Beauty&Hygine Tax : {self.c.get()}\n")
    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")
def clear(self):
        self.txtarea.delete(1.0,END)
        self.nutella.set(0)
        self.noodles.set(0)
        self.lays.set(0)
        self.oreo.set(0)
        self.muffin.set(0)
        self.silk.set(0)
        self.namkeen.set(0)
        self.atta.set(0)
        self.pasta.set(0)
        self.rice.set(0)
        self.oil.set(0)
        self.sugar.set(0)
        self.dal.set(0)
        self.tea.set(0)
        self.soap.set(0)
        self.shampoo.set(0)
        self.lotion.set(0)
        self.cream.set(0)
        self.foam.set(0)
        self.mask.set(0)
        self.sanitizer.set(0)
        self.total_sna.set(0)
        self.total_gro.set(0)
        self.total_hyg.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
def exit1(self):
    self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()
