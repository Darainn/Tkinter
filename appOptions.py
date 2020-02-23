import tkinter as tk
import textEditor as text
import message as msg
import os
import shutil

class TeacherOptions():

    def __init__(self, master, user):
        self.master = master
        self.user = user
        
        optPage = tk.Toplevel(self.master)
        optPage.title("App Options")
        optPage.configure(bg = "black")
        optPage.wm_state("zoomed")

        optLabel = tk.Label(optPage, text = "TEACHER MENU", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        optLabel.place(x = 400, y = 0)

        sendBtn = tk.Button(optPage, text = "SEND FILE", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.send(self.master))
        sendBtn.place(x = 500, y = 200)

        recieveBtn = tk.Button(optPage, text = "VIEW RECIEVED", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.recieve(self.master))
        recieveBtn.place(x = 500, y = 300)

        topicsBtn = tk.Button(optPage, text = "EDIT TOPICS", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topics(self.master))
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

        fileLabel = tk.Label(sendPage, text = "Enter the filename to send: ", bg = "black", fg = "yellow", bd = 16, font = "Times 28 bold italic", relief = tk.RAISED)
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

        recieveFile = 'C:/OOP Project/OOP Semester Project/teacherUsers/' + str(self.user) + '/recieved.txt'

        recieveLabel = tk.Label(recievePage, text = "RECIEVED FILES", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        recieveLabel.place(x = 400, y = 0)

        recieveText = text.Text(recievePage, bg = 'black', fg = 'yellow', width = 150, bd = 12, relief = tk.RAISED)

        with open(recieveFile, 'r') as f:
            recieveText.insert(tk.INSERT, f.read())

        recieveText.configure(state = tk.DISABLED)
        recieveText.place(x = 100, y = 100)

        backBtn = tk.Button(recievePage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(recievePage))
        backBtn.place(x = 500, y = 600)


    def topics(self, root):

        topicsPage = tk.Toplevel(root)
        topicsPage.title("Topics")
        topicsPage.configure(bg = "black")
        topicsPage.wm_state("zoomed")

        topicsLabel = tk.Label(topicsPage, text = "EDIT TOPICS", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        topicsLabel.place(x = 400, y = 0)

        OOPBtn = tk.Button(topicsPage, text = "OBJECT ORIENTED PROGRAMMING", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.OOP(self.master))
        OOPBtn.place(x = 500, y = 100)
        
        DAABtn = tk.Button(topicsPage, text = "DATA STRUCTURE ALGORITHMS", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.DAA(self.master))
        DAABtn.place(x = 500, y = 200)

        DSBtn = tk.Button(topicsPage, text = "DISCRETE STRUCTURES", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.DS(self.master))
        DSBtn.place(x = 500, y = 300)

        backBtn = tk.Button(topicsPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(topicsPage))
        backBtn.place(x = 500, y = 400)
    
    
    def sendFile(self, filename, dest):

        DEST = r'C:/OOP Project/OOP Semester Project/studentUsers/'  +  dest
        SOURCE = r'C:/OOP Project/OOP Semester Project/teacherUsers/' + str(self.user)

        for root, subdirs, files in os.walk(SOURCE):

            if str(filename) in files:
                path = os.path.join(root, filename)
                shutil.copy(path, DEST)

                f = open(DEST + '/' + 'recieved.txt', 'a') 
                sentFile = str(filename) + ' sent by ' + str(self.user) + '\n'
                f.write(sentFile)

                mes = meg.Message(self.master, "FIle Sent Successfully")
            else:
                mes = msg.Message(self.master , "Invalid File Entry")

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

        ClassBtn = tk.Button(OOPPage, text = "CLASSES", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Classes", 'C:\OOP Project\OOP Semester Project\Study Topics\OOP\CLASS.txt'))
        ClassBtn.place(x = 500, y = 100)
        
        InhBtn = tk.Button(OOPPage, text = "INHERITANCE", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Inheritance", 'C:\OOP Project\OOP Semester Project\Study Topics\OOP\INHERITANCE.txt'))
        InhBtn.place(x = 500, y = 200)

        PolyBtn = tk.Button(OOPPage, text = "POLYMORPHISM", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Polymorphism", 'C:\OOP Project\OOP Semester Project\Study Topics\OOP\POLYMORPHISM.txt'))
        PolyBtn.place(x = 500, y = 300)

        VirBtn = tk.Button(OOPPage, text = "VIRTUAL FUNCTIONS", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Virtual Functions", 'C:\OOP Project\OOP Semester Project\Study Topics\OOP\VIRTUAL FUNCTIONS.txt'))
        VirBtn.place(x = 500, y = 400)

        MultifileBtn = tk.Button(OOPPage, text = "MULTIFILING", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Multifiling", 'C:\OOP Project\OOP Semester Project\Study Topics\OOP\MULTIFILING.txt'))
        MultifileBtn.place(x = 500, y = 500)
        
        backBtn = tk.Button(OOPPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(OOPPage))
        backBtn.place(x = 500, y = 600)

    def DS(self, root):

        DSPage = tk.Toplevel(root)
        DSPage.title("DS Topics")
        DSPage.configure(bg = "black")
        DSPage.wm_state("zoomed")
        
        DSLabel = tk.Label(DSPage, text = "DS TOPICS", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        DSLabel.place(x = 400, y = 0)

        DiscreteStructureBtn = tk.Button(DSPage, text = "DISCRETE STRUCTURE", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Discrete Structure", 'C:\OOP Project\OOP Semester Project\Study Topics\DS\DISCRETE STRUCTURE.txt'))
        DiscreteStructureBtn.place(x = 500, y = 100)
        
        FunctionNRelationBtn = tk.Button(DSPage, text = "FUNCTION N RELATION", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Function N Relation",  'C:\OOP Project\OOP Semester Project\Study Topics\DS\FUNCTIONS AND RELATION.txt'))
        FunctionNRelationBtn.place(x = 500, y = 200)

        GraphsBtn = tk.Button(DSPage, text = "GRAPHS", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Graphs", 'C:\OOP Project\OOP Semester Project\Study Topics\DS\GRAPHS.txt'))
        GraphsBtn.place(x = 500, y = 300)

        TruthtableBtn = tk.Button(DSPage, text = "TRUTHTABLE", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Truthtable", 'C:\OOP Project\OOP Semester Project\Study Topics\DS\TRUTH TABLE.txt'))
        TruthtableBtn.place(x = 500, y = 400)

        RecursiveRelationBtn = tk.Button(DSPage, text = "RECURSIVE RELATION", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Recursive Relation", 'C:\OOP Project\OOP Semester Project\Study Topics\DS\RECURSIVE RELATION.txt'))
        RecursiveRelationBtn.place(x = 500, y = 500)

        backBtn = tk.Button(DSPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(DSPage))
        backBtn.place(x = 500, y = 600)

    def DAA(self, root):

        DAAPage = tk.Toplevel(root)
        DAAPage.title("DAA Topics")
        DAAPage.configure(bg = "black")
        DAAPage.wm_state("zoomed")

        DAALabel = tk.Label(DAAPage, text = "DAA TOPICS", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        DAALabel.place(x = 400, y = 0)

        AlgoBtn = tk.Button(DAAPage, text = "ALGORITHM", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Algorithm", 'C:\OOP Project\OOP Semester Project\Study Topics\DAA\ALGORITHM.txt'))
        AlgoBtn.place(x = 500, y = 100)
        
        ArrayBtn = tk.Button(DAAPage, text = "ARRAY", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Array",  'C:\OOP Project\OOP Semester Project\Study Topics\DAA\ARRAY.txt'))
        ArrayBtn.place(x = 500, y = 200)

        LinkedListBtn = tk.Button(DAAPage, text = "LINKED LIST", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Linked list", 'C:\OOP Project\OOP Semester Project\Study Topics\DAA\LINKED LIST.txt'))
        LinkedListBtn.place(x = 500, y = 300)

        QueueBtn = tk.Button(DAAPage, text = "QUEUE", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Queue", 'C:\OOP Project\OOP Semester Project\Study Topics\DAA\QUEUE.txt'))
        QueueBtn.place(x = 500, y = 400)

        StackBtn = tk.Button(DAAPage, text = "STACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Stack", 'C:\OOP Project\OOP Semester Project\Study Topics\DAA\STACK.txt'))
        StackBtn.place(x = 500, y = 500)

        backBtn = tk.Button(DAAPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(DAAPage))
        backBtn.place(x = 500, y = 600)
    
    def topicDes(self, root, topicTitle, topicFile):

        topicPage = tk.Toplevel(root)
        topicPage.title(topicTitle)
        topicPage.configure(bg = "black")
        topicPage.wm_state("zoomed")

        topicLabel = tk.Label(topicPage, text = topicTitle, bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        topicLabel.place(x = 400, y = 0)

        topicText = text.Text(topicPage, bg = 'black', fg = 'yellow', width = 150, bd = 12, relief = tk.RAISED)

        with open(topicFile, 'r') as f:
            topicText.insert(tk.INSERT, f.read())

        topicText.place(x = 100, y = 100)

        def finish(event = None):
            with open(topicFile, "w") as f:
                f.write(ending_text)

        topicText.bind("<Destroy>", finish)
        
        backBtn = tk.Button(topicPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(topicPage))
        backBtn.place(x = 500, y = 600)

    def delete(self, root):
        root.destroy()
 

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

        fileLabel = tk.Label(sendPage, text = "Enter the filename to send: ", bg = "black", fg = "yellow", bd = 16, font = "Times 28 bold italic", relief = tk.RAISED)
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

        recieveFile = 'C:/OOP Project/OOP Semester Project/studentUsers/' + str(self.user) + '/recieved.txt'

        recieveLabel = tk.Label(recievePage, text = "RECIEVED FILES", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        recieveLabel.place(x = 400, y = 0)

        recieveText = text.Text(recievePage, bg = 'black', fg = 'yellow', width = 150, bd = 12, relief = tk.RAISED)

        with open(recieveFile, 'r') as f:
            recieveText.insert(tk.INSERT, f.read())

        recieveText.configure(state = tk.DISABLED)
        recieveText.place(x = 100, y = 100)

        backBtn = tk.Button(recievePage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(recievePage))
        backBtn.place(x = 500, y = 600)

    def topics(self, root):

        topicsPage = tk.Toplevel(root)
        topicsPage.title("Topics")
        topicsPage.configure(bg = "black")
        topicsPage.wm_state("zoomed")

        topicsLabel = tk.Label(topicsPage, text = "STUDY TOPICS", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        topicsLabel.place(x = 400, y = 0)

        OOPBtn = tk.Button(topicsPage, text = "OBJECT ORIENTED PROGRAMMING", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.OOP(self.master))
        OOPBtn.place(x = 500, y = 100)
        
        DAABtn = tk.Button(topicsPage, text = "DATA STRUCTURE ALGORITHMS", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED,command = lambda: self.DAA(self.master))
        DAABtn.place(x = 500, y = 200) 

        DSBtn = tk.Button(topicsPage, text = "DISCRETE STRUCTURES", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED,command = lambda: self.DS(self.master))
        DSBtn.place(x = 500, y = 300)

        backBtn = tk.Button(topicsPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(topicsPage))
        backBtn.place(x = 500, y = 400)
        
    def sendFile(self, filename, dest):

        DEST = r'C:/OOP Project/OOP Semester Project/teacherUsers/'  +  dest
        SOURCE = r'C:/OOP Project/OOP Semester Project/studentUsers/' + str(self.user)

        for root, subdirs, files in os.walk(SOURCE):

            if str(filename) in files:
                path = os.path.join(root, filename)
                shutil.copy(path, DEST)

                f = open(DEST + '/' + 'recieved.txt', 'a') 
                sentFile = str(filename) + ' sent by ' + str(self.user) + '\n'
                f.write(sentFile)

                mes = msg.Message(self.master, "File Sent Successfully")
            else:
                mes = msg.Message(self.master, "Invalid File Entry")

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

        ClassBtn = tk.Button(OOPPage, text = "CLASSES", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Classes", 'C:\OOP Project\OOP Semester Project\Study Topics\OOP\CLASS.txt'))
        ClassBtn.place(x = 500, y = 100)
        
        InhBtn = tk.Button(OOPPage, text = "INHERITANCE", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Inheritance",  'C:\OOP Project\OOP Semester Project\Study Topics\OOP\INHERITANCE.txt'))
        InhBtn.place(x = 500, y = 200)

        PolyBtn = tk.Button(OOPPage, text = "POLYMORPHISM", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Polymorphism", 'C:\OOP Project\OOP Semester Project\Study Topics\OOP\POLYMORPHSIM.txt'))
        PolyBtn.place(x = 500, y = 300)

        VirBtn = tk.Button(OOPPage, text = "VIRTUAL FUNCTIONS", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Virtual Functions", 'C:\OOP Project\OOP Semester Project\Study Topics\OOP\VIRTUAL FUNCTIONS.txt'))
        VirBtn.place(x = 500, y = 400)

        MultifileBtn = tk.Button(OOPPage, text = "MULTIFILING", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Multifiling", 'C:\OOP Project\OOP Semester Project\Study Topics\OOP\MULTIFILING.txt'))
        MultifileBtn.place(x = 500, y = 500)

        backBtn = tk.Button(OOPPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(OOPPage))
        backBtn.place(x = 500, y = 600)

    def DS(self, root):

        DSPage = tk.Toplevel(root)
        DSPage.title("DS Topics")
        DSPage.configure(bg = "black")
        DSPage.wm_state("zoomed")

        DSLabel = tk.Label(DSPage, text = "DS TOPICS", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        DSLabel.place(x = 400, y = 0)

        DiscreteStructureBtn = tk.Button(DSPage, text = "DISCRETE STRUCTURE", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Discrete Structure", 'C:\OOP Project\OOP Semester Project\Study Topics\DS\DISCRETE STRUCTURE.txt'))
        DiscreteStructureBtn.place(x = 500, y = 100)
        
        FunctionNRelationBtn = tk.Button(DSPage, text = "FUNCTION N RELATION", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Function N Relation",  'C:\OOP Project\OOP Semester Project\Study Topics\DS\FUNCTIONS AND RELATION.txt'))
        FunctionNRelationBtn.place(x = 500, y = 200)

        GraphsBtn = tk.Button(DSPage, text = "GRAPHS", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Graphs", 'C:\OOP Project\OOP Semester Project\Study Topics\DS\GRAPHS.txt'))
        GraphsBtn.place(x = 500, y = 300)

        TruthtableBtn = tk.Button(DSPage, text = "TRUTHTABLE", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Truthtable", 'C:\OOP Project\OOP Semester Project\Study Topics\DS\TRUTH TABLE.txt'))
        TruthtableBtn.place(x = 500, y = 400)

        RecursiveRelationBtn = tk.Button(DSPage, text = "RECURSIVE RELATION", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Recursive Relation", 'C:\OOP Project\OOP Semester Project\Study Topics\DS\RECURSIVE RELATION.txt'))
        RecursiveRelationBtn.place(x = 500, y = 500)

        backBtn = tk.Button(DSPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(DSPage))
        backBtn.place(x = 500, y = 600)

    def DAA(self, root):

        DAAPage = tk.Toplevel(root)
        DAAPage.title("DAA Topics")
        DAAPage.configure(bg = "black")
        DAAPage.wm_state("zoomed")

        DAALabel = tk.Label(DAAPage, text = "DAA TOPICS", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        DAALabel.place(x = 400, y = 0)

        AlgoBtn = tk.Button(DAAPage, text = "ALGORITHM", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Algorithm", 'C:\OOP Project\OOP Semester Project\Study Topics\DAA\ALGORITHM.txt'))
        AlgoBtn.place(x = 500, y = 100)
        
        ArrayBtn = tk.Button(DAAPage, text = "ARRAY", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Array",  'C:\OOP Project\OOP Semester Project\Study Topics\DAA\ARRAY.txt'))
        ArrayBtn.place(x = 500, y = 200)

        LinkedListBtn = tk.Button(DAAPage, text = "LINKED LIST", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Linked list", 'C:\OOP Project\OOP Semester Project\Study Topics\DAA\LINKED LIST.txt'))
        LinkedListBtn.place(x = 500, y = 300)

        QueueBtn = tk.Button(DAAPage, text = "QUEUE", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Queue", 'C:\OOP Project\OOP Semester Project\Study Topics\DAA\QUEUE.txt'))
        QueueBtn.place(x = 500, y = 400)

        StackBtn = tk.Button(DAAPage, text = "STACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topicDes(self.master, "About Stack", 'C:\OOP Project\OOP Semester Project\Study Topics\DAA\STACK.txt'))
        StackBtn.place(x = 500, y = 500)

        backBtn = tk.Button(DAAPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(DAAPage))
        backBtn.place(x = 500, y = 600)


    def topicDes(self, root, topicTitle, topicFile):

        topicPage = tk.Toplevel(root)
        topicPage.title(topicTitle)
        topicPage.configure(bg = "black")
        topicPage.wm_state("zoomed")

        topicLabel = tk.Label(topicPage, text = topicTitle, bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        topicLabel.place(x = 400, y = 0)

        topicText = text.Text(topicPage, bg = 'black', fg = 'yellow', width = 150, bd = 12, relief = tk.RAISED)

        with open(topicFile, 'r') as f:
            topicText.insert(tk.INSERT, f.read())

        topicText.configure(state = tk.DISABLED)
        topicText.place(x = 100, y = 100)

        backBtn = tk.Button(topicPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(topicPage))
        backBtn.place(x = 500, y = 600)

    def delete(self, root):
        root.destroy()
