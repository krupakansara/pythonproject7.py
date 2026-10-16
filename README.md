📂 Modular and Packages
A feature-rich Python command-line utility application designed to demonstrate modular programming, package structures, built-in library exploration, and custom utility functions.
---
📁 File Structure
```text
modularandpackages/
│
├── main.py             # Main entry point providing an interactive CLI menu
└── utilities/          # Custom package containing utility modules
    ├── __init__.py     # Exposes package-level functions
    ├── file_operations.py  # Handles basic text file reading and writing
    └── math_utilities.py   # Handles basic unit conversions (Celsius/Fahrenheit, Kilometers/Miles)
```
---
🚀 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.
Prerequisites
🐍 Python 3.x installed on your system.
Running the Application
Open your terminal or command prompt.
Navigate to the folder containing your project files.
Run the main script:
```bash
   python main.py
   ```
---
⚙️ How the Files Work Together
`main.py`: Serves as the interactive application hub. It brings together Python's built-in modules (`datetime`, `time`, `math`, `random`, `uuid`, `string`) and your custom `utilities` package to provide an intuitive CLI menu.
`utilities/__init__.py`: Acts as the package initializer, importing and exposing functions from `file_operations` and `math_utilities`.
`utilities/file_operations.py`: Provides interactive functions to write text contents to a user-specified file or read existing files with built-in error handling.
`utilities/math_utilities.py`: Contains custom conversion helpers, such as translating Celsius to Fahrenheit and kilometers to miles.
---
✨ Features & Menu Options
⏰ Date & Time Operations: Access real-time clocks, calculate differences between dates, format custom dates, use a stopwatch, or run a countdown timer.
📐 Mathematical Operations: Perform standard arithmetic, calculate square roots, find factorials, compute trigonometry and logarithms, calculate compound interest, and find the area of a circle.
🎲 Random Utilities: Generate random numbers and lists, create custom passwords, perform random sampling, generate secure OTPs, and play a built-in dice game.
🔑 UUID Generator: Instantly generate unique identifiers (UUIDv4).
📝 File Operations: Securely write text to files and read file contents right from the menu.
🌡️ Unit Conversions: Convert temperatures and distances using custom mathematical logic.
🔍 Module Explorer: Inspect attributes and methods of built-in and custom modules dynamically using `dir()`.
---
📄 License
This project is open-source and free to use for learning and development.
