import tkinter as tk
from tkinter import messagebox
def add_text():
    new_text = entry.get()
    new_text = new_text.replace(" ","")
    if new_text.isnumeric() and 0<int(new_text)<=100:
    	label0.config(text=label0.cget("text") + " " + new_text)
    	entry.delete(0, tk.END)  # Clear the entry widget
    	add_button.config(state = tk.DISABLED)
    	entry.config(state = tk.DISABLED)
    	checkPlag.config(state = tk.NORMAL)
    else:
    	m = messagebox.showerror("Error","Input an integer between 1 to 100.")
def clear_text():
    label0.config(text = "python3 checkPlagForAll.py")
    textWidgetResult.config(state=tk.NORMAL)
    textWidgetResult.delete(1.0,tk.END)
    textWidgetResult.config(state=tk.DISABLED)
    entry.delete(0,tk.END)
    add_button.config(state = tk.NORMAL)
    entry.config(state = tk.NORMAL)
    checkPlag.config(state = tk.NORMAL)
    checkPlag.config(state = tk.DISABLED)
def checkPlagfn():
	import subprocess
	new_text = label0.cget("text")
	cmd = new_text.split()
	try:
		# Run the 'python3' command
		result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		# Check if the command was successful
		if result.returncode == 0:
		    # Print the standard output (Python 3 version information)
		    print("Job Done!")
		    res = (result.stdout)
		    textWidgetResult.config(state=tk.NORMAL)
		    textWidgetResult.insert(tk.END,res)
		    textWidgetResult.config(state=tk.DISABLED)
		    checkPlag.config(state = tk.DISABLED)
		    #messagebox.showinfo("Job Complete", "The results are printed in the console.")
		else:
		    # Print the error message if the command failed
		    print("Error:")
		    print(result.stderr)
	except FileNotFoundError:
		print("Contact the owner and try later.")
	
# Create the main window
root = tk.Tk()
root.title("Plaganotex")
root.configure(bg = "#ffe89c")
#root.geometry("350x150")
root.resizable(width=False, height=False)

#create two frames
topFrame = tk.Frame(root,bg = "#343630")
bottomFrame = tk.Frame(root,bg = "#343630")

# Create a label widget for command line
label0 = tk.Label(topFrame, text="python3 checkPlagForAll.py")
label0.grid_forget()	
# create a label widget for plag percentage
label1 = tk.Label(topFrame, text = "Release plag (1 - 100)%",foreground="#ffffff", background="#343630",font = ("Courier", 11, "bold"))

# create a text widget for output of console
textWidgetResult = tk.Text(bottomFrame , state = tk.DISABLED, wrap=tk.WORD, foreground="#a2ff00", background="#243606",font = ("Courier", 11, "bold"))

#create a scroll bar for textWidget
scrollbarResult = tk.Scrollbar(bottomFrame, command = textWidgetResult.yview)
textWidgetResult.config(yscrollcommand=scrollbarResult.set)

# Create an entry widget for input plag percentage
entry = tk.Entry(topFrame,foreground="#000111", background="#ffffff",font = ("Courier", 11, "bold"))	

# Create a button widget to add text
add_button = tk.Button(topFrame, text="Add command     ", command=add_text,foreground="#ffffff", background="#277d2a", borderwidth=0, relief="solid",font = ("Courier", 11, "bold"),anchor="center", justify="center")

# Create a button widget to clear text
clear_button = tk.Button(topFrame, text="Clear command   ", command=clear_text,foreground="#ffffff", background="#c71414", borderwidth=0, relief="solid",font = ("Courier", 11, "bold"),anchor="center", justify="center")

checkPlag = tk.Button(bottomFrame, text = "Check plagiarism", command = checkPlagfn,state = tk.DISABLED, bg = "#b85600", fg = "#ffffff", borderwidth = 0, relief="solid",font = ("Courier", 11, "bold"),anchor="center", justify="center")
# Start the tkinter main loop

#postions of widgets
label1.pack(side = tk.LEFT, padx=5, pady = 5)
entry.pack(side = tk.LEFT, padx=5, pady = 5)
add_button.pack(side = tk.LEFT, padx=5, pady = 5)
checkPlag.pack(side = tk.LEFT, padx=5, pady = 5)
clear_button.pack(side = tk.LEFT, padx=5, pady = 5)
textWidgetResult.pack(side = tk.LEFT, padx=5, pady = 5)
scrollbarResult.pack(side = tk.LEFT, padx=5, pady = 5,fill = tk.Y)

topFrame.pack(fill = tk.BOTH)
bottomFrame.pack()



root.mainloop()
