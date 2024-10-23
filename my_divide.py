from tkinter import *
from tkinter import ttk

class DivideApp:
    def __init__(self, root):
        self.root = root
        root.geometry("250x200")
        self.root.resizable(False, False)
        self.root.title("Divide App")
        
        self.start_spinbox = ttk.Spinbox(root, from_=0, to=100, increment=1)
        self.end_spinbox = ttk.Spinbox(root, from_=0, to=100, increment=1)
        self.divide_label = Label(root, text="")
        self.calc_button = Button(root, text="Вычислить чему равно деление чисел.", 
                                  command=self.calculate_divide)
        
        self.start_spinbox.pack(pady=10)
        self.end_spinbox.pack(pady=10)
        self.divide_label.pack(pady=10)
        self.calc_button.pack(pady=10)
    
    def calculate_divide(self):
        start = float(self.start_spinbox.get())
        end = float(self.end_spinbox.get())
        divide_ = round(start / end, 2)
        self.divide_label.configure(text=f"Ответ: {divide_}")
                
root = Tk()
app = DivideApp(root)
root.mainloop()