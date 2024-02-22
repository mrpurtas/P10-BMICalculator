from tkinter import *

def calculate_bmi():
    try:
        height=float(height_entry.get())/100
        weight=float(weight_entry.get())
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            status = "Underweight: Let's gain strength!"
        elif 18.5<= bmi <= 24.9:
            status = "Normal: Great shape, keep it up!"
        elif 25 <= bmi <= 29.9:
            status= "Overweight: Time for healthier choices!"
        else:
            status = "You're a motherfucker OBESE"
        bmi_result_label.config(text=f"BMI: {bmi:.2f} - Status: {status}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=200)

Label(window, text="Height (cm):").grid(row=0, column=0, padx=10, pady=10)
height_entry = Entry(window)
height_entry.grid(row=0, column=1, padx=10, pady=10)

Label(window, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=10)
weight_entry = Entry(window)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = Button(window, text="Calculate", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

bmi_result_label = Label(window, text="BMI:")
bmi_result_label.grid(row=3, column=0, columnspan=2)

window.mainloop()