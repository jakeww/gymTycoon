import tkinter as tk
from tkinter import messagebox

class GymTycoon:
    def __init__(self, root):
        self.root = root
        self.root.title("Gym Tycoon Builder")

        self.balance = 1000
        self.gym_members = 0

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.balance_label = tk.Label(self.frame, text=f"Balance: ${self.balance}", font=("Arial", 16))
        self.balance_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self.members_label = tk.Label(self.frame, text=f"Members: {self.gym_members}", font=("Arial", 16))
        self.members_label.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        self.build_button = tk.Button(self.frame, text="Build", font=("Arial", 16), command=self.build_gym)
        self.build_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.advertise_button = tk.Button(self.frame, text="Advertise", font=("Arial", 16), command=self.advertise_gym)
        self.advertise_button.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    def build_gym(self):
        if self.balance >= 500:
            self.balance -= 500
            self.gym_members += 5
            self.update_labels()
        else:
            messagebox.showerror("Error", "Not enough money to build a gym!")

    def advertise_gym(self):
        if self.balance >= 200:
            self.balance -= 200
            self.gym_members += 2
            self.update_labels()
        else:
            messagebox.showerror("Error", "Not enough money to advertise your gym!")

    def update_labels(self):
        self.balance_label.config(text=f"Balance: ${self.balance}")
        self.members_label.config(text=f"Members: {self.gym_members}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GymTycoon(root)
    root.mainloop()
