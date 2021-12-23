from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"

# Todo: GUI Interface
windows = Tk()
windows.title("Card Flash Project")
windows.config(bg=BACKGROUND_COLOR, padx=10, pady=10)

# Canvas
front_car_img = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(410, 275, image=front_car_img)
canvas.grid(column=0, row=0, columnspan=2)

# Button
x_img = PhotoImage(file="images/wrong.png")
btn_x = Button(image=x_img, highlightthickness=0)
btn_x.grid(column=0, row=1)

y_img = PhotoImage(file="images/right.png")
btn_y = Button(image=y_img, highlightthickness=0)
btn_y.grid(column=1, row=1)

windows.mainloop()
