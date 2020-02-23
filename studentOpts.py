
class StudentOptions():

    def __init__(self, master, user):
        self.master = master
        self.user = user
        
        optPage = tk.Toplevel(self.master)
        optPage.title("App Options")
        optPage.configure(bg = "black")
        optPage.wm_state("zoomed")

        optLabel = tk.Label(optPage, text = "STUDENT MENU", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        optLabel.place(x = 400, y = 0)

        sendBtn = tk.Button(optPage, text = "SEND FILE", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.send(self.master))
        sendBtn.place(x = 500, y = 200)

        recieveBtn = tk.Button(optPage, text = "VIEW RECIEVED", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.recieve(self.master))
        recieveBtn.place(x = 500, y = 300)

        topicsBtn = tk.Button(optPage, text = "STUDY TOPICS", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topics(self.master))
        topicsBtn.place(x = 500, y = 400)
        
        exitBtn = tk.Button(optPage, text = "LOGOUT", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(optPage))
        exitBtn.place(x = 500, y = 500)

    def send(self, root):

        sendPage = tk.Toplevel(root)
        sendPage.title("Send Files")
        sendPage.configure(bg = "black")
        sendPage.wm_state("zoomed")

        sendLabel = tk.Label(sendPage, text = "SEND FILES", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        sendLabel.place(x = 400, y = 0)

        fileLabel = tk.Label(sendPage, text = "Enter the filenaem to send: ", bg = "black", fg = "yellow", bd = 16, font = "Times 28 bold italic", relief = tk.RAISED)
        fileLabel.place(x = 100, y = 200, width = 500)
        
        fileEntry = tk.Entry(sendPage, bg = "black", fg = "yellow", font = "Times 28 italic")
        fileEntry.place(x = 650, y = 200)

        recieverLabel = tk.Label(sendPage, text = "Enter the user to send to: ", bg = "black", fg = "yellow", bd = 16, font = "Times 28 bold italic", relief = tk.RAISED)
        recieverLabel.place(x = 100, y = 300, width = 500)
        
        recieverEntry = tk.Entry(sendPage, bg = "black", fg = "yellow", font = "Times 28 italic")
        recieverEntry.place(x = 650, y = 300)

        sendfileBtn = tk.Button(sendPage, text = "SEND", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.sendFile(str(fileEntry.get()),recieverEntry.get()))
        sendfileBtn.place(x = 500, y = 500)
        
        backBtn = tk.Button(sendPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(sendPage))
        backBtn.place(x = 500, y = 600)

    def recieve(self, root):

        recievePage = tk.Toplevel(root)
        recievePage.title("Recieved Files")
        recievePage.configure(bg = "black")
        recievePage.wm_state("zoomed")

        recieved = self.readfile('D:/Hassan Files/Python Programming/OOP Semester Project/studentUsers/' + str(self.user) + '/recieved.txt')

        recieveLabel = tk.Label(recievePage, text = "RECIEVED FILES", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        recieveLabel.place(x = 400, y = 0)

        reciever = tk.Label(recievePage, text = recieved, bg = "black", fg = "yellow", bd = 16, font = "Times 10 italic", relief = tk.RAISED)
        reciever.place(x = 200, y = 200, width = 500)

        backBtn = tk.Button(recievePage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(recievePage))
        backBtn.place(x = 500, y = 600)

    def topics(self, root):

        topicsPage = tk.Toplevel(root)
        topicsPage.title("Topics")
        topicsPage.configure(bg = "black")
        topicsPage.wm_state("zoomed")

        topicsLabel = tk.Label(topicsPage, text = "STUDY TOPICS", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        topicsLabel.place(x = 400, y = 0)

        OOPBtn = tk.Button(topicsPage, text = "OOP", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.OOP(self.master))
        OOPBtn.place(x = 500, y = 100)
        
        DAABtn = tk.Button(topicsPage, text = "DAA", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED)
        DAABtn.place(x = 500, y = 200)

        DSBtn = tk.Button(topicsPage, text = "DS", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED)
        DSBtn.place(x = 500, y = 300)

        backBtn = tk.Button(topicsPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(topicsPage))
        backBtn.place(x = 500, y = 400)
        
    def sendFile(self, filename, dest):

        DEST = r'D:/Hassan Files/Python Programming/OOP Semester Project/teacherUsers/'  +  dest
        SOURCE = r'D:/Hassan Files/Python Programming/OOP Semester Project/studentUsers/' + str(self.user)

        for root, subdirs, files in os.walk(SOURCE):

            if str(filename) in files:
                path = os.path.join(root, filename)
                shutil.copy(path, DEST)

                f = open(DEST + '/' + 'recieved.txt', 'a') 
                sentFile = str(filename) + ' sent by ' + str(self.user) + '\n'
                f.write(sentFile)
            else:
                print("Invalid File Entry")

    def readfile(self, filename):
        with open(filename) as f:
            return f.read()

    def OOP(self, root):

        OOPPage = tk.Toplevel(root)
        OOPPage.title("OOP Topics")
        OOPPage.configure(bg = "black")
        OOPPage.wm_state("zoomed")

        OOPLabel = tk.Label(OOPPage, text = "OOP TOPICS", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        OOPLabel.place(x = 400, y = 0)

        ClassBtn = tk.Button(OOPPage, text = "Classes", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Classes", 'D:\Hassan Files\Python Programming\OOP Semester Project\Study Topics\OOP\Class.txt'))
        ClassBtn.place(x = 500, y = 100)
        
        InhBtn = tk.Button(OOPPage, text = "Inheritance", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Classes", 'D:\Hassan Files\Python Programming\OOP Semester Project\Study Topics\OOP\Inherit.txt'))
        InhBtn.place(x = 500, y = 200)

        PolyBtn = tk.Button(OOPPage, text = "Polymorphism", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Classes", 'D:\Hassan Files\Python Programming\OOP Semester Project\Study Topics\OOP\Poly.txt'))
        PolyBtn.place(x = 500, y = 300)

        backBtn = tk.Button(OOPPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(OOPPage))
        backBtn.place(x = 500, y = 400)

    def topicDes(self, root, topicTitle, topicFile):

        topicPage = tk.Toplevel(root)
        topicPage.title(topicTitle)
        topicPage.configure(bg = "black")
        topicPage.wm_state("zoomed")

        definition = self.readfile(topicFile)

        topicLabel = tk.Label(topicPage, text = topicTitle, bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        topicLabel.place(x = 400, y = 0)

        defLabel = tk.Label(topicPage, text = definition, bg = "black", fg = "yellow", bd = 16, font = "Times 10 italic", relief = tk.RAISED)
        defLabel.place(x = 50, y = 200, width = 1250)

        backBtn = tk.Button(topicPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(topicPage))
        backBtn.place(x = 500, y = 600)

    def delete(self, root):
        root.destroy()
