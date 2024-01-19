from tkinter import *
window=Tk()


def calculate_int():
  p=float(principal.get())
  r=float(rate.get())
  t=float(time.get())
  i=(r*p*t)/100
  interest=round(i,2)
  
  
  result_label.destroy()
  msg='Your interest in'+t+'will be'+interest
  
  output_msg=Label(result_frame,+"Intrest is"+str(interest), bg = "lightcyan", font=("Calibri", 12), width=42)
  output_msg.place(x=20,y=40)
  output_msg.pack()

window.title('Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightblue')


app_label=Label(window, text="INTEREST CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

time_label=Label(window, text="Time in bank", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
time_label.place(x=20, y=90)

time=Entry(window, text="", bd=2, width=22)
time.place(x=150, y=92)

principal_label=Label(window, text="principal", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
principal_label.place(x=20, y=130)

principal=Entry(window, text="", bd=2, width=22)
principal.place(x=150, y=132)

rate_label=Label(window, text="Your rate", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
rate_label.place(x=20, y=170)

rate=Entry(window, text="", bd=2, width=22)
rate.place(x=150, y=172)


calc=Button(window, text="CALCULATE", fg='black' ,bg="cyan",bd=4, command=calculate_int)
calc.place(x=150, y=202)








result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()
window.mainloop()
