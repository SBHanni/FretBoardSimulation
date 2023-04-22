#Import necessry libraries
from tkinter import *
from tkinter import ttk

#Create an instance of tkinter frame or window
window = Tk()

#Set the geometry of tkinter frame
window.geometry("1000x350")
window.title("Fretboard Simulator")

#Create fretboard background
fretboard_image = PhotoImage(file = "guitarneck.png")
fboard = Label(window, i=fretboard_image).grid(row = 1, column = 1, rowspan=6, columnspan=7)

#Create integer variables
note_I   = IntVar()
note_II  = IntVar()
note_III = IntVar()
note_IV  = IntVar()
note_V   = IntVar()
note_VI  = IntVar()

#Create Label for title
program_title = Label(text="Guitar Fretboard Simulator V1.0", font = "Helvetica 18 bold").grid(row = 0, column = 2, columnspan = 4, pady = 15)

#Create Labels for chord and note indicators
chord_label = Label(text="Chord: ", font = "Helvetica 12").grid(row = 7, column = 1, columnspan = 4, pady = 10)
notes_label = Label(text="Notes: ", font = "Helvetica 12").grid(row = 8, column = 1, columnspan = 4, pady = 10)

#Create Radiobuttons for string I
I_Open_String = Radiobutton(window, variable = note_I, value = 0).grid(row=1, column=0, padx = 45, pady = 2)
I_First_Fret  = Radiobutton(window, variable = note_I, value = 1).grid(row=1, column=1, padx = 50, pady = 2)
I_Second_Fret = Radiobutton(window, variable = note_I, value = 2).grid(row=1, column=2, padx = 50, pady = 2)
I_Third_Fret  = Radiobutton(window, variable = note_I, value = 3).grid(row=1, column=3, padx = 50, pady = 2)
I_Fourth_Fret = Radiobutton(window, variable = note_I, value = 4).grid(row=1, column=4, padx = 50, pady = 2)
I_Fifth_Fret  = Radiobutton(window, variable = note_I, value = 5).grid(row=1, column=5, padx = 50, pady = 2)
I_Sixth_Fret  = Radiobutton(window, variable = note_I, value = 6).grid(row=1, column=6, padx = 50, pady = 2)

#Create Radiobuttons for string II
II_Open_String = Radiobutton(window, variable = note_II, value = 0).grid(row=2, column=0, padx = 10, pady = 2)
II_First_Fret  = Radiobutton(window, variable = note_II, value = 1).grid(row=2, column=1, padx = 10, pady = 2)
II_Second_Fret = Radiobutton(window, variable = note_II, value = 2).grid(row=2, column=2, padx = 10, pady = 2)
II_Third_Fret  = Radiobutton(window, variable = note_II, value = 3).grid(row=2, column=3, padx = 10, pady = 2)
II_Fourth_Fret = Radiobutton(window, variable = note_II, value = 4).grid(row=2, column=4, padx = 10, pady = 2)
II_Fifth_Fret  = Radiobutton(window, variable = note_II, value = 5).grid(row=2, column=5, padx = 10, pady = 2)
II_Sixth_Fret  = Radiobutton(window, variable = note_II, value = 6).grid(row=2, column=6, padx = 10, pady = 2)

#Create Radiobuttons for string III
III_Open_String = Radiobutton(window, variable = note_III, value = 0).grid(row=3, column=0, padx = 10, pady = 2)
III_First_Fret  = Radiobutton(window, variable = note_III, value = 1).grid(row=3, column=1, padx = 10, pady = 2)
III_Second_Fret = Radiobutton(window, variable = note_III, value = 2).grid(row=3, column=2, padx = 10, pady = 2)
III_Third_Fret  = Radiobutton(window, variable = note_III, value = 3).grid(row=3, column=3, padx = 10, pady = 2)
III_Fourth_Fret = Radiobutton(window, variable = note_III, value = 4).grid(row=3, column=4, padx = 10, pady = 2)
III_Fifth_Fret  = Radiobutton(window, variable = note_III, value = 5).grid(row=3, column=5, padx = 10, pady = 2)
III_Sixth_Fret  = Radiobutton(window, variable = note_III, value = 6).grid(row=3, column=6, padx = 10, pady = 2)

#Create Radiobuttons for string IV
IV_Open_String = Radiobutton(window, variable = note_IV, value = 0).grid(row=4, column=0, padx = 10, pady = 2)
IV_First_Fret  = Radiobutton(window, variable = note_IV, value = 1).grid(row=4, column=1, padx = 10, pady = 2)
IV_Second_Fret = Radiobutton(window, variable = note_IV, value = 2).grid(row=4, column=2, padx = 10, pady = 2)
IV_Third_Fret  = Radiobutton(window, variable = note_IV, value = 3).grid(row=4, column=3, padx = 10, pady = 2)
IV_Fourth_Fret = Radiobutton(window, variable = note_IV, value = 4).grid(row=4, column=4, padx = 10, pady = 2)
IV_Fifth_Fret  = Radiobutton(window, variable = note_IV, value = 5).grid(row=4, column=5, padx = 10, pady = 2)
IV_Sixth_Fret  = Radiobutton(window, variable = note_IV, value = 6).grid(row=4, column=6, padx = 10, pady = 2)

#Create Radiobuttons for string V
V_Open_String = Radiobutton(window, variable = note_V, value = 0).grid(row=5, column=0, padx = 10, pady = 2)
V_First_Fret  = Radiobutton(window, variable = note_V, value = 1).grid(row=5, column=1, padx = 10, pady = 2)
V_Second_Fret = Radiobutton(window, variable = note_V, value = 2).grid(row=5, column=2, padx = 10, pady = 2)
V_Third_Fret  = Radiobutton(window, variable = note_V, value = 3).grid(row=5, column=3, padx = 10, pady = 2)
V_Fourth_Fret = Radiobutton(window, variable = note_V, value = 4).grid(row=5, column=4, padx = 10, pady = 2)
V_Fifth_Fret  = Radiobutton(window, variable = note_V, value = 5).grid(row=5, column=5, padx = 10, pady = 2)
V_Sixth_Fret  = Radiobutton(window, variable = note_V, value = 6).grid(row=5, column=6, padx = 10, pady = 2)

#Create Radiobuttons for string VI
VI_Open_String = Radiobutton(window, variable = note_VI, value = 0).grid(row=6, column=0, padx = 10, pady = 2)
VI_First_Fret  = Radiobutton(window, variable = note_VI, value = 1).grid(row=6, column=1, padx = 10, pady = 2)
VI_Second_Fret = Radiobutton(window, variable = note_VI, value = 2).grid(row=6, column=2, padx = 10, pady = 2)
VI_Third_Fret  = Radiobutton(window, variable = note_VI, value = 3).grid(row=6, column=3, padx = 10, pady = 2)
VI_Fourth_Fret = Radiobutton(window, variable = note_VI, value = 4).grid(row=6, column=4, padx = 10, pady = 2)
VI_Fifth_Fret  = Radiobutton(window, variable = note_VI, value = 5).grid(row=6, column=5, padx = 10, pady = 2)
VI_Sixth_Fret  = Radiobutton(window, variable = note_VI, value = 6).grid(row=6, column=6, padx = 10, pady = 2)

#Launch GUI
window.mainloop()