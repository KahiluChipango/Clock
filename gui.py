import tkinter as tk
from tkinter import ttk
from clocklogic import ClockLogic

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Digital Clock")
        self.root.geometry("650x500")
        self.root.configure(bg='#1a1a1a')
        self.root.resizable(True, True)
        
        # Configure modern styling
        self.setup_styles()
        
        self.logic = ClockLogic()
        
        # Main container
        self.main_frame = tk.Frame(root, bg='#1a1a1a')
        self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header
        self.create_header()
        
        # Time display
        self.create_time_display()
        
        # Control panel
        self.create_control_panel()
        
        # Status bar
        self.create_status_bar()
        
        # Start updating
        self.update_clock()

    def setup_styles(self):
        """Configure modern styling for ttk widgets"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure button style
        style.configure('Modern.TButton',
                       background='#4a4a4a',
                       foreground='white',
                       borderwidth=1,
                       focuscolor='none')
        style.map('Modern.TButton',
                 background=[('active', '#5a5a5a'),
                           ('pressed', '#3a3a3a')])
        
        # Configure frame style
        style.configure('Card.TFrame',
                       background='#2a2a2a',
                       relief='flat',
                       borderwidth=1)

    def create_header(self):
        """Create the header section"""
        header_frame = tk.Frame(self.main_frame, bg='#1a1a1a')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame, 
                              text="⏰ Digital Clock Controller",
                              font=("Segoe UI", 16, "bold"),
                              fg='#ffffff',
                              bg='#1a1a1a')
        title_label.pack()

    def create_time_display(self):
        """Create the time display section"""
        display_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        display_frame.pack(fill='x', pady=(0, 20), padx=10)
        
        # Time display with modern styling
        self.time_label = tk.Label(display_frame, 
                                  font=("Consolas", 36, "bold"),
                                  fg='#00ff88',
                                  bg='#2a2a2a',
                                  relief='flat')
        self.time_label.pack(pady=15)
        
        self.date_label = tk.Label(display_frame,
                                  font=("Segoe UI", 14),
                                  fg='#cccccc',
                                  bg='#2a2a2a')
        self.date_label.pack(pady=(0, 15))

    def create_control_panel(self):
        """Create the enhanced control panel"""
        control_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        control_frame.pack(fill='both', expand=True, padx=10)
        
        # Title for control panel
        control_title = tk.Label(control_frame,
                                text="Time Adjustments",
                                font=("Segoe UI", 12, "bold"),
                                fg='#ffffff',
                                bg='#2a2a2a')
        control_title.pack(pady=(15, 10))
        
        # Create organized control sections
        self.create_time_controls(control_frame)
        self.create_date_controls(control_frame)
        self.create_action_controls(control_frame)

    def create_time_controls(self, parent):
        """Create time adjustment controls"""
        time_frame = tk.Frame(parent, bg='#2a2a2a')
        time_frame.pack(pady=5, padx=20, fill='x')
        
        time_label = tk.Label(time_frame,
                             text="⏱️ Time Controls",
                             font=("Segoe UI", 10, "bold"),
                             fg='#aaaaaa',
                             bg='#2a2a2a')
        time_label.pack(anchor='w', pady=(0, 5))
        
        time_controls = tk.Frame(time_frame, bg='#2a2a2a')
        time_controls.pack(fill='x')
        
        time_adjustments = [
            ("Hours", [
                ("−1h", lambda: self.logic.adjust(hours=-1)),
                ("+1h", lambda: self.logic.adjust(hours=1))
            ]),
            ("Minutes", [
                ("−1m", lambda: self.logic.adjust(minutes=-1)),
                ("+1m", lambda: self.logic.adjust(minutes=1))
            ]),
            ("Seconds", [
                ("−1s", lambda: self.logic.adjust(seconds=-1)),
                ("+1s", lambda: self.logic.adjust(seconds=1))
            ])
        ]
        
        for i, (label, buttons) in enumerate(time_adjustments):
            col_frame = tk.Frame(time_controls, bg='#2a2a2a')
            col_frame.pack(side='left', fill='both', expand=True, padx=5)
            
            tk.Label(col_frame, text=label, font=("Segoe UI", 9),
                    fg='#cccccc', bg='#2a2a2a').pack()
            
            btn_frame = tk.Frame(col_frame, bg='#2a2a2a')
            btn_frame.pack(pady=2)
            
            for btn_text, cmd in buttons:
                ttk.Button(btn_frame, text=btn_text, command=cmd,
                          style='Modern.TButton', width=6).pack(side='left', padx=1)

    def create_date_controls(self, parent):
        """Create date adjustment controls"""
        date_frame = tk.Frame(parent, bg='#2a2a2a')
        date_frame.pack(pady=15, padx=20, fill='x')
        
        date_label = tk.Label(date_frame,
                             text="📅 Date Controls",
                             font=("Segoe UI", 10, "bold"),
                             fg='#aaaaaa',
                             bg='#2a2a2a')
        date_label.pack(anchor='w', pady=(0, 5))
        
        date_controls = tk.Frame(date_frame, bg='#2a2a2a')
        date_controls.pack(fill='x')
        
        date_adjustments = [
            ("Years", [
                ("−1y", lambda: self.logic.adjust(years=-1)),
                ("+1y", lambda: self.logic.adjust(years=1))
            ]),
            ("Months", [
                ("−1M", lambda: self.logic.adjust(months=-1)),
                ("+1M", lambda: self.logic.adjust(months=1))
            ]),
            ("Days", [
                ("−1d", lambda: self.logic.adjust(days=-1)),
                ("+1d", lambda: self.logic.adjust(days=1)),
                ("−1w", lambda: self.logic.adjust(days=-7)),
                ("+1w", lambda: self.logic.adjust(days=7))
            ])
        ]
        
        for i, (label, buttons) in enumerate(date_adjustments):
            col_frame = tk.Frame(date_controls, bg='#2a2a2a')
            col_frame.pack(side='left', fill='both', expand=True, padx=5)
            
            tk.Label(col_frame, text=label, font=("Segoe UI", 9),
                    fg='#cccccc', bg='#2a2a2a').pack()
            
            btn_frame = tk.Frame(col_frame, bg='#2a2a2a')
            btn_frame.pack(pady=2)
            
            for btn_text, cmd in buttons:
                ttk.Button(btn_frame, text=btn_text, command=cmd,
                          style='Modern.TButton', width=6).pack(side='left', padx=1)

    def create_action_controls(self, parent):
        """Create action controls"""
        action_frame = tk.Frame(parent, bg='#2a2a2a')
        action_frame.pack(pady=15, padx=20)
        
        # Reset button with emphasis
        reset_btn = tk.Button(action_frame,
                             text="🔄 Reset to Current Time",
                             font=("Segoe UI", 11, "bold"),
                             bg='#ff6b6b',
                             fg='white',
                             activebackground='#ff5252',
                             activeforeground='white',
                             relief='flat',
                             padx=20,
                             pady=8,
                             command=self.logic.reset_time)
        reset_btn.pack()

    def create_status_bar(self):
        """Create status bar"""
        self.status_frame = tk.Frame(self.main_frame, bg='#1a1a1a', height=30)
        self.status_frame.pack(fill='x', side='bottom')
        self.status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(self.status_frame,
                                    text="Clock running normally",
                                    font=("Segoe UI", 9),
                                    fg='#888888',
                                    bg='#1a1a1a')
        self.status_label.pack(side='left', pady=5)
        
        # Add adjustment indicator
        self.adjustment_label = tk.Label(self.status_frame,
                                        text="",
                                        font=("Segoe UI", 9),
                                        fg='#00ff88',
                                        bg='#1a1a1a')
        self.adjustment_label.pack(side='right', pady=5)

    def update_status(self):
        """Update status information"""
        try:
            # Check if time has been adjusted (you might need to add this to ClockLogic)
            if hasattr(self.logic, 'is_adjusted') and self.logic.is_adjusted():
                self.adjustment_label.config(text="⚠️ Time adjusted")
            else:
                self.adjustment_label.config(text="")
        except:
            pass

    def update_clock(self):
        """Update the clock display"""
        self.time_label.config(text=self.logic.get_time_str())
        self.date_label.config(text=self.logic.get_date_str())
        self.update_status()
        self.logic.tick()
        self.root.after(1000, self.update_clock)

def run_app():
    root = tk.Tk()
    
    # Center the window on screen
    root.update_idletasks()
    width = 650
    height = 500
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    app = DigitalClock(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()