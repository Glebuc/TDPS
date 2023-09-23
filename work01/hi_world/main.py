import tkinter as tk
import random

window = tk.Tk()
window.title("Генератор паролей")
window["bg"] = "white"
window.geometry("350x200")
window.resizable(False,False)

lbl = tk.Label(text="Создай пароль", bg="white", font=16, fg="purple")
lbl.pack()
lbl2 = tk.Label(text="Введите количество символов в пароле", bg="white", font=("Arial", 12), fg="purple")
lbl2.pack()
inp = tk.Entry(font=13)
inp.pack()
btn = tk.Button(text="Сгенерировать", font=("Arial", 12), bg="purple", fg="white")
btn.pack(pady=20)



window.mainloop()