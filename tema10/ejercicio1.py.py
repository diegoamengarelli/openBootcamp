import tkinter as tk

app = tk.Tk()
app.geometry('200x100')

default = 0
radioValue = tk.IntVar(value=default)

rdioOne = tk.Radiobutton(app, text='Option 1',
                         variable=radioValue, value=1)
rdioTwo = tk.Radiobutton(app, text='Option 2',
                         variable=radioValue, value=2)
rdioThree = tk.Radiobutton(app, text='Option 3',
                           variable=radioValue, value=3)

rdioOne.grid(column=0, row=0, sticky="W")
rdioTwo.grid(column=0, row=1, sticky="W")
rdioThree.grid(column=0, row=2, sticky="W")

labelValue = tk.Label(app, textvariable=radioValue)
labelValue.grid(column=2, row=0, sticky="E", padx=40)

def refresh():
    radioValue.set(default)

def exit():
    app.destroy()

refreshButton = tk.Button(app, text = "refresh", command = refresh)
refreshButton.grid(column=2, row=1, sticky="E", padx=40)

exitButton = tk.Button(app, text="exit", command=exit)
exitButton.grid(column=2, row=2, sticky="E", padx=40)

app.mainloop()