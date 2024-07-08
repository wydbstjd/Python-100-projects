from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#Label
label_1 = Label(text="is equal to")
label_1.grid(column=0, row=1)

label_2 = Label(text="Miles")
label_2.grid(column=2, row=0)

label_3 = Label(text="Km")
label_3.grid(column=2, row=1)

num = Label(text="0")
num.grid(column=1, row=1)

#Button
def miles_to_km():
    miles = input.get()
    km = round(float(miles) * 1.609)
    num.config(text= f"{km}")

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

#Entry
input = Entry(width=7)
input.grid(column=1, row=0)


window.mainloop() # 이 줄은 프로그램의 맨 마지막에 위치