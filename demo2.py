from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import Tk, Label, Frame
from PIL import Image, ImageTk
import pyttsx3
import os

root = Tk()
root.title("Text to Voice")
root.geometry("900x500")
root.resizable(False, False)
root.configure(bg="#305065")

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')
    
    def setvoice():
        if gender == "Male":
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
    
    if text.strip():
        if speed == "Fast":
            engine.setProperty("rate", 250)
        elif speed == "Normal":
            engine.setProperty("rate", 150)
        else:
            engine.setProperty("rate", 60)
        setvoice()

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty("voices")

    def setvoice():
        if gender == "Male":
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        
        path = filedialog.askdirectory()
        if path:
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if text.strip():
        if speed == "Fast":
            engine.setProperty("rate", 250)
        elif speed == "Normal":
            engine.setProperty("rate", 150)
        else:
            engine.setProperty("rate", 60)
        setvoice()

############## logo ############################
img = PhotoImage(file="logo.png")
root.iconphoto(False, img)

################top frame ##########################
Top_frame = Frame(root, bg="black", width=900, height=100)
Top_frame.place(x=0, y=0)

################# set image on top frame ######################
img = Image.open("wave.png")
resized_img = img.resize((170, 90))
photo_img = ImageTk.PhotoImage(resized_img)
image_label = Label(root, image=photo_img)
image_label.place(x=10, y=0)

img2 = Image.open("wave.png")
resized_img2 = img2.resize((170, 90))
photo_img2 = ImageTk.PhotoImage(resized_img2)
image_label2 = Label(root, image=photo_img2)
image_label2.place(x=720, y=0)

############ logo image #################
Label(Top_frame, text="TEXT TO SPEECH", font="arial 40 bold", bg="black", fg="white").place(x=220, y=30)

############################### notepad ########################
text_area = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=300)

###################### speed and voice #######################
Label(root, text="VOICE", font="arial 15 bold", bg="#305065", fg="white").place(x=550, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="#305065", fg="white").place(x=750, y=160)

##################### gender variation ##########################
gender_combobox = Combobox(root, values=["Male", "Female"], font="arial 14", state="readonly", width=8)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

########################## speed variation ###############################
speed_combobox = Combobox(root, values=["Fast", "Normal", "Slow"], font="arial 14", state="readonly", width=8)
speed_combobox.place(x=750, y=200)
speed_combobox.set('Normal')

##################### Speak Button ############################
btn = Button(root, text="Speak", width=10, font="arial 14 bold", command=speaknow)
btn.place(x=550, y=280)

#################### Save Button ####################################
save = Button(root, text="Save", width=10, bg="#39c790", font="arial 14 bold", command=download)
save.place(x=750, y=280)

root.mainloop()
