from Assets.scripts.settings import *
from Assets.scripts.commonFileFuntions import *


class Aplication(Frame):
    
    def __init__(self,root,testFile):
        super(Aplication,self).__init__(root)
        self.root = root
        self.logo = PhotoImage(file="Assets\sprites\logo.png")
        self.tts = pyttsx3.init()
        pg.mixer.init()
        self.loadSounds()
        # root.title("Term 3 Final Exam")
        self.test = openFileSafe(testFile,'r')
        self.title = self.test.readline()
        self.checked = False
        self.name = False
        self.name = ""    
        self.queNum = ""
        self.question = ""
        self.answers = []
        self.correct = ""
        self.explnation = ""
        self.score = 0
        self.curQue = 1
        self.totalQuestions = 50
        self.totalCorrect = 0
        self.queNum,self.question,self.answers,self.correct,self.explanation = self.read_question()
        self.mainMenu = Menu(self.root)
        self.root.configure(menu=self.mainMenu)   
        self.grid()
        self.createWidgets()
        self.createMenu()


    def loadSounds(self):
        try:
            pg.mixer_music.load(None)
        except:
            pass

    

    def read_question(self):
        """this is a method that will read the question information form the text file """
        queNum = nextLine(self.test)
        question = nextLine(self.test)
        answers = []
        for i in range(4):
            answers.append(nextLine(self.test))
        correct = nextLine(self.test)
        if correct:
            correct = correct[0]
        explanation = nextLine(self.test)
        return queNum,question,answers,correct,explanation
    

    def createWidgets(self):
       
        self.createLogo()
        self.createTitle()
        self.createNameBox()
        self.createQuestionLabel()
        self.createRadioBtns()
        self.createDisplayFeld()
        self.createNextButtn()
        self.createReadQue()
        self.createSubmitBttn()
        

    def createLogo(self):
        logo = Label(self,image=self.logo)
        logo.grid(row=0,column=0,columnspan=3,sticky=NSEW)
        print("Created logo")

    def createTitle(self):
        self.titleLbl =Label(self,text="Author: "+self.title,font=("sanserif",25))
        self.titleLbl.grid(row=1,column=0,columnspan=3,sticky=NSEW) 
        print("Created Title")
       
    def createNameBox(self):
        self.nameBox = Label(self,text="Enter Your Name",font=("sanserif",25))
        self.nameBox.grid(row=2,column=0,columnspan=3,sticky=NSEW)
        self.nameTbx = Entry(self,font=("sanserif",25))
        self.nameTbx.grid(row=3,column=1,columnspan=1,sticky=NSEW)
        self.nameTbx.bind("<KeyRelease>",self.onNameChanged)
        print("Created NameBox")


    def createQuestionLabel(self):
        self.queNumLbl = Label(self,font=("sanserif",18),text= self.queNum)
        self.queNumLbl.grid(row=4,column=0,columnspan=3,sticky=NSEW)
        self.queLbl = Label(self, text=self.question,font=("sanserif",18))
        self.queLbl.grid(row=5,column=0,columnspan=3,sticky=NSEW)
        print("Created queLbl")


    def createRadioBtns(self):
        self.readioBtnList = []
        self.optionChoice = StringVar()
        self.optionChoice.set(None)
        self.options = self.answers
        row = 6
        for i in range(4):
            
            x = Radiobutton(self,text=self.options[i],font=("sanserif",18),variable=self.optionChoice,value = i+1,command=lambda: self.changeState(self.submitBttn,'normal'))
            x.grid(row=row,column=0,columnspan=3,sticky=NSEW)
            self.readioBtnList.append(x)
            row +=1
        print("Created Radio btns")

    def createDisplayFeld(self):
        self.display = Text(self,width=125,height=3,wrap=WORD)
        self.display.grid(row=10,column=0,columnspan=3,sticky=NSEW) 
        print("Created display")

    def createReadQue(self):
        self.readBttn = Button(self,text="Read Question",font=("sanserif",18))  # this button is not hooked to a command to runn the function
        self.readBttn.grid(row=11, column=0,columnspan=1,sticky=NSEW)

    def createNextButtn(self):
        self.nextBttn = Button(self,text="Next Question",font=("sanserif",18),command= self.nextQue)  # this button is not hooked to a command to runn the function
        self.nextBttn.grid(row=11, column=2,columnspan=1,sticky=NSEW)
        self.nextBttn['state'] = 'disabled'
        print("Created NectBtn")
    
    def createSubmitBttn(self):
        self.submitBttn = Button(self,text="Submit Question",font=("sanserif",18),command= self.checkAns)
        self.submitBttn.grid(row=11, column=1,columnspan=1,sticky=NSEW)
        self.submitBttn['state'] = 'disabled'

    def changeState(self,object,state = str):
        """Change state to 'normal' or 'disabled'"""
        object['state'] = state

    def createMenu(self):
        fileMenu = Menu(self.mainMenu)
        settingsMenu = Menu(self.mainMenu)
        voiceMenu = Menu(self.mainMenu)

        self.mainMenu.add_cascade(label="File",menu=fileMenu)
        self.mainMenu.add_cascade(label="Settings",menu=settingsMenu)
        self.mainMenu.add_cascade(label="Change Voice",menu=voiceMenu)
        
        fileMenu.add_command(label="New Test",command=self.newTest)
        fileMenu.add_command(label="Change Test File",command=self.changeTestFile)

        settingsMenu.add_command(label="Mute",command=self.mute)

        voiceMenu.add_command(label="Change Voice",command=self.changeVoice)      

    def nextQue(self):
        if self.curQue == self.totalQuestions -1:
            self.nextBttn.config(text="Submit Test")
        if self.curQue < self.totalQuestions:
            self.display.delete(0.0,END)
            self.checked = False
            self.queNum,self.question,self.answers,self.correct,self.explanation = self.read_question()

            self.queNumLbl.config(text=self.queNum)
            self.queLbl.config(text=self.question)

            self.optionChoice.set(None)
            i = 0
            for btn in self.readioBtnList:
                btn.config(text=self.answers[i],variable=self.optionChoice,value = i+1)
                self.changeState(btn,'normal')
                i+= 1
            self.curQue += 1
        else:
            self.createReportCard()
        self.display.delete(0.0,END)
        self.display.insert(0.0,"This answer is "+str(self.correct))



    def newTest(self):
        pass

    def changeTestFile(self):
        pass

    def mute(self):
        pass

    def changeVoice(self):
        pass

    def checkAns(self):
        for b in self.readioBtnList:
            self.changeState(b,'disabled')
        if not self.name:
            self.optionChoice.set(None)
            output = "You must enter your name"
            self.display.delete(0.0,END)
            self.display.insert(0.0,output)
            return
        if not self.checked:
            self.checked = True
            self.nameTbx["state"] = "disabled"
            choice = self.optionChoice.get()
            if self.correct == choice:
                self.totalCorrect +=1
                output = "Correct!!\n"
            else:
                output = "Wrong!!\n"
            
            output += self.explanation
            self.display.delete(0.0,END)
            self.display.insert(0.0,output)
            self.nextBttn["state"] = "normal"
            self.changeState(self.submitBttn,'disabled')

    def onNameChanged(self,events):
        for b in self.readioBtnList:
            self.changeState(b,'normal')
        self.name = self.nameTbx.get()
        print(self.name)

    def readQuestionToUser(self):
        """this is a method that will read the question and answers out to the user using text to speach """
        self.tts.say(self.question)
        self.tts.runAndWait()
        for i in range(len(self.answers)):
            self.tts.say(str(i+1))
            self.tts.runAndWait()
            self.tts.say(self.answers[i])

    def createReportCard(self):
        import datetime as dt
        openedTime = dt.datetime.now()
        score, gradeMark = self.createScore()
        reportCard = openFileSafe("Assets/reportCards/reportCards.txt",'w+')
        reportCard.write("Test Taker: "+self.name + '\n')
        reportCard.write("Time Finished: "+str(openedTime) + '\n')
        reportCard.write(str.format("Score: {} Grade Mark: {}",score,gradeMark))
        
        reportCard.close()
        self.changeState(self.display,'normal')
        self.display.delete(0.0,END)
        
        self.display.insert(0.0,str.format("Your score was: {} {} press enter to quit",score,gradeMark))
        self.changeState(self.display,'disabled')
        input("")
        quit()

    def createScore(self):
        pointPerQue = (100/self.totalQuestions)
        score = self.totalCorrect*pointPerQue
        if score >= 93:
            gradeMark = 'A'
        elif score <93>=90:
            gradeMark = "A-"
        elif score <90>=87:
            gradeMark = "B+"
        elif score <87>=83:
            gradeMark = "B"
        elif score <83>=80:
            gradeMark = "B-"
        elif score <80>=77:
            gradeMark = "C+"
        elif score <77>=73:
            gradeMark = "C"
        elif score <73>=70:
            gradeMark = "C-"
        elif score <70>=67:
            gradeMark ="D+"
        elif score <67>=63:
            gradeMark = "D"
        elif score <63>=60:
            gradeMark = "D-"
        else:
            gradeMark = "F"
        

        score = str(score)
        gradeMark = str(gradeMark)
        return score,gradeMark

        
        