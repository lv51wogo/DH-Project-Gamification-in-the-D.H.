import sys

if sys.version_info[0] != 3:
    import Tkinter as tk
else:
    import tkinter as tk

import getsData

questionDic = getsData.questionDic
AnswerDic = getsData.AnswerDic
QuestionCounter = 1




class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(MainMenue)

    def switch_frame(self, frame_class):
        global QuestionCounter
        QuestionCounter = 1
        
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        

   
class MainMenue(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.WelcomeLbl = tk.Label(self,text = 'Welocme to our little Python Quiz')
        self.WelcomeLbl.pack(pady =45) 
        self.WelcomeLbl.config(bg = '#4b8bbe',font=("Courier", 14))

        self.QuizBtn = tk.Button(self, text="Start Quiz",command=lambda: master.switch_frame(QuizPage))
        self.QuizBtn.pack(pady = 30)
        self.QuizBtn.config(bg = '#ffe873',font=("TkDefaultFont", 11))

        self.InfoBtn = tk.Button(self, text = 'Info' ,command= lambda : master.switch_frame(InfoPage))
        self.InfoBtn.pack(pady = 10)
        self.InfoBtn.config(bg = '#ffe873',font=("TkDefaultFont", 11))

        self.CreditsBtn = tk.Button(self,text = 'Credits', command = lambda: master.switch_frame(CreditsPage))
        self.CreditsBtn.pack(pady  = 30)
        self.CreditsBtn.config(bg = '#ffe873',font=("TkDefaultFont", 11))

        self.config(bg = '#4b8bbe')



class QuizPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.Question =tk.Label(self, text= list(questionDic[QuestionCounter].keys())[list(questionDic[QuestionCounter].values()).index('Q')])
        self.Question.pack(pady = 10)
        self.Question.config(bg = '#4b8bbe',font=("TkDefaultFont", 10))

        self.Answer1 = tk.Button(self, text= "True",command =  lambda: self.checkAnswer(AnswerDic[QuestionCounter][1]))
        self.Answer1.pack(pady = 3)
        self.Answer1.config(bg = '#ffe873')

        self.Answer2 = tk.Button(self, text= "1",command =  lambda: self.checkAnswer(AnswerDic[QuestionCounter][2]))
        self.Answer2.pack(pady = 3)
        self.Answer2.config(bg = '#ffe873')

        self.Answer3 = tk.Button(self, text= "42",command =  lambda: self.checkAnswer(AnswerDic[QuestionCounter][3]))
        self.Answer3.pack(pady = 3)
        self.Answer3.config(bg = '#ffe873')

        self.Answer4 = tk.Button(self, text= "Wahr",command =  lambda: self.checkAnswer(AnswerDic[QuestionCounter][4]))
        self.Answer4.pack(pady = 3)
        self.Answer4.config(bg = '#ffe873')

        self.AnswerStatus = tk.Label(self, text  = '')
        self.AnswerStatus.pack(pady  = 6)
        self.AnswerStatus.config(bg = '#4b8bbe')

        self.CorrectAnswer = tk.Label(self, text = '')
        self.CorrectAnswer.pack(pady = 6)
        self.CorrectAnswer.config(bg = '#4b8bbe')


        self.YourScore = tk.Label(self, text = 'Your Score :')
        self.YourScore.pack()
        self.YourScore.config(bg = '#4b8bbe')

        self.Counter = tk.Label(self, textvariable = total)
        self.Counter.pack(pady = 12 )
        self.Counter.config(bg = '#4b8bbe')

        self.NextQuestion = tk.Button(self, text= 'Next Question', command = self.nextQuestion)
        self.NextQuestion.pack( pady = 12)
        self.NextQuestion.config(bg = '#ffe873')

        self.ReturnToMain = tk.Button(self, text = 'Return to Main Menu', command = lambda: master.switch_frame(MainMenue))
        self.ReturnToMain.pack()
        self.ReturnToMain.config(bg = '#ffe873')

        self.config(bg = '#4b8bbe')

    
        
    def checkAnswer(self, key):
        if questionDic[QuestionCounter][key] == 'T':
      
            self.Answer1.config(state = 'disabled')
            self.Answer2.config(state = 'disabled')
            self.Answer3.config(state = 'disabled')
            self.Answer4.config(state = 'disabled')            


            self.AnswerStatus.config(text = 'Correct',font = 'TkDefaultFont  10 bold' , fg = '#06FF2F')
            total.set(total.get() + 1)

        else:

            self.CorrectAnswer.config(text = ' The correct answer would have been' +  ' "' + list(questionDic[QuestionCounter].keys())[list(questionDic[QuestionCounter].values()).index('T')] + '"' )
            self.AnswerStatus.config(text = 'False')
            self.AnswerStatus.config(font = 'TkDefaultFont  10 bold' , fg = 'red')

            self.Answer1.config(state = 'disabled')
            self.Answer2.config(state = 'disabled')
            self.Answer3.config(state = 'disabled')
            self.Answer4.config(state = 'disabled')

    def nextQuestion(self): 

        global QuestionCounter
        global CorrectAnswerCounter

        if QuestionCounter < len(questionDic):
            QuestionCounter += 1
            self.AnswerStatus.config(text ='')
            self.Question.config(text = list(questionDic[QuestionCounter].keys())[list(questionDic[QuestionCounter].values()).index('Q')])
            self.Answer1.config(text = AnswerDic[QuestionCounter][1])
            self.Answer2.config(text = AnswerDic[QuestionCounter][2])
            self.Answer3.config(text = AnswerDic[QuestionCounter][3])
            self.Answer4.config(text = AnswerDic[QuestionCounter][4])

            self.Answer1.config(state = 'normal')
            self.Answer2.config(state = 'normal')
            self.Answer3.config(state = 'normal')
            self.Answer4.config(state = 'normal')

            self.CorrectAnswer.config(text = '')

           

        else :
            self.master.switch_frame(EndPage)
            
            


class EndPage(tk.Frame):

	def __init__(self, master):
		tk.Frame.__init__(self, master)
		
		self.CongratsLbl = tk.Label(self, text = 'Congratulations!!!\n\n\nYou answered ' + str(total.get())  + ' from ' + str(len(questionDic)) + ' Questions correct.')
		self.CongratsLbl.config(bg = '#4b8bbe',font=("TkDefaultFont", 14))
		self.CongratsLbl.pack(pady  = 80)

		self.ReturnToMain = tk.Button(self, text = 'Return to Main Menu', command = lambda: master.switch_frame(MainMenue))
		self.ReturnToMain.pack()
		self.ReturnToMain.config(bg = '#ffe873')

		self.config(bg = '#4b8bbe')

class InfoPage(tk.Frame):

	def __init__(self, master):
		tk.Frame.__init__(self, master)

		self.InfoLbl = tk.Label(self,text = 'This quiz is to getsData your Python knowledge and not to build it up.\nIt is not intended as a stand-alone Python learning tool.\n\n\n\n\nTo begin simply click the "Start Quiz" Button and then click on the'
						+ '\ncorrect answer for the given question.\n\n\n\n\nAfter you have answered the last question, \nyou will see how many questions you have answered correctly. ')
		self.InfoLbl.pack(pady = 60)
		self.InfoLbl.config(bg = '#4b8bbe')

		self.ReturnToMain = tk.Button(self, text = 'Return to Main Menu', command = lambda: master.switch_frame(MainMenue))
		self.ReturnToMain.pack()
		self.ReturnToMain.config(bg = '#ffe873')

		self.config(bg = '#4b8bbe')


class CreditsPage(tk.Frame):

	def __init__(self, master):
		tk.Frame.__init__(self, master)

		self.CreditsLbl = tk.Label(self, text = 'Coding = Tim Karwasz\n\n\nfor the Gamification Project WS 2018/2019')
		self.CreditsLbl.pack(pady = 50)
		self.CreditsLbl.config(bg = '#4b8bbe')

		self.ReturnToMain = tk.Button(self, text = 'Return to Main Menu', command = lambda: master.switch_frame(MainMenue))
		self.ReturnToMain.pack()
		self.ReturnToMain.config(bg = '#ffe873')

		self.config(bg = '#4b8bbe')

#Basically, it separates the dictionary's values in a list, finds the position of the value you have, and gets the key at that position.'
#  list(question1.keys())[list(question1.values()).index('Q')]
if __name__ == "__main__":
    app = SampleApp()
    
    total = tk.IntVar()
    app.config(bg = '#4b8bbe')
    app.geometry('480x400')

    app.title('Python Quiz')
    app.resizable(0,0)
 
    app.mainloop()