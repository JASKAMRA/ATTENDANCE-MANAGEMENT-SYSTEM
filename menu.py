# !/usr/bin/python3  
      
bg_color="lavender"
fg_color="black"
   
import csv
import datetime
from tkinter import *
from datetime import date
from datetime import timedelta

def add_student():

   def submit_info():
       myFile = open("Student.csv","a",newline='')
       writer=csv.writer(myFile)
       writer.writerow([roll.get(), sname.get(), fname.get(), address.get()])
       myFile.close()

   def gencode():
       with open("Student.csv","r") as myFile:
          stureader = csv.reader(myFile)
          maxno=0
          for rec in stureader:
             if rec[0]=="Roll No":
                continue
             roll=int(rec[0])
             if(maxno < roll):
                maxno = roll
       myFile.close()
       maxno = maxno + 1
       return maxno
   


   global root
   a.title("Student Entry Form- St Cecilia School...")
   root.destroy()
   root=Frame(a)
   root.configure(bg=bg_color)
   rollno = int(gencode())

   Label(root, text="Add Student Form",width=20,font=("bold", 20)).place(x=150,y=53) 
   
   Label(root, text="Roll No.",width=20,font=("bold", 12)).place(x=180,y=240)

   roll = Entry(root)
   roll.insert(0,rollno)
   roll.place(x=440,y=240)  
   roll.config(state="disabled")
      
   Label(root, text="Student Name",width=20,font=("bold", 12)).place(x=180,y=280)  
   
   sname = Entry(root)  
   sname.place(x=440,y=280)  
      
   Label(root, text="Father's Name",width=20,font=("bold", 12)).place(x=180,y=320)  
   
   fname = Entry(root)  
   fname.place(x=440,y=320)  
     
   Label(root, text="Address",width=20,font=("bold", 12)).place(x=180,y=360)  
   
   address = Entry(root)  
   address.place(x=440,y=360)  
      
     
   submit = Button(root,text="Submit", width = "10", height = "2",bg='yellow',fg=fg_color, command = submit_info)
   submit.place(x=460, y=460)

   root.pack(side="top", expand=True, fill="both")
   
def display_student():
    global root
    root.destroy()
    root=Frame(a)
    root.configure(bg=bg_color)
    with open("Student.csv", mode ='r') as file:
       csvFile = csv.DictReader(file)
       x=1
       lbl = Label(root, text="Roll No ",width=20,font=("bold", 12), bg=bg_color)  
       lbl.place(x=10,y=50)  
       lbl = Label(root, text="Student Name ",width=20,font=("bold", 12), bg=bg_color)  
       lbl.place(x=200,y=50)  
       lbl = Label(root, text="Father's Name ",width=20,font=("bold", 12), bg=bg_color)  
       lbl.place(x=400,y=50)  
       lbl = Label(root, text="Address ",width=20,font=("bold", 12), bg=bg_color)  
       lbl.place(x=600,y=50)  
       z=100
       for lines in csvFile:
          lbl = Label(root, text=lines["Roll No"],width=20,font=("bold", 12), bg=bg_color)  
          lbl.place(x=10,y=z)  
          lbl = Label(root, text=lines["Student Name"],width=20,font=("bold", 12), bg=bg_color)  
          lbl.place(x=200,y=z)  
          lbl = Label(root, text=lines["Fathers Name"],width=20,font=("bold", 12), bg=bg_color)  
          lbl.place(x=400,y=z)  
          lbl = Label(root, text=lines["Address"],width=20,font=("bold", 12), bg=bg_color)  
          lbl.place(x=600,y=z)
          z=z+22
          
    a.geometry("1000x600")
    a.title("Student Details- St Cecilia School...")
    submit = Button(root,text="Clear", width = "10", height = "2",bg='yellow',fg=fg_color, command = clear_window)
    submit.place(x=460, y=z+50)
    root.pack(side="top", expand=True, fill="both")
    file.close()


