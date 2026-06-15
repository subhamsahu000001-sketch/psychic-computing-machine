import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())

        if height <= 0 or weight <= 0:
            messagebox.showerror("Invalid Input", "Height and Weight must be positive number!")
            return
        
        bmi = weight / (height/100)**2

        if bmi < 18.5 :
            category = "Underweight"
        elif 18.5 <= bmi <= 24.9 :
            category = "Normal weight"
        elif 25 <= bmi <= 29.9 :
            category = "Overweight"
        else:
            category = "Obese"
        label_result.config(text = f"BMI; {bmi:.2f} {category}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for height and weight.")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x300")

# Height input
label_height = tk.Label(root, text = "Enter Heiglt (cm):")
label_height.pack(pady = 5)
entry_height = tk.Entry(root)
entry_height.pack(pady = 5)

# Weight input
label_weight = tk.Label(root, text = "Enter Weight (kg):")
label_weight.pack(pady = 5)
entry_weight = tk.Entry(root)
entry_weight.pack(pady = 5)

btn_calculate = tk.Button(root, text = "Calculate BMI", command = calculate_bmi)
btn_calculate.pack(pady = 10)

# Result lable
label_result = tk.Label(root, text = "", font = ("Arial", 12, "bold"))
label_result.pack(pady = 10)

root.mainloop()

