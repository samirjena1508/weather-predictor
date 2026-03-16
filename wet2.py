from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9d65229602e88a93a5321ffb98d97046"
    data = requests.get(url).json()

    wt_lebel1.config(text=data['weather'][0]["main"])
    wp_lebel1.config(text=data['weather'][0]["description"])
    temp_lebel1.config(text=round(data['main']["temp"] - 273.15, 2))
    pre_lebel1.config(text=data['main']["pressure"])


win = Tk()
win.title("Weather App")
win.config(bg="black")
win.geometry("500x580")

name_lebel = Label(
    win,
    text="Weather App",
    font=("time new roman", 20, "bold")
)
name_lebel.place(x=25, y=50, height=50, width=450)

city_name = StringVar()

list_name = [
    'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar',
    'Chhattisgarh', 'Delhi', 'Goa', 'Gujarat', 'Haryana',
    'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand',
    'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra',
    'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
    'Odisha', 'Punjab', 'Rajasthan', 'Sikkim',
    'Tamil Nadu', 'Tripura', 'Uttar Pradesh',
    'Uttarakhand', 'West Bengal'
]

com = ttk.Combobox(
    win,
    values=list_name,
    font=("time new roman", 15),
    textvariable=city_name
)
com.place(x=25, y=120, height=50, width=450)

wt_lebel = Label(win, text="Climate", font=("time new roman", 10))
wt_lebel.place(x=25, y=260, height=50, width=210)

wt_lebel1 = Label(win, text="", font=("time new roman", 10))
wt_lebel1.place(x=250, y=260, height=50, width=210)

wp_lebel = Label(win, text="Description", font=("time new roman", 10))
wp_lebel.place(x=25, y=330, height=50, width=210)

wp_lebel1 = Label(win, text="", font=("time new roman", 10))
wp_lebel1.place(x=250, y=330, height=50, width=210)

temp_lebel = Label(win, text="Temperature (°C)", font=("time new roman", 10))
temp_lebel.place(x=25, y=400, height=50, width=210)

temp_lebel1 = Label(win, text="", font=("time new roman", 10))
temp_lebel1.place(x=250, y=400, height=50, width=210)

pre_lebel = Label(win, text="Pressure", font=("time new roman", 10))
pre_lebel.place(x=25, y=470, height=50, width=210)

pre_lebel1 = Label(win, text="", font=("time new roman", 10))
pre_lebel1.place(x=250, y=470, height=50, width=210)

done_button = Button(
    win,
    text="Done",
    font=("time new roman", 20, "bold"),
    command=data_get
)
done_button.place(x=200, y=190, height=50, width=100)

win.mainloop()
