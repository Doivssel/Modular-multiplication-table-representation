#Last update 20/07/21 17:29

from tkinter import *
from PIL import ImageGrab

from math import cos,sin,pi


"""Definit l'ensemble de interface utilisateur"""
class GUI():
    def __init__(self,windows):
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
        #self.modulo=self.draw.create_text(400,400,text="678")

        self.draw.grid(row=0,column=0,padx=20,pady=20,rowspan=9)


        self.leaveButton=Button(windows,text="QUIT",command=windows.quit)
        self.calculateButton=Button(windows,text="CALCULATE",command=lambda:calculate(self.windows,self.moduloEntry.get(),self.tableEntry.get(),self.speedEntry.get(),self.checkVarModulo.get(),self.checkVarTable.get(),self.isClicked,self.draw))
        self.downloadButton=Button(windows,text='DOWNLOAD',command=lambda:downloadCommand(windows,self.draw))
        self.stopButton=Button(windows,text="STOP",command=lambda:stopButtonClick(self.isClicked))
        
        self.leaveButton.grid(row=8,column=1,sticky=NSEW,columnspan=2)
        self.calculateButton.grid(row=5,column=1,sticky=NSEW,columnspan=2)
        self.downloadButton.grid(row=7,column=1,sticky=NSEW,columnspan=2)
        self.stopButton.grid(row=6,column=1,sticky=NSEW,columnspan=2)

"""Permet de generer dans un tableau de dimension (modulo,2) l'ensemeble des points d'un cercle necessaire
tout en ayant un ecart d'angle entre chaque points egaux"""
def pointGeneraorCircle(modulo,l_coord):
    for i in range(0,modulo):
        for j in range(0,2):
            if j%2==0:
                l_coord[i][j]=cos(pi/2-i*((2*pi)/modulo))
            else:
                l_coord[i][j]=sin(pi/2-i*((2*pi)/modulo))

"""permet de verifier que l'utilisateur entre bien des nombres à finir"""
def verifyEntry(getRandomEntry):
    return True
    """for i in range(len(getRandomEntry)):
        if(ord(getRandomEntry[i])<=ord("9") and ord(getRandomEntry[i])>=ord("0") and i==len(getRandomEntry)-1):
            return True
        else:
            return False"""
    """i=0
    random=0
    while(i<=len(randomEntry)-1 and ord(randomEntry[i])<=ord("9") and ord(randomEntry[i])>=ord("0")):
        random=random*10+ord(randomEntry[i])-ord("0")
        i+=1
    return random"""

"""Les objet de type entry retourne des str, cette fonction sert à les convertir en int
en utilisant la valeur des car dans la table ASCII"""
def stringToInt(getRandomEntry):
    random=0
    if verifyEntry(getRandomEntry):
        for i in range(len(getRandomEntry)):
            random=random*10+ord(getRandomEntry[i])-ord("0")
        return random
    else:
        return 0

"""Permet de stop les animations en cours"""
def stopButtonClick(isClicked):
    isClicked.set(True)

"""On anime de 0 à la valeur de table avec une fonction recursive qui s'appele toute les
valeur de getspeedentry on affiche aussi la valeur de table et modulo"""
def animateTableMode(windows,getModuloEntry,getTableEntry,getSpeedEntry,isClicked,draw,j) :
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

"""On anime de 0 à la valeur de modulo avec une fonction recursive qui s'appele toute les
valeur de getspeedentry on affiche aussi la valeur de table et modulo"""
def animateModuloMode(windows,getTableEntry,getModuloEntry,getSpeedEntry,isClicked,draw,j) :
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

"""permet en fonction des checkbox de cocher de savoir qu'elle animation lancée ou de ne pas en lancer
dans le cas contraire"""
def calculate(windows,getModuloEntry,getTableEntry,getSpeedEntry,checkVarModulo,checkVarTable,isClicked,draw):
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

"""On se sert du module Pil pour faire une capture d"ecran il faut encore completer la partie
sur la sauvegarde auto"""
def downloadCommand(windows,draw):
    drawWidth=draw.winfo_width()
    drawHeight=draw.winfo_height()
    im=ImageGrab.grab(bbox=(22,22,drawWidth+15,drawHeight+15))
    im.show()#+telechargement automatique


windows=Tk()

interface=GUI(windows)

windows.update()

windows.mainloop()