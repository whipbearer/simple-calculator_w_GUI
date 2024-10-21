import customtkinter

#CALCULATION
def perform_calculation():
    input1 = float(entry_1.get())
    input2 = float(entry_2.get())
    operation = optionmenu_1.get()
    
    if operation == "*":
        result = input1 * input2
    elif operation == "÷":
        result = input1 / input2
    elif operation == "+":
        result = input1 + input2
    elif operation == "-":
        result = input1 - input2
    else:
        result = "Invalid operation"
    
    result_label.configure(text = f"Answer: {result}")

#CONFIGURING
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("800x350")
app.title("Noah Yonas simple calculator")

frame = customtkinter.CTkFrame(master = app)
frame.grid(pady=20, padx=60, sticky="nsew")

#TITLE OF APP
label = customtkinter.CTkLabel(master = frame, text = "Calculation", font=("Comfortaa", 27))
label.grid(row=0, column=0, columnspan=3, pady=12, padx=10)

#SUBHEADING
label = customtkinter.CTkLabel(master = frame, text = "Pick which operation you would like to do", font=("Roboto", 17))
label.grid(row=1, column=1, pady=12, padx=10)

#USER INPUTS
entry_1 = customtkinter.CTkEntry(master=frame, placeholder_text="Input 1")
entry_1.grid(row=2, column=0, padx=10, pady=12)

optionmenu_1 = customtkinter.CTkOptionMenu(frame, values=["*", "÷", "+", "-"])
optionmenu_1.grid(row=2, column=1, padx=10, pady=12)
optionmenu_1.set("sign")

entry_2 = customtkinter.CTkEntry(master=frame, placeholder_text="Input 2")
entry_2.grid(row=2, column=2, padx=10, pady=12)

# ANSWER BUTTON
calculate_button = customtkinter.CTkButton(master=frame, text="Calculate", command=perform_calculation)
calculate_button.grid(row=3, column=0, columnspan=3, pady=10)

# Label to display result
result_label = customtkinter.CTkLabel(master=frame, text="Result: ", font=("Roboto", 17))
result_label.grid(row=4, column=0, columnspan=3, pady=12, padx=10)

app.mainloop()