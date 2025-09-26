#genera un numero random entre 1 y 20 y lo muestra en una ventana de tkinter

import tkinter as tk
import random

root = tk.Tk()
root.title("My Application")
root.geometry("576x640")
root.resizable(True, True)
root.configure(bg="lightblue")

total = 0

def incremento()->int:
    global total
    total =random.randint(1, 20)
    print(f"numero nuevo: {total}")
    return total


label = tk.Label(root, text="numero random! es:", bg="lightblue", font=("Arial", 16))
label.pack(pady=20)
button = tk.Button(root, text="Click Me", bg='Blue', font=("Arial", 14))
button.pack(pady=10)

def on_button_click():
    label.config(text=f"numero random! es: {incremento()}")
button.config(command=on_button_click)


root.mainloop()