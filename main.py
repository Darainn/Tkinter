import tkinter as tk
import myApplication as myApp

def main():
    main = tk.Tk()
    main.title("My Application")
    main.configure(bg = "black")
    main.wm_state("zoomed")
    run = myApp.myApplication(main)
    main.mainloop()

if __name__ == "__main__":
    main()

    
