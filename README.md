#  Adjustable Digital Clock with Python (Tkinter)

A fully customizable and visually modern digital clock application built with Python and Tkinter. Designed to simulate real-time ticking with manual time adjustment capabilities across **seconds, minutes, hours, days, weeks, months, and years** — ideal for time-based simulations, testing alarm logic, or time-sensitive applications.

---

##  Features

- Real-time ticking clock (hh:mm:ss)
- Live date display (Week, Day, Month, Year)
- Fully adjustable time:
  - + / − Seconds, Minutes, Hours
  - + / − Days, Weeks, Months, Years
-  Clean and modern Tkinter GUI with styled controls
-  Modular structure:
  - `clocklogic.py` – Core clock time engine
  - `gui.py` – Styled GUI with real-time updates
  - `main.py` – Entry point to launch the application
-  Easy integration with other apps (exposes getters like `get_hours()`, `get_day()`, `get_week()`, etc.)

---

##  Project Structure

```
project-root/
├── clocklogic.py   # Time logic engine (adjustments, tick, formatting)
├── gui.py          # Tkinter interface with styled controls
├── main.py         # Entry point to run the app
```

---

##  How to Run

### 1. Install Python

Make sure you have Python 3.7+ installed. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

### 2. Run the app

```bash
python main.py
```

---

##  Integration Example

Want to use this clock in another Python application? Just import the logic engine:

```python
from clocklogic import ClockLogic

clock = ClockLogic()
print(clock.get_time_snapshot())  # {'hour': 12, 'minute': 30, 'second': 5, ...}
```

Available getters:

```python
clock.get_seconds()
clock.get_minutes()
clock.get_hours()
clock.get_day()
clock.get_week()
clock.get_month()
clock.get_year()
```

---

##  Use Cases

- Time-based Simulation & Testing Tools
- Educational Demos and Clock Simulators
- Date/Time-Aware Logging or Scheduling Systems

---

##  Author

Made by Kahilu Chipango – Lusaka, Zambia 🇿🇲  
_Data Analyst | Aspiring Head of AI_

---

##  License

MIT License
