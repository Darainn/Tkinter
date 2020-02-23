import tkinter as tk
import appOptions as opt
import message as msg

class myApplication():

    def __init__(self, master):
        self.master = master

        pageLabel = tk.Label(self.master, text = "MAIN MENU", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        pageLabel.place(x = 400, y = 0)

        loginBtn = tk.Button(self.master, text = "LOGIN", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.login(self.master))
        loginBtn.place(x = 500, y = 200)

        instructBtn = tk.Button(self.master, text = "INSTRUCTIONS", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.instruct(self.master))
        instructBtn.place(x = 500, y = 300)

        exitBtn = tk.Button(self.master, text = "EXIT", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(self.master))
        exitBtn.place(x = 500, y = 400)

    def instruct(self, root):

        instructPage = tk.Toplevel(root)
        instructPage.title("Instructions")
        instructPage.configure(bg = "black")
        instructPage.wm_state("zoomed")

        instructLabel = tk.Label(instructPage, text = "INSTRUCTIONS", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        instructLabel.place(x = 400, y = 0)

        instructions = tk.Label(instructPage, bg = 'black', fg='yellow', font='Times 14 italic', text=
        """ This is the instructions section. This application acts as a reliable and quick
            source of file transmission between students and teachers. Through this app,
            teachers can easily send assignments and/or any other kind of file, e.g. tutorial
            video or notes to the desired student. Moreover, the students can also send
            their completed assignments to their respective teachers. Both the students and
            teachers can access their accounts using the id Number/ roll Number assigned
            to them by the Management Staff. Their is also a section for viewing the
            recieved files by a person, telling which file was sent to him/her and by whom.
            Another feature of this Application is that it allows Students to view topics
            updated by different teachers on their subjects. Thus, in short this Application
            provides easy file transmission and management for students and teachers and also
            provides a source of reviewing various topics of various subjects as per updated
            by the subject teachers.....................................................""" ,borderwidth=10, relief=tk.RAISED)
        instructions.place(x = 200, y = 100, width= 750)
        
        backBtn = tk.Button(instructPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(instructPage))
        backBtn.place(x = 500, y = 500)
    
    def login(self, root):

        loginPage = tk.Toplevel(root)
        loginPage.title("Login Panel")
        loginPage.configure(bg = "black")
        loginPage.wm_state("zoomed")

        loginLabel = tk.Label(loginPage, text = "LOGIN PANEL", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        loginLabel.place(x = 400, y = 0)

        signinBtn = tk.Button(loginPage, text = "SIGNIN", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.signin(self.master))
        signinBtn.place(x = 500, y = 200)
        
        backBtn = tk.Button(loginPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(loginPage))
        backBtn.place(x = 500, y = 300)
        
    def signin(self, root):

        signinPage = tk.Toplevel(root)
        signinPage.title("SignIn Account")
        signinPage.configure(bg = "black")
        signinPage.wm_state("zoomed")

        signinLabel = tk.Label(signinPage, text = "SIGNIN ACCOUNT", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        signinLabel.place(x = 400, y = 0)

        idLabel = tk.Label(signinPage, text = "Enter your ID number: ", bg = "black", fg = "yellow", bd = 16, font = "Times 28 bold italic", relief = tk.RAISED)
        idLabel.place(x = 100, y = 100, width = 500)
        
        idEntry = tk.Entry(signinPage, bg = "black", fg = "yellow", font = "Times 28 italic")
        idEntry.place(x = 650, y = 100)

        usernameLabel = tk.Label(signinPage, text = "Enter your username: ", bg = "black", fg = "yellow", bd = 16, font = "Times 28 bold italic", relief = tk.RAISED)
        usernameLabel.place(x = 100, y = 200, width = 500)
        
        usernameEntry = tk.Entry(signinPage, bg = "black", fg = "yellow", font = "Times 28 italic")
        usernameEntry.place(x = 650, y = 200)

        passwordLabel = tk.Label(signinPage, text = "Enter your password: ", bg = "black", fg = "yellow", bd = 16, font = "Times 28 bold italic", relief = tk.RAISED)
        passwordLabel.place(x = 100, y = 300, width = 500)
        
        passwordEntry = tk.Entry(signinPage, show = "*",  bg = "black", fg = "yellow", font = "Times 28 italic")
        passwordEntry.place(x = 650, y = 300)

        studentBtn = tk.Button(signinPage, text = "STUDENT", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.checkFile('studentUsers.txt', usernameEntry.get(), passwordEntry.get(), idEntry.get()))
        studentBtn.place(x = 500, y = 400)

        teacherBtn = tk.Button(signinPage, text = "TEACHER", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.checkFile('teacherUsers.txt', usernameEntry.get(), passwordEntry.get(), idEntry.get()))
        teacherBtn.place(x = 500, y = 500)
        
        backBtn = tk.Button(signinPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(signinPage))
        backBtn.place(x = 500, y = 600)

    def checkFile(self, filename, user, passw, idNum):
        with open(filename) as f:
            f1 = f.read().split('\n')
            if str(user + ',' + idNum) in f1:
                f = open('pass' + filename)
                f2 = f.read().split('\n')
                if str(passw + ',' + idNum) in f2:
                    if filename == 'studentUsers.txt':
                        optPage = opt.StudentOptions(self.master, idNum)
                    elif filename == 'teacherUsers.txt':
                        optPage = opt.TeacherOptions(self.master, idNum)
                else:
                    mes = msg.Message(self.master, "Invalid Password Entered")
            else:
                mes = msg.Message(self.master, "Invalid Username or ID Entered")
    
    def delete(self, root):
         root.destroy()
        




    
