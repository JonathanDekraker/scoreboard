import tkinter as tk
import time
from tkinter import filedialog
from tkinter import messagebox

from gui import create_canvas

class ControllerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Controller GUI")

        self.canvas = create_canvas()
        self.away_score = tk.StringVar()
        self.home_score = tk.StringVar()
        self.time = tk.StringVar()
        self.penalty = tk.StringVar()
        self.timer_running = False
        self.start_time = 0

        self.create_widgets()

    def create_widgets(self):
        # Labels
        away_score_label = tk.Label(self, text="Away Score:")
        away_score_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        home_score_label = tk.Label(self, text="Home Score:")
        home_score_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        time_label = tk.Label(self, text="Time:")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        penalty_label = tk.Label(self, text="Penalty:")
        penalty_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

        # Entry fields
        away_score_entry = tk.Entry(self, textvariable=self.away_score)
        away_score_entry.grid(row=0, column=1, padx=10, pady=5)

        home_score_entry = tk.Entry(self, textvariable=self.home_score)
        home_score_entry.grid(row=1, column=1, padx=10, pady=5)

        time_entry = tk.Entry(self, textvariable=self.time)
        time_entry.grid(row=2, column=1, padx=10, pady=5)

        penalty_entry = tk.Entry(self, textvariable=self.penalty)
        penalty_entry.grid(row=3, column=1, padx=10, pady=5)
        
        # Buttons
        update_button = tk.Button(self, text="Update", command=self.update_gui)
        update_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

        start_stop_button = tk.Button(self, text="Start/Stop", command=self.start_stop_timer)
        start_stop_button.grid(row=5, column=0, padx=10, pady=5, columnspan=2)

    def update_gui(self):
        try:
            self.canvas.itemconfigure("away_score", text=self.away_score.get())
            self.canvas.itemconfigure("home_score", text=self.home_score.get())
            self.canvas.itemconfigure("time", text=self.time.get())
            self.canvas.itemconfigure("penalties", text=self.penalty.get())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update GUI: {e}")

    def start_stop_timer(self):
        if self.timer_running:
            self.timer_running = False
        else:
            self.timer_running = True
            self.start_time = time.time()
            self.update_timer()

    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            self.time.set(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
            self.after(1000, self.update_timer)

# Create the ControllerGUI instance
controller_gui = ControllerGUI()
controller_gui.mainloop()
