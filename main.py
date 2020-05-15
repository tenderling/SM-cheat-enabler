from tkinter import *
from tkinter import filedialog
import os.path

scfolder = ""

def folderselect():
    global scfolder
    scfolder = filedialog.askdirectory()
    print(scfolder)
    if os.path.isfile(scfolder + "\Survival\Scripts\game\SurvivalGame.lua"):
        lbl.configure(text="Path correct")
    else:
        lbl.configure(text="Path incorrect")

def save():
    cheatenabler(scfolder)
    print('saved')

def cheatenabler(gamefolder):
    if gamefolder == "":
        folderselect()
    commands = open(gamefolder + "\Survival\Scripts\game\SurvivalGame.lua", "r")
    if not os.path.isfile(scfolder + "\Survival\Scripts\game\SurvivalGame.backup"):     
        backup = open(gamefolder + "\Survival\Scripts\game\SurvivalGame.backup", 'tw', encoding='utf-8')
        backup.write(commands.read())
        backup.close()
    x = commands.read().replace("if g_survivalDev then", "if true then", 1)

    enb = open(gamefolder + "\Survival\Scripts\game\SurvivalGame.lua", 'tw', encoding='utf-8')
    enb.write(x)
    enb.close()
    commands.close()
    status.configure(text="Cheats enabled!")

def restore():
    global scfolder
    if scfolder == "":
        folderselect()
    backup = open(scfolder + "\Survival\Scripts\game\SurvivalGame.backup", "r")
    
    rest = open(scfolder + "\Survival\Scripts\game\SurvivalGame.lua", 'tw', encoding='utf-8')
    rest.write(backup.read())
    rest.close()
    backup.close()
    status.configure(text="Cheats disabled")

root = Tk()
root.geometry('300x150')
root.title("SM cheats enabler")
lbl = Label(root, text="Folder not selected")  
lbl.grid(column=0, row=0)  
btn = Button(root, text="Select folder", command=folderselect)
btn.grid(column=1, row=0)
savebtn = Button(root, text="Enable cheats", command=save)
savebtn.grid(column=5, row=1)
restore = Button(root, text="Restore", command=restore)
restore.grid(column=5, row=2)
status = Label(root, text="")  
status.grid(column=0, row=1)  



root.mainloop()