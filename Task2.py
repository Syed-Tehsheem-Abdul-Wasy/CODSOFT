import tkinter as tk
# Function to perform calculation based on operation choice
def Calculater():
    try:
        Num1 = float(Enter_Num1.get())
        Num2 = float(Enter_Num2.get())
        Operation = Operation_Var.get()      
        if Operation == '+':
            Result.set(Num1 + Num2)
        elif Operation == '-':
            Result.set(Num1 - Num2)
        elif Operation == '*':
            Result.set(Num1 * Num2)
        elif Operation == '/':
            if Num2 != 0:
                Result.set(Num1 / Num2)
            else:
                Result.set("Cannot divide by zero!")
    except ValueError:
        Result.set("Invalid Input")
# Create main tkinter window
root = tk.Tk()
root.title("Simple Calculator")
# Number input fields
Label_Num1 = tk.Label(root, text="Enter First Number:")
Label_Num1.pack()
Enter_Num1 = tk.Entry(root)
Enter_Num1.pack()
Label_Num2 = tk.Label(root, text="Enter Second Number:")
Label_Num2.pack()
Enter_Num2 = tk.Entry(root)
Enter_Num2.pack()
# Operation choice
Operation_Var = tk.StringVar()
Operations = ['+', '-', '*', '/']
for Operation in Operations:
    rb = tk.Radiobutton(root, text=Operation, variable=Operation_Var, value=Operation)
    rb.pack()
# Calculate button
Calculate_Button = tk.Button(root, text="Calculate", command=Calculater)
Calculate_Button.pack()
# Result display
Result = tk.StringVar()
Result_Label = tk.Label(root, textvariable=Result)
Result_Label.pack()

# Start the main event loop
root.mainloop()