import tkinter as tk
from tkinter.ttk import Label

root = tk.Tk()
root.geometry('200x120')
root.resizable(False, False)
root.title('Listbox')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

langs = ('Op1', 'Op2', 'Op3', 'Op4', 'Op5',
         'Op6')

langs_var = tk.StringVar(value=langs)

listbox = tk.Listbox(
    root,
    listvariable=langs_var,
    height=6,
    selectmode='extended')

listbox.grid(
    column=0,
    row=0,
    sticky='nwes'
)


def items_selected(event):
    selected_indices = listbox.curselection()
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    label = Label(root, text=f'You have selected: {selected_langs}').grid(column=0,row=1,sticky='nwes')

listbox.bind('<<ListboxSelect>>', items_selected)

root.mainloop()