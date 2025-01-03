__version__="0.1.2"
import tkinter
import customtkinter
from blockchain import exchangerates as ex


#Function that takes the dollar entry input to convert to bitcoin
def button_function():
    global label
    entryState = entry.get()
    entryState1 = entry1.get()
    a = float(entryState)
    b = float(entryState1)
#this will show the entry based on proper order for percent negative or positive
    c = b - a

    if a > b:  # if a is greater than b then to get to b your result will be negative.
        cc = f"{c:.8f}"
        d = c / a
        e = d * 100
        ee = f"{e:.2f}"
        label.configure(text=f"Diff: {cc}")
        label2.configure(text=f"% Diff: {ee}")
    elif a < b:
        cc = f"{c:.8f}"
        d = c / a
        e = d * 100
        ee = f"{e:.2f}"
        label.configure(text=f"Diff: {cc}")
        label2.configure(text=f"% Diff: {ee}")
    elif a == b:
        label2.configure(text=f"Results: inconclusive")
    else:
        pass
customtkinter.set_appearance_mode("dark")#.set_default_color_theme("green") 
#Modes: system (default), light, dark
#Themes: blue (default), dark-blue, green

app = customtkinter.CTk() #create CTK window like you do with the Tk window
app.geometry("400x350")
app.title("Bitcoin Percent Difference App")

#creates a frame effect in background
frame1 = customtkinter.CTkFrame(master = app)
frame1.pack(pady=15, padx=25, expand=False) #master or placement is the "app" defined

#Bitcoin Price Tracker
ticker = ex.get_ticker()
for k in ticker:
    if k == "USD":
        btcPrice = (ticker[k].p15min)

#Bitcoin Label for the current interface showing
label1 = customtkinter.CTkLabel(master=frame1, justify=tkinter.LEFT,text=f'''
    Bitcoin
${btcPrice}''')
label1.pack(pady=10, padx=10)

#Entry box for the conversion
entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter 1st Number")
entry.pack(padx=25, pady=10)
entry1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter 2nd number")
entry1.pack(padx=25, pady=10)



#Dropdown menu Next to entry box for currency conversion
#???Need to make this drop menu smaller and adjacent to the left of the entry box. Default USD.
#dropMenu1 = customtkinter.CTkOptionMenu(frame1, values=["USD", "CAD", "JPY", "GBP"])
#dropMenu1.pack(padx=10, pady=10)
#dropMenu1.set("Fiat Type")

#Use CTKButton instead of tkinter Button
#used pack to keep button in place instead of using place which lets it move with window
button = customtkinter.CTkButton(master=frame1, text="Calculate", command=button_function).pack(padx=25, pady=10)

#Function to delete last result
def myDelete():
    label.configure(text="")
    label2.configure(text="")

#button to delete the label of result
dbutton = customtkinter.CTkButton(master=frame1, text="Delete", command=myDelete).pack(padx=25, pady=1)

#widget to create placement for the results
label = customtkinter.CTkLabel(master=frame1, text="")
label.pack()
label2 = customtkinter.CTkLabel(master=frame1, text="")
label2.pack()
app.mainloop()