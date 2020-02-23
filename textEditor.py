import tkinter as tk

class Text(tk.Text):
    def destroy(self):
        global ending_text
        ending_text = self.get("1.0", "end-1c")
        super(Text, self).destroy()
