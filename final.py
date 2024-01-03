from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
root =tb.Window(themename="cyborg")
root.geometry("1920x1080")
label1=tb.Label(text="Please Select Your Required Subject:",font= ("Helvetica",28),bootstyle="info")
label1.pack(pady=50)
def two():
     def scalevalue(e):
          noclabel.config(text=f'{int(noc.get())}')
          global a
          a=int(noc.get())
     
     def display2():
         needed=25-a
         
         percent=(a/30)*100
         print(percent)
         if a>=25:
             
             win3=tb.Toplevel()
             win3.title("window3")
             win3.geometry("1920x1080")
             label3= tb.Label(win3,text="This subject has 30 classes in total ",font= ("Helvetica",28),bootstyle="info")
             label3.pack(pady=10)
             label4= tb.Label(win3,text="you currently have:",font= ("Helvetica",28),bootstyle="info")
             label4.pack(pady=10)
             attendpercent=tb.Progressbar(win3,bootstyle="danger",maximum=100,mode="determinate",length=300,value=percent)
             attendpercent.pack(pady=20)
             label5=tb.Label(win3,text=str(int(percent))+"%",bootstyle="info",font=("Helvetica,12"))
             label5.pack(pady=10)
             label6= tb.Label(win3,text="You Already Have Attenandce Above 85% Happy Bunking!!! ",font= ("Helvetica",28),bootstyle="info")  
             label6.pack(pady=10)          
         else:
             win3=tb.Toplevel()
             win3.geometry("1920x1080")
             win3.title("window3")
             label3= tb.Label(win3,text="This subject has 30 classes in total ",font= ("Helvetica",28),bootstyle="info")
             label3.pack(pady=10)
             label4= tb.Label(win3,text="you currently have:",font= ("Helvetica",28),bootstyle="info")
             label4.pack(pady=10)
             attendpercent=tb.Progressbar(win3,bootstyle="danger",maximum=100,mode="determinate",length=300,value=percent)
             attendpercent.pack(pady=20)
             label5=tb.Label(win3,text=str(int(percent))+"%",bootstyle="info",font=("Helvetica,12"))
             label5.pack(pady=10)
             label6= tb.Label(win3,text="Your Attenandce Is Below 85% ",font= ("Helvetica",28),bootstyle="info")  
             label6.pack(pady=10)
             label7= tb.Label(win3,text="You Need These Many Classes To Make Up For 85%:"+str(needed),font= ("Helvetica",28),bootstyle="info")  
             label7.pack(pady=10)
     
     
         
     win2=tb.Toplevel()
     win2.title("window2")
     win2.geometry("1920x1080")
     label2=tb.Label(win2,text="Enter the number of classes you have attended:",font= ("Helvetica",28),bootstyle="info")
     label2.pack(pady=10)
     noc=tb.Scale(win2,bootstyle="warning",length=300,from_=0,to=30,command=scalevalue)
     noc.pack(pady=25)
     noclabel=tb.Label(win2,text="",font=("Helvetica,12"))
     noclabel.pack(pady=10)
     enterybutton=tb.Button(win2,text="Submit",bootstyle="success,outline",command=display2)
     enterybutton.pack(pady=10)
     
def four():
     def scalevalue(e):
          noclabel.config(text=f'{int(noc.get())}')
          global a
          a=int(noc.get())
     
     def display2():
         needed=56-a
         
         percent=(a/66)*100
         print(percent)
         if a>=56:
             
             win3=tb.Toplevel()
             win3.title("window3")
             win3.geometry("1920x1080")
             label3= tb.Label(win3,text="This subject has 66 classes in total ",font= ("Helvetica",28),bootstyle="info")
             label3.pack(pady=10)
             label4= tb.Label(win3,text="you currently have:",font= ("Helvetica",28),bootstyle="info")
             label4.pack(pady=10)
             attendpercent=tb.Progressbar(win3,bootstyle="danger",maximum=100,mode="determinate",length=300,value=percent)
             attendpercent.pack(pady=20)
             label5=tb.Label(win3,text=str(int(percent))+"%",bootstyle="info",font=("Helvetica,12"))
             label5.pack(pady=10)
             label6= tb.Label(win3,text="You Already Have Attenandce Above 85% Happy Bunking!!! ",font= ("Helvetica",28),bootstyle="info")  
             label6.pack(pady=10)          
         else:
             win3=tb.Toplevel()
             win3.title("window3")
             win3.geometry("1920x1080")
             label3= tb.Label(win3,text="This subject has 66 classes in total ",font= ("Helvetica",28),bootstyle="info")
             label3.pack(pady=10)
             label4= tb.Label(win3,text="you currently have:",font= ("Helvetica",28),bootstyle="info")
             label4.pack(pady=10)
             attendpercent=tb.Progressbar(win3,bootstyle="danger",maximum=100,mode="determinate",length=300,value=percent)
             attendpercent.pack(pady=20)
             label5=tb.Label(win3,text=str(int(percent))+"%",bootstyle="info",font=("Helvetica,12"))
             label5.pack(pady=10)
             label6= tb.Label(win3,text="Your Attenandce Is Below 85% ",font= ("Helvetica",28),bootstyle="info")  
             label6.pack(pady=10)
             label7= tb.Label(win3,text="You Need These Many Classes To Make Up For 85%:"+str(needed),font= ("Helvetica",28),bootstyle="info")  
             label7.pack(pady=10)
     
     
         
     win2=tb.Toplevel()
     win2.title("window2")
     win2.geometry("1920x1080")
     label2=tb.Label(win2,text="Enter the number of classes you have attended:",font= ("Helvetica",28),bootstyle="info")
     label2.pack(pady=10)
     noc=tb.Scale(win2,bootstyle="warning",length=300,from_=0,to=66,command=scalevalue)
     noc.pack(pady=25)
     noclabel=tb.Label(win2,text="",font=("Helvetica,12"))
     noclabel.pack(pady=10)
     enterybutton=tb.Button(win2,text="Submit",bootstyle="success,outline",command=display2)
     enterybutton.pack(pady=10)     
