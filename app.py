import tkinter as tk
from tkinter import font
import protein as p

wn = tk.Tk()
wn.title("Protein data")
wn.resizable(0, 0)
app_w = 300
app_h = 400
screen_w= wn.winfo_screenwidth()
screen_h = wn.winfo_screenheight()

coord_x =(screen_w // 2) - (app_w // 2)
coord_y = (screen_h // 2) - (app_h // 2)

wn.geometry(f"{app_w}x{app_h}+{coord_x}+{coord_y}")

subtitle_roadrage = font.Font(family="Road Rage", size=17)
txt_roadrage = font.Font(family="Road Rage", size=13)

fs_lbl = tk.Label(wn, text="Ingrese su alimento ↧", font=subtitle_roadrage)
fs_lbl.place(relx=0.5, y=65, anchor="center")

pr_in = tk.Entry(wn, width=40, border=2, relief= tk.SOLID)
pr_in.place(relx=0.5, y=100, anchor="center")

ou = lambda: pr_lbl.config(text= f"{pr_in.get()} tiene \n{p.get_protein_amount(pr_in.get(), p.api_key)}g de proteina")

smt_btn = tk.Button(wn, text="Ingresar", activebackground='#345', font=txt_roadrage, border=3, relief= tk.SOLID, command= ou)
smt_btn.place(relx=0.5, y=140, anchor="center")

pr_lbl = tk.Label(wn, text="", font=txt_roadrage)
pr_lbl.place(relx=0.5, y=200, anchor="center")

exit_btn = tk.Button(wn, text="Salir", activebackground='#345', font=txt_roadrage, border=3, relief= tk.SOLID, command= lambda: wn.destroy())
exit_btn.place(relx=0.5, rely=0.9, anchor="center")

wn.mainloop()