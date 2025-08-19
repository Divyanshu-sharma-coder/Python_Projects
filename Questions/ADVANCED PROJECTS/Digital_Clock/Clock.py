

# Make A digital Clock with Date And Time

# Caution : Code is only runnable in PC's


from tkinter import Label, Tk
import time

# Create The main window
root = Tk()
root.title("Digital Clock With Date")
root.geometry("400x200")
root.resizable(True, True)
root.configure(bg="black")

# Create Label For time and Date
time_label = Label(root, font=("Arial", 40, "bold"), bg="black", fg="white")
time_label.pack(pady=10)

date_label = Label(root, font=("Arial", 20, "bold"), bg="black", fg="white")
date_label.pack()

# Function To update Time and Date
def update_time():
    current_time = time.strftime("%I:%M:%S %p")  # Added %p for AM/PM
    current_date = time.strftime("%A, %d, %B, %Y")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)

# Start the Clock update
update_time()

# Run The tkinter loop
root.mainloop()
