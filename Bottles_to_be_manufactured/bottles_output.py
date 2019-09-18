#shree

#importing all the neccesary libraries
import tkinter
import pandas as pd
from sklearn import linear_model

#importing the dataset
data = pd.read_csv("modified.csv")
data



#fitting the model in Linear Regession with Multiple variable
reg = linear_model.LinearRegression()
reg.fit(data[['Month','Date','Time']],data.Bottles)
reg.predict([[1,1,1]])

#clicked function
def clicked():
	x = int(entry1.get())
	x1 = int(entry2.get())
	x2 = int(entry3.get())
	if ((x<0 or x>=13) or (x1<0 or x1>=32) or (x2<0 or x2>=24)):
		label5.configure(text="Not valid",fg="red")
	else :
		y = reg.predict([[x,x1,x2]]) 
		y=round(y[0])
		label5.configure(text=y,fg="green")

#GUI for Model

#creating object	
window = tkinter.Tk()
window.config(bg="yellow")
window.title("Bottle Manufacturing Prediction Model")
window.geometry("400x300")

#Label1
label1 = tkinter.Label(window,text="Enter Month : ",font=("Arial",15),bg="yellow")
label1.grid(column=0,row=0)

label2 = tkinter.Label(window,text="Enter Date : ",font=("Arial",15),bg="yellow")
label2.grid(column=0,row=1)

label3 = tkinter.Label(window,text="Enter Time : ",font=("Arial",15),bg="yellow")
label3.grid(column=0,row=2)

#input entry from user
entry1 = tkinter.Entry(window,width=10,)
entry1.grid(column=1,row=0)

entry2 = tkinter.Entry(window,width=10,)
entry2.grid(column=1,row=1)

entry3 = tkinter.Entry(window,width=10,)
entry3.grid(column=1,row=2)

#Enter button
button = tkinter.Button(window,text="Enter",bg="green",fg="black",command=clicked)
button.grid(column=1,row=3)

#label2
label4 = tkinter.Label(window,text="Bottles : ", font=("Arial",15),bg="yellow")
label4.grid(column=0,row=4)

#labbel3
label5 = tkinter.Label(window,text="----",font=("Arial",15),bg="yellow")
label5.grid(column=1,row=4)

#label6 = tkinter.Label(window,text="Developed By : Shubhangi Rokade ",bg="yellow")
#label6.grid(column=1,row=5)

window.mainloop()