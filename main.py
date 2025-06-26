if __name__ == "__main__":
    from gui import run_app
    run_app()
class ClockLogic:
    def __init__(self):
        self.adjusted_time = datetime.now()

    def adjust(self, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
        dt = self.adjusted_time
        year = dt.year + years
        month = dt.month + months
        while month > 12:
            month -= 12
            year += 1
        while month < 1:
            month += 12
            year -= 1
        day = min(dt.day, calendar.monthrange(year, month)[1])
        try:
            dt = dt.replace(year=year, month=month, day=day)
        except ValueError:
            dt = dt.replace(year=year, month=month, day=28)
        dt += timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        self.adjusted_time = dt

    def reset_time(self):
        self.adjusted_time = datetime.now()

    def tick(self):
        self.adjusted_time += timedelta(seconds=1)

    def get_time_str(self):
        return self.adjusted_time.strftime("%H:%M:%S")

    def get_date_str(self):
        return self.adjusted_time.strftime("Week %U | %A, %d %B %Y")
        return self.adjusted_time.strftime("Week %U | %A, %d %B %Y")

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Fully Adjustable Digital Clock")
        self.root.geometry("500x400")

        self.logic = ClockLogic()

        # Time display
        self.time_label = tk.Label(root, font=("Helvetica", 32))
        self.time_label.pack(pady=10)

        self.date_label = tk.Label(root, font=("Helvetica", 18))
        self.date_label.pack(pady=5)

        # Adjustment buttons
        self.build_controls()

        # Start updating
        self.update_clock()

    def build_controls(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        adjustments = [
            ("+Year", lambda: self.logic.adjust(years=1)),
            ("-Year", lambda: self.logic.adjust(years=-1)),
            ("+Month", lambda: self.logic.adjust(months=1)),
            ("-Month", lambda: self.logic.adjust(months=-1)),
            ("+Week", lambda: self.logic.adjust(days=7)),
            ("-Week", lambda: self.logic.adjust(days=-7)),
            ("+Day", lambda: self.logic.adjust(days=1)),
            ("-Day", lambda: self.logic.adjust(days=-1)),
            ("+Hour", lambda: self.logic.adjust(hours=1)),
            ("-Hour", lambda: self.logic.adjust(hours=-1)),
            ("+Min", lambda: self.logic.adjust(minutes=1)),
            ("-Min", lambda: self.logic.adjust(minutes=-1)),
            ("+Sec", lambda: self.logic.adjust(seconds=1)),
            ("-Sec", lambda: self.logic.adjust(seconds=-1)),
            ("Reset", self.logic.reset_time)
        ]

        for i, (text, cmd) in enumerate(adjustments):
            btn = tk.Button(frame, text=text, width=8, command=cmd)
            btn.grid(row=i//4, column=i%4, padx=4, pady=4)

    def update_clock(self):
        self.time_label.config(text=self.logic.get_time_str())
        self.date_label.config(text=self.logic.get_date_str())
        self.logic.tick()
        self.root.after(1000, self.update_clock)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClock(root)
    root.mainloop()
    app = DigitalClock(root)
    root.mainloop()
