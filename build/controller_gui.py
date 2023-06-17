import tkinter as tk
from tkinter import messagebox
import gui


class ControllerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Controller GUI")

        self.canvas = gui.create_canvas()
        self.away_score = tk.StringVar(value="0")
        self.home_score = tk.StringVar(value="0")
        self.time = tk.StringVar(value="00:00")
        self.penalty_minutes = tk.StringVar(value="0")
        self.penalty_string = tk.StringVar(value="")
        self.timer_running = False
        self.penalty_timer_running = False
        self.start_time = 0
        self.penalty_start_time = 0
        self.is_home = tk.BooleanVar(value=True)

        self.create_widgets()

    def create_widgets(self):
        # Labels
        away_score_label = tk.Label(self, text="Away Score:")
        away_score_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        home_score_label = tk.Label(self, text="Home Score:")
        home_score_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        time_label = tk.Label(self, text="Time:")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        penalty_minutes_label = tk.Label(self, text="Penalty Minutes:")
        penalty_minutes_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

        penalty_string_label = tk.Label(self, text="Penalty String:")
        penalty_string_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

        # Entry fields
        away_score_entry = tk.Entry(self, textvariable=self.away_score)
        away_score_entry.grid(row=0, column=1, padx=10, pady=5)

        home_score_entry = tk.Entry(self, textvariable=self.home_score)
        home_score_entry.grid(row=1, column=1, padx=10, pady=5)

        time_entry = TimeEntry(self, textvariable=self.time)
        time_entry.grid(row=2, column=1, padx=10, pady=5)

        penalty_minutes_entry = TimeEntry(self, textvariable=self.penalty_minutes)
        penalty_minutes_entry.grid(row=3, column=1, padx=10, pady=5)

        penalty_string_entry = tk.Entry(self, textvariable=self.penalty_string)
        penalty_string_entry.grid(row=4, column=1, padx=10, pady=5)

        # Checkboxes
        home_checkbox = tk.Checkbutton(self, text="Home", variable=self.is_home)
        home_checkbox.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

        away_checkbox = tk.Checkbutton(self, text="Away", variable=self.is_home, offvalue=True, onvalue=False)
        away_checkbox.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

        # Buttons
        start_stop_button = tk.Button(self, text="Start / Stop", command=self.start_stop_timer)
        start_stop_button.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

        update_button = tk.Button(self, text="Update", command=self.update_gui)
        update_button.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

        # Penalty display
        penalty_display_label = tk.Label(self, text="Penalty Display:")
        penalty_display_label.grid(row=8, column=0, padx=10, pady=5, sticky=tk.W)

        self.penalty_textbox = tk.Text(self, height=6, width=30)
        self.penalty_textbox.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

    def update_gui(self):
        try:
            self.canvas.itemconfigure("away_score", text=self.away_score.get())
            self.canvas.itemconfigure("home_score", text=self.home_score.get())
            self.canvas.itemconfigure("time", text=self.time.get())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update GUI: {e}")

        self.canvas.update_idletasks()

        # Display penalty and penalty minutes in the penalty display area
        penalty_display = self.penalty_string.get()
        penalty_minutes_display = self.penalty_minutes.get()
        self.penalty_textbox.delete(1.0, tk.END)
        self.penalty_textbox.insert(tk.END, f"Penalty: {penalty_display}\nPenalty Minutes: {penalty_minutes_display}")

    def start_stop_timer(self):
        if not self.timer_running:
            self.start_time = self.get_total_seconds(self.time.get())
            if self.start_time >= 0:
                self.timer_running = True
                self.update_timer()
        else:
            self.timer_running = False

        if not self.penalty_timer_running:
            self.penalty_start_time = self.get_total_seconds(self.penalty_minutes.get())
            if self.penalty_start_time >= 0:
                self.penalty_timer_running = True
                self.update_penalty_timer()
        else:
            self.penalty_timer_running = False

    def update_timer(self):
        if self.timer_running and self.start_time >= 0:
            minutes = self.start_time // 60
            seconds = self.start_time % 60
            time_str = f"{minutes:02d}:{seconds:02d}"
            self.time.set(time_str)

            if self.start_time > 0:
                self.start_time -= 1
                self.after(1000, self.update_timer)
            else:
                self.timer_running = False

    def update_penalty_timer(self):
        if self.penalty_timer_running and self.penalty_start_time >= 0:
            minutes = self.penalty_start_time // 60
            seconds = self.penalty_start_time % 60
            penalty_time_str = f"{minutes:02d}:{seconds:02d}"
            self.penalty_minutes.set(penalty_time_str)

            if self.penalty_start_time > 0:
                self.penalty_start_time -= 1
                self.after(1000, self.update_penalty_timer)
            else:
                self.penalty_timer_running = False

    def get_total_seconds(self, time_str):
        try:
            minutes, *seconds = time_str.split(":")
            minutes = int(minutes)
            if seconds:
                seconds = int(seconds[0])
            else:
                seconds = 0
            return minutes * 60 + seconds
        except ValueError:
            messagebox.showerror("Error", "Invalid time format.")
            return -1


class TimeEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = kwargs.get("textvariable")
        self.var.trace_add("write", self.validate_time_entry)

        super().__init__(master, **kwargs)

    def validate_time_entry(self, *args):
        new_value = self.var.get()
        if new_value == "":
            return True

        try:
            minutes, seconds = new_value.split(":")
            if len(minutes) > 2 or len(seconds) > 2:
                return False

            minutes = int(minutes)
            seconds = int(seconds)

            if minutes < 0 or seconds < 0 or seconds >= 60:
                return False
        except ValueError:
            return False

        return True



# Create the ControllerGUI instance
controller_gui = ControllerGUI()
controller_gui.mainloop()