def report_attendance(i):
    global root
    dat=date.today()
    if i==-1:
        dat = dat - timedelta(days = 1)
    dat=str(dat)
    tot_stu=0
    pre_stu=0
    col="red"
    root.destroy()
    root=Frame(a)
    root.configure(bg=bg_color)
    msg="Date: "+dat
    lbl = Label(root, text=msg,font=("bold", 12), bg=bg_color)  
    lbl.place(x=10,y=10)  
                  
    with open("Attendance.csv", mode ='r') as file:
       csvFile = csv.DictReader(file)
       x=1
       lbl = Label(root, text="Roll No ",width=20,font=("bold", 12), bg=bg_color)  
       lbl.place(x=10,y=50)  
       lbl = Label(root, text="Student Name ",width=20,font=("bold", 12), bg=bg_color)  
       lbl.place(x=200,y=50)  
       lbl = Label(root, text="Present/ Absent ",width=20,font=("bold", 12), bg=bg_color)  
       lbl.place(x=400,y=50)  
       z=100
       for lines in csvFile:
            if lines["Date"]==dat:
                  tot_stu=tot_stu+1
                  lbl = Label(root, text=lines["Roll No"],width=20,font=("bold", 12), bg=bg_color)  
                  lbl.place(x=10,y=z)  
                  lbl = Label(root, text=lines["Student Name"],width=20,font=("bold", 12), bg=bg_color)  
                  lbl.place(x=200,y=z)
                  if lines["Present"]==str(1):
                      att="Present"
                      col="green"
                      pre_stu=pre_stu+1
                  else:
                      att="Absent"
                      col="red"
                  lbl = Label(root, text=att,width=20,font=("bold", 12), bg=bg_color, fg=col)  
                  lbl.place(x=400,y=z)
                  z=z+20
       per_stu=(pre_stu/tot_stu)*100
       msg='No of Student Present = '+ str(pre_stu)+ '/' + str(tot_stu)+'\n'+"Percentage Attendance = "+str(per_stu)+' %'
       if tot_stu==0:
            msg="No Record Available for the date",dat
       lbl = Label(root, text=msg,font=("bold", 12), bg=bg_color, fg=col)  
       lbl.place(x=50,y=z+20)
    a.geometry("1000x600")
    a.title("Attendance Report- St Cecilia School...")
    submit = Button(root,text="Clear", width = "10", height = "2",bg='yellow',fg=fg_color, command = clear_window)
    submit.place(x=460, y=460)
    root.pack(side="top", expand=True, fill="both")
    file.close()
    
def close_program():
   a.destroy()
   
def clear_window():
    global root
    a.title("Attendance System - St Cecilia's Public School")
    root.destroy()
    root=Frame(a)
    root.configure(bg=bg_color)
    Label(root, text="Attendance System - St Cecilia's Public School",font=("bold", 40), bg=bg_color, fg=fg_color).place(x=150,y=100)
    Label(root, text="By Jas Kamra, Roll No 9",font=("bold", 20), bg=bg_color, fg=fg_color).place(x=620,y=500)
    root.pack(side="top", expand=True, fill="both")


def attendance():

   def add_attendance():
       myFile = open("Attendance.csv","a",newline='')
       writer=csv.writer(myFile)
       for i in range(len(ch)):
         writer.writerow([i+1,get_name(i+1),date.today(),ch[i].get()])
         print(i+1, get_name(i+1),date.today(),ch[i].get())
       myFile.close()
         
   def get_name(i):
        with open("Student.csv", mode ='r') as file:
             csvFile = csv.DictReader(file)
             for lines in csvFile:
                if lines["Roll No"]==str(i):
                    return lines["Student Name"]
        return "NA"
        
   global root, ch
   a.title("Add Attendance- St Cecilia School...")
   root.destroy()
   root=Frame(a)
   root.configure(bg=bg_color)
   x=0
   with open("Student.csv", mode ='r') as file:
     csvFile = csv.DictReader(file)
     for lines in csvFile:
        ch[x]=IntVar()
        Checkbutton(root,text=lines["Roll No"]+" : "+lines["Student Name"],variable=ch[x], bg=bg_color,fg=fg_color,font=("bold", 12)).place(x=100,y=100+20*x)
        x=x+1
   Button(root,text="Mark Attendance",command=add_attendance, bg='yellow').place(x=100,y=140+20*x)
   Button(root,text="Cancel",command=clear_window, bg='yellow').place(x=250,y=140+20*x)
   root.pack(side="top", expand=True, fill="both")
   
ch={}
a = Tk()
root = Frame(a)
a.geometry("600x600")
a.title("Attendance System - St Cecilia's Public School")
a.state('zoomed')
root.configure(bg=bg_color)
a.configure(bg=bg_color)

Label(root, text="Attendance System - St Cecilia's Public School",font=("bold", 40), bg=bg_color, fg=fg_color).place(x=150,y=100)
Label(root, text="By Jas Kamra, Roll No 9",font=("bold", 20), bg=bg_color, fg=fg_color).place(x=620,y=500)

root.pack(side="top", expand=True, fill="both")


menubar = Menu(a)

menubar.add_command(label="Home", command=clear_window)

studmenu = Menu(menubar, tearoff=0)
studmenu.add_command(label="Add Student Details", command=add_student)
studmenu.add_separator()
studmenu.add_command(label="Display Student Details", command=display_student)
menubar.add_cascade(label="Student Menu", menu=studmenu)

attmenu = Menu(menubar, tearoff=0)
attmenu.add_command(label="Add Attendance", command=attendance)
attmenu.add_separator()
attmenu.add_command(label="Display Today's Attendance Report", command=lambda: report_attendance(1))
attmenu.add_command(label="Display Yesterday's Attendance Report", command=lambda: report_attendance(-1))
menubar.add_cascade(label="Attendance Menu", menu=attmenu)

menubar.add_command(label="Quit", command=close_program)




a.config(menu=menubar)
a.mainloop()
