import tkinter # import library for images in python
from tkinter import *
from PIL import Image, ImageTk # used for visualization but used here for importing images

import random


class Environment(object):
    def __init__(self, win):
        # instantiate locations and conditions
        # 0 indicates Clean and 1 indicates Dirty
        self.Location = ['A', 'B']
        self.locationCondition = {'A': '0', 'B': '0'}

        # randomize conditions
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)
        # place vacuum at random location
        self.vacuumLocation = random.choice(self.Location)

    def displayEnv(self, win): # describing the GUI
        imaged = Image.open("dirt.png") # open img
        pic1 = imaged.resize((176, 146), Image.ANTIALIAS) # resize img
        picd = ImageTk.PhotoImage(pic1) # add img to form

        imagec = Image.open("clean.png")
        pic2 = imagec.resize((176, 146), Image.ANTIALIAS)
        picc = ImageTk.PhotoImage(pic2)

        imagev = Image.open("vacuum.png")
        pic3 = imagev.resize((30, 30), Image.ANTIALIAS)
        picv = ImageTk.PhotoImage(pic3)
        gridLabel = {'A': '0', 'B': '1'} # dictates how things will be layed out on the screen. (Grid Geometry used here)

        if self.locationCondition[self.vacuumLocation] == 0: # when room is cleaned, superimpose clean img over dirty img
            # use clean image
            imagelv = imagec
            # superimpose vacuum and clean image
            imagelv.paste(pic3, (0, 0), pic3)
            imagelv = ImageTk.PhotoImage(imagelv)
            # Update location
            Label1 = Label(win, image=imagelv, borderwidth=1, relief="solid") # creating a lable
            Label1.grid(row=0, column=int(gridLabel[self.vacuumLocation])) # where the label sits on the screen
            Label1.imagelv = imagelv
            # find next location
            newIndex = self.Location.index(self.vacuumLocation) + 1
            if newIndex == 2:
                newIndex = 0
            # Update next location
            if self.locationCondition[self.Location[newIndex]] == 0:
                Label2 = tkinter.Label(win, image=picc, compound=LEFT, borderwidth=1, relief="solid")
                Label2.grid(row=0, column=int(gridLabel[self.Location[newIndex]]))
                Label2.imagec = picc
            elif self.locationCondition[self.Location[newIndex]] == 1:
                Label2 = tkinter.Label(win, image=picd, compound=LEFT, borderwidth=1, relief="solid")
                Label2.grid(row=0, column=int(gridLabel[self.Location[newIndex]]))
                Label2.imagec = picd
        else:
            # use dirty image
            imagelv = imaged
            # superimpose vacuum and dirty image
            imagelv.paste(pic3, (0, 0), pic3)
            imagelv = ImageTk.PhotoImage(imagelv)
            # Update location
            Label1 = Label(win, image=imagelv, borderwidth=1, relief="solid")
            Label1.grid(row=0, column=int(gridLabel[self.vacuumLocation]))
            Label1.imagelv = imagelv
            # find next location
            newIndex = self.Location.index(self.vacuumLocation) + 1
            if newIndex == 2:
                newIndex = 0
            # Update next location
            if self.locationCondition[self.Location[newIndex]] == 0:
                Label2 = tkinter.Label(win, image=picc, compound=LEFT, borderwidth=1, relief="solid")
                Label2.grid(row=0, column=int(gridLabel[self.Location[newIndex]]))
                Label2.imagec = picc
            elif self.locationCondition[self.Location[newIndex]] == 1:
                Label2 = tkinter.Label(win, image=picd, compound=LEFT, borderwidth=1, relief="solid")
                Label2.grid(row=0, column=int(gridLabel[self.Location[newIndex]]))
                Label2.imagec = picd


class SimpleReflexVacuumAgent(Environment):
    def __init__(self, win, Environment):
        # randomize conditions
        print(Environment.locationCondition)
        print("Vacuum is randomly placed at Location.", Environment.vacuumLocation)
        # and Location is Dirty.
        count = 0
        n = 0
        while count < 2:
            if Environment.locationCondition[Environment.vacuumLocation] == 1:
                Environment.locationCondition[Environment.vacuumLocation] = 0;
                print(Environment.vacuumLocation, "has been Cleaned.")

            else:
                print(Environment.vacuumLocation, " is Clean.")
            newIndex = Environment.Location.index(Environment.vacuumLocation) + 1
            if newIndex == 2:
                newIndex = 0
            Environment.vacuumLocation = Environment.Location[newIndex]
            count += 1

            # done cleaning
        print(Environment.locationCondition)


window = tkinter.Tk() # creates a window

theEnvironment = Environment(window) # reads the environment
theEnvironment.displayEnv(window) # puts the imgs on the window
window.title('Vaccum Cleaner App') # window title
window.geometry("400x300") # window dimentions
window.mainloop() #

window = tkinter.Tk() # creates another window to show environment after cleaning
theVacuum = SimpleReflexVacuumAgent(window, theEnvironment)
theEnvironment.displayEnv(window) # reads parameters of environment
window.title('Vaccum Cleaner App')
window.geometry("400x300")
window.mainloop()







