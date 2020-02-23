import tkinter as tk

class Message():

    def center(self, root):
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def __init__(self, master, text):
        self.master = master
        self.text = text
        
        message = tk.Toplevel(self.master)
        message.title('Message')
        self.center(message)
        message.configure(bg = 'black')
        messageLabel = tk.Label(message, bg='black', fg='yellow', text=self.text , font='Times 10 italic')
        messageLabel.place(x = 0, y = 40, width = 200)
        okBtn = tk.Button(message, bg='black', fg='yellow', text='OK', borderwidth=4, relief=tk.RAISED, command= lambda: self.delete(message))
        okBtn.place(x = 50, y = 100, width = 50)

    def delete(self, root):
        root.destroy()
