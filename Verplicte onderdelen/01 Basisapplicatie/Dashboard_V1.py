import tkinter as tk

# ==================================================== ROOT CONFIG ====================================================

root = tk.Tk()
root.title("Dashboard Steam")
root.geometry("1500x900")
root.config(bg="white")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# ======================================================= FRAMES =======================================================

# TODO: Kies de info voor het dashboard
# TODO: Verander zo nodig de layout en rename de frames

temp_frame1 = tk.Frame(root, bg='#FF0000')
temp_frame2 = tk.Frame(root, bg='orange')
temp_frame3 = tk.Frame(root, bg='pink')
temp_frame4 = tk.Frame(root, bg='blue')
temp_frame5 = tk.Frame(root, bg='green')

temp_frame1.grid(column=0, row=0, sticky='news')
temp_frame2.grid(column=1, row=0, sticky='news')
temp_frame3.grid(column=2, row=0, rowspan=2, sticky='news')
temp_frame4.grid(column=0, row=1, sticky='news')
temp_frame5.grid(column=1, row=1, sticky='news')

# ====================================================== MAINLOOP ======================================================

root.mainloop()