def one():
     def scalevalue(e):
          noclabel.config(text=f'{int(noc.get())}')
          global a
          a=int(noc.get())
     
     def display2():
         needed=12-a
         
         percent=(a/15)*100
         print(percent)
         if a>=12:
             
             win3=tb.Toplevel()
             win3.title("window3")
             win3.geometry("1920x1080")
             label3= tb.Label(win3,text="This subject has 3015 classes in total ",font= ("Helvetica",28),bootstyle="info")
             label3.pack(pady=10)
             label4= tb.Label(win3,text="you currently have:",font= ("Helvetica",28),bootstyle="info")
             label4.pack(pady=10)
             attendpercent=tb.Progressbar(win3,bootstyle="danger",maximum=100,mode="determinate",length=300,value=percent)
             attendpercent.pack(pady=20)
             label5=tb.Label(win3,text=str(int(percent))+"%",bootstyle="info",font=("Helvetica,12"))
             label5.pack(pady=10)
             label6= tb.Label(win3,text="You Already Have Attenandce Above 85% Happy Bunking!!! ",font= ("Helvetica",28),bootstyle="info")  
             label6.pack(pady=10)          
         else:
             win3=tb.Toplevel()
             win3.title("window3")
             win3.geometry("1920x1080")
             label3= tb.Label(win3,text="This subject has 15 classes in total ",font= ("Helvetica",28),bootstyle="info")
             label3.pack(pady=10)
             label4= tb.Label(win3,text="you currently have:",font= ("Helvetica",28),bootstyle="info")
             label4.pack(pady=10)
             attendpercent=tb.Progressbar(win3,bootstyle="danger",maximum=100,mode="determinate",length=300,value=percent)
             attendpercent.pack(pady=20)
             label5=tb.Label(win3,text=str(int(percent))+"%",bootstyle="info",font=("Helvetica,12"))
             label5.pack(pady=10)
             label6= tb.Label(win3,text="Your Attenandce Is Below 85% ",font= ("Helvetica",28),bootstyle="info")  
             label6.pack(pady=10)
             label7= tb.Label(win3,text="You Need These Many Classes To Make Up For 85%:"+str(needed),font= ("Helvetica",28),bootstyle="info")  
             label7.pack(pady=10)
     
     
         
     win2=tb.Toplevel()
     win2.title("window2")
     win2.geometry("1920x1080")
     label2=tb.Label(win2,text="Enter the number of classes you have attended:",font= ("Helvetica",28),bootstyle="info")
     label2.pack(pady=10)
     noc=tb.Scale(win2,bootstyle="warning",length=300,from_=0,to=15,command=scalevalue)
     noc.pack(pady=25)
     noclabel=tb.Label(win2,text="",font=("Helvetica,12"))
     noclabel.pack(pady=10)
     enterybutton=tb.Button(win2,text="Submit",bootstyle="success,outline",command=display2)
     enterybutton.pack(pady=10)
    
eng= tb.Button(text="English",bootstyle="primary,outline",command=two)
math= tb.Button(text="Mathematics",bootstyle="primary,outline",command=four)
chem= tb.Button(text="Chemistry",bootstyle="primary,outline",command=four)
ico= tb.Button(text="Indian Constitution",bootstyle="primary,outline",command=one)
sfh= tb.Button(text="SFH",bootstyle="primary,outline",command=one)
mech= tb.Button(text="Mechanical",bootstyle="primary,outline",command=two)
python= tb.Button(text="Python",bootstyle="primary,outline",command=four)
caed= tb.Button(text="CAED",bootstyle="primary,outline",command=two)
eng.pack(pady=10)
math.pack(pady=10)
chem.pack(pady=10)
ico.pack(pady=10)
sfh.pack(pady=10)
mech.pack(pady=10)
python.pack(pady=10)
caed.pack(pady=10)

root.title("new")
root.mainloop()