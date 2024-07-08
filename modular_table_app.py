from tkinter import *
from PIL import ImageGrab
from math import cos,sin,pi

class GUI():
    def __init__(self,windows):
        """
        Parameters:
        windows: tkinter.Tk() instance
        
        Goal:
        Graphics representation, button...
        """
        self.windows=windows
        windows.title("Table modulaire")
        windows.attributes('-fullscreen',True)
        windows.update()

        self.checkVarModulo=IntVar()
        self.checkVarTable=IntVar()
        self.isClicked=BooleanVar()

        self.moduloText=Label(windows,text="MODULO : ")
        self.tableText=Label(windows,text="TABLE : ")
        self.speedText=Label(windows,text="ANIMATION SPEED : ")
        self.moduloEntry=Entry(windows)
        self.tableEntry=Entry(windows)
        self.speedEntry=Entry(windows)

        self.speedEntry.insert(0,"10")

        self.moduloText.grid(row=0,column=1,sticky=NSEW)
        self.tableText.grid(row=1,column=1,sticky=NSEW)
        self.speedText.grid(row=2,column=1,sticky=NSEW)
        self.moduloEntry.grid(row=0,column=2,sticky=EW)
        self.tableEntry.grid(row=1,column=2,sticky=EW)
        self.speedEntry.grid(row=2,column=2,sticky=EW)

        self.checkBoxModuloAnim=Checkbutton(self.windows,text="Animation modulo",variable=self.checkVarModulo,onvalue=1,offvalue=0)
        self.checkBoxTableAnim=Checkbutton(self.windows,text="Animation table",variable=self.checkVarTable,onvalue=1,offvalue=0)
        
        self.checkBoxModuloAnim.grid(row=3,column=1,sticky=NSEW,columnspan=2)
        self.checkBoxTableAnim.grid(row=4,column=1,stick=NSEW,columnspan=2)

        self.draw = Canvas(windows,bg='white',width=windows.winfo_width()*15/20,height=windows.winfo_height()-40)

        self.draw.grid(row=0,column=0,padx=20,pady=20,rowspan=9)


        self.leaveButton=Button(windows,text="QUIT",command=windows.quit)
        self.calculateButton=Button(windows,text="CALCULATE",command=lambda:calculate(self.windows,self.moduloEntry.get(),self.tableEntry.get(),self.speedEntry.get(),self.checkVarModulo.get(),self.checkVarTable.get(),self.isClicked,self.draw))
        self.downloadButton=Button(windows,text='DOWNLOAD',command=lambda:downloadCommand(windows,self.draw))
        self.stopButton=Button(windows,text="STOP",command=lambda:stopButtonClick(self.isClicked))
        
        self.leaveButton.grid(row=8,column=1,sticky=NSEW,columnspan=2)
        self.calculateButton.grid(row=5,column=1,sticky=NSEW,columnspan=2)
        self.downloadButton.grid(row=7,column=1,sticky=NSEW,columnspan=2)
        self.stopButton.grid(row=6,column=1,sticky=NSEW,columnspan=2)


def pointGeneraorCircle(modulo,l_coord):
    """
    Parameters:
    modulo: int self explanatory
    l_coord: list used to store coords
    
    Goal:
    Creating a list of dim (modulo,2) that store the position of the point on the circle.
    These point must have the same distance between them.
    """
    for i in range(0,modulo):
        for j in range(0,2):
            if j%2==0:
                l_coord[i][j]=cos(pi/2-i*((2*pi)/modulo))
            else:
                l_coord[i][j]=sin(pi/2-i*((2*pi)/modulo))

def verifyEntry(getRandomEntry):
    """
    Parameters:
    getRandomEntry: input of an entry tkinter widget

    Goal:
    Verify if the input of the widgets are of the correct type

    Note:
    Either to complete or delete
    """
    return True


def stringToInt(getRandomEntry):
    """
    Parameters:
    getRandomEntry: input of an entry tkinter widget

    Goal:
    The widget used here only return string, for example 1 get returned as "1".
    As such this function convert the string to int using the ASCII table. It is important to note 
    that it also convert letters or every characters in fact. That's why the verifyEntry
    function may be unecessary
    """
    random=0
    if verifyEntry(getRandomEntry):
        for i in range(len(getRandomEntry)):
            random=random*10+ord(getRandomEntry[i])-ord("0")
        return random
    else:
        return 0


def stopButtonClick(isClicked):
    """
    Parameters:
    isClicked: output of a button widget

    Goal:
    Stop the animation when the stop button widget is clicked
    """
    isClicked.set(True)


def animateTableMode(windows,getModuloEntry,getTableEntry,getSpeedEntry,isClicked,draw,j) :
    """
    Parameters:
    windows: tkinter.TK instance
    getModuloEntry: output of the Modulo entry widget
    getTabbleEntry: output of the Table entry widget
    getSpeedEntry: output of the Speed entry widget
    isClicked: output of the isClicked button widget
    draw: output of the draw button widget
    j: int explained in goal
    
    Goal:
    Animate from 0 to getTableEntry the graph by using a recursie function
    that call itself every getSpeedEntry. As such j is used to keep track of the current table animated
    to animate the next one
    """

    draw.delete("all")
    if(j<=stringToInt(getTableEntry)):
        draw.create_text(draw.winfo_width()/2+100,draw.winfo_height()-40,text="TABLE : "+str(j),font=("Arial", 10,))
        draw.create_text(draw.winfo_width()/2-100,draw.winfo_height()-40,text="MODULO : "+getModuloEntry,font=("Arial", 10,))
        l_coord=[[0]*(2) for _ in range(stringToInt(getModuloEntry))]
        pointGeneraorCircle(stringToInt(getModuloEntry),l_coord)
        for i in range(1,stringToInt(getModuloEntry)):
            draw.create_line(draw.winfo_width()/2+290*l_coord[i][0],draw.winfo_height()/2+290*l_coord[i][1],draw.winfo_width()/2+290*l_coord[(i*j)%stringToInt(getModuloEntry)][0],draw.winfo_height()/2+290*l_coord[(i*j)%stringToInt(getModuloEntry)][1],fill="black",width=1)
        if(isClicked.get()!=True):
            windows.after(getSpeedEntry,lambda :animateTableMode(windows,getModuloEntry,getTableEntry,getSpeedEntry,isClicked,draw,j=j+1))


def animateModuloMode(windows,getTableEntry,getModuloEntry,getSpeedEntry,isClicked,draw,j) :
    """
    Parameters:
    windows: tkinter.TK instance
    getModuloEntry: output of the Modulo entry widget
    getTabbleEntry: output of the Table entry widget
    getSpeedEntry: output of the Speed entry widget
    isClicked: output of the isClicked button widget
    draw: output of the draw button widget
    j: int explained in goal
    
    Goal:
    Animate from 0 to getModuloEntry the graph by using a recursie function
    that call itself every getSpeedEntry. As such j is used to keep track of the current table animated
    to animate the next one
    """
    draw.delete("all")
    if(j<=stringToInt(getModuloEntry)):
        draw.create_text(draw.winfo_width()/2+100,draw.winfo_height()-40,text="TABLE : "+getTableEntry,font=("Arial", 10,))
        draw.create_text(draw.winfo_width()/2-100,draw.winfo_height()-40,text="MODULO : "+str(j),font=("Arial", 10,))
        l_coord=[[0]*(2) for _ in range(j)]
        pointGeneraorCircle(j,l_coord)
        for i in range(1,j):
            draw.create_line(draw.winfo_width()/2+290*l_coord[i][0],draw.winfo_height()/2+290*l_coord[i][1],draw.winfo_width()/2+290*l_coord[(i*stringToInt(getTableEntry))%j][0],draw.winfo_height()/2+290*l_coord[(i*stringToInt(getTableEntry))%j][1],fill="black",width=1)
        if(isClicked.get()!=True):
            windows.after(getSpeedEntry,lambda :animateModuloMode(windows,getTableEntry,getModuloEntry,getSpeedEntry,isClicked,draw,j=j+1))


def calculate(windows,getModuloEntry,getTableEntry,getSpeedEntry,checkVarModulo,checkVarTable,isClicked,draw):
    """
    Parameters:
    windows: tkinter.TK instance
    getModuloEntry: output of the Modulo entry widget
    getTabbleEntry: output of the Table entry widget
    getSpeedEntry: output of the Speed entry widget
    chechVarModulo: output of the Modulo checkButton
    chechVarTable: output of the Table checkButton
    isClicked: output of the isClicked button widget
    draw: output of the draw button widget
    
    Goal:
    Used to decide what to animate/draw depending on the current configuration of all the widgets
    """
    draw.delete("all")
    isClicked.set(False)
    j=0
    if(checkVarTable==1):
        animateTableMode(windows,getModuloEntry,getTableEntry,getSpeedEntry,isClicked,draw,j)
    else:
        if(checkVarModulo==1):
            animateModuloMode(windows,getTableEntry,getModuloEntry,getSpeedEntry,isClicked,draw,j)
        else:
            l_coord=[[0]*(2) for _ in range(stringToInt(getModuloEntry))]
            pointGeneraorCircle(stringToInt(getModuloEntry),l_coord)
            draw.create_text(draw.winfo_width()/2+100,draw.winfo_height()-40,text="TABLE : "+getTableEntry,font=("Arial", 10,))
            draw.create_text(draw.winfo_width()/2-100,draw.winfo_height()-40,text="MODULO : "+getModuloEntry,font=("Arial", 10,))
            for i in range(1,stringToInt(getModuloEntry)):
                draw.create_line(draw.winfo_width()/2+290*l_coord[i][0],draw.winfo_height()/2+290*l_coord[i][1],draw.winfo_width()/2+290*l_coord[(i*stringToInt(getTableEntry))%stringToInt(getModuloEntry)][0],draw.winfo_height()/2+290*l_coord[(i*stringToInt(getTableEntry))%stringToInt(getModuloEntry)][1],fill="black",width=1)


def downloadCommand(windows,draw):
    """
    Goal:
    Download a graph
    """
    drawWidth=draw.winfo_width()
    drawHeight=draw.winfo_height()
    im=ImageGrab.grab(bbox=(22,22,drawWidth+15,drawHeight+15))
    im.show()


windows=Tk()

interface=GUI(windows)

windows.update()

windows.mainloop()
