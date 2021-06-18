import tkinter
from tkinter import *
import random

questions=[
    "Which of the following is an invalid variable ?",
    "Which of the following statements is wrong about inheritance ?",
    "Which of the following cannot be a variable ?",
    "What error occurs when you execute the following Python code snippet\napple = mango ?",
    "Which is the correct operator for power(xy) ?",
    "Which of the following functions helps us to randomize the items of a list ?",
    "Which one of the following has the highest precedence in the expression ?",
    "Which one of the following is not a python's predefined data type ?",
    "What is the type of inf ?",
    "Which of the following expressions results in an error ?",
    "Which of the following represents the bitwise XOR operator ?",
    "The output of which of the codes shown below will be: “There are 4 blue birds ?",
    "What will be the output of the following Python code\ni = 1\n\nwhile True:\n\n\nif i%3 == 0:\nbreak\nprint(i)\ni + = 1 ?",
    "What arithmetic operators cannot be used with strings ?",
    "Which of the following is not a valid namespace ?",
]

answers_choice=[
    ["my_string_1","1st_string","foo","_",],
    ["Protected members of a class can be inherited","The inheriting class is called a subclass","Private members of a class can be inherited and accessed","Inheritance is one of the features of OOP",],
    ["__init__","in","it","on",],
    ["SyntaxError","NameError","ValueError","TypeError",],
    ["X^y","X**y","X^^y","None of the mentioned",],
    ["seed","randomise","shuffle","uniform",],
    ["Exponential","Addition","Multiplication","Parentheses",],
    ["List","Dictionary","Tuple","Class",],
    ["Boolean","Integer","Float","Complex",],
    ["float(‘10’)","int(‘10’)","float(’10.8’)","int(’10.8’)",],
    ["&","^","|","!",],
    ["‘There are %g %d birds.’ %4 %blue","‘There are %d %s birds.’ %(4, blue)","‘There are %s %d birds.’ %[4, blue]","‘There are %d %s birds.’ 4, blue",],
    ["1 2","1 2 3","error","none of the mentioned",],
    ["+","*","–","All of the mentioned",],
    ["Global namespace","Public namespace","Built-in namespace","Local namespace",],
]

answers=[1,2,1,1,1,2,3,3,2,3,1,1,2,2,1]


user_answer=[]


randomlist=[]
def randomlistgen():
    global randomlist
    while(len(randomlist)<10):
        x=random.randint(0,14)
        if x in randomlist:
            continue
        else:
            randomlist.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage=Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext=Label(
        root,
        font=("Consolas",20),
        background="#ffffff",

    )
    labelresulttext.pack()
    if score>=90:
        img=PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You Are Excellent !!")
    elif (score>=20 and score<90):
        img=PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You Can be Better !!")
    else:
        img=PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="You Should Work Hard !!")


def calc():
    global randomlist,user_answer,answers
    x=0
    score=0
    for i in randomlist:
        if user_answer[x]==answers[i]:
            score=score+10
        x+=1
    print(score)
    showresult(score)


ques=1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x=radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques<10:
        lblQuestion.config(text=questions[randomlist[ques]])
        r1["text"]=answers_choice[randomlist[ques]][0]
        r2["text"]=answers_choice[randomlist[ques]][1]
        r3["text"]=answers_choice[randomlist[ques]][2]
        r4["text"]=answers_choice[randomlist[ques]][3]
        ques+=1
    else:
        print(randomlist)
        print(user_answer)
        calc()


def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion=Label(
        root,
        text=questions[randomlist[0]],
        font=("Times New Roman",16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff"
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)

    r1=Radiobutton(
        root,
        text=answers_choice[randomlist[0]][0],
        font=("Perpetua",12),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r1.pack(pady=5)

    r2=Radiobutton(
        root,
        text=answers_choice[randomlist[0]][1],
        font=("Perpetua",12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r2.pack(pady=5)

    r3=Radiobutton(
        root,
        text=answers_choice[randomlist[0]][2],
        font=("Perpetua",12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r3.pack(pady=5)

    r4=Radiobutton(
        root,
        text=answers_choice[randomlist[0]][3],
        font=("Perpetua",12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    randomlistgen()
    startquiz()


root=tkinter.Tk()
root.title("Python_Quiz")
root.geometry("680x580")
root.config(background="#ffffff")
root.resizable(0,0)

img1=PhotoImage(file="python2.png")

labelimage=Label(
    root,
    image=img1,
    background="#ffffff",
)
labelimage.pack()

labeltext=Label(
    root,
    text="Python_Quiz",
    font=("Segoe UI",24,"bold"),
    background="#ffffff",
)
labeltext.pack(pady=(0,20))


img2=PhotoImage(file="python3.png")
btnStart=Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    background="#FFD54F",
    command=startIspressed,
)
btnStart.pack()

lblInstruction=Label(
    root,
    text="Read The Rules And\nClick Start Once You Are Ready",
    background="#ffffff",
    font=("Cambria",12),
    justify="center",
)
lblInstruction.pack(pady=(70,30))

lblRules=Label(
    root,
    text="This Quiz Contains 10 Questions\nOnce You Select a Radio Button That Will be a Final Choice\nHence Think Before You Select",
    width=100,
    font=("Bookman Old Style",14),
    background="#000000",
    foreground="#F1C40F",
)
lblRules.pack()


root.mainloop()
