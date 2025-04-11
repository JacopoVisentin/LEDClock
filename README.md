# Virtual TIXClock - LED Matrix Clock

A customizable LED matrix clock inspired by the TIX clock concept. This project lights up a matrix of LEDs to display the current time using a visually abstract format. Each digit of the time is represented by a grid of lit dots.

This part of the project is just meant to display a virtual version of the physical product inside your terminal.

The C++ code for the physical model can be found on my github as well.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Project Structure

``` bash
LEDClock/
├── clock/                      # Core code (rendering logic, time parsing)
│   ├── clock_display.py        # Time-to-dot mapping logic
│   ├── clock_timer.py          # Time synchronization
│   ├── utils.py                # Helper functions
│   └── config.yaml             # Custom working parameters
│
├── dev/                        # code testing
│   └── dev_sandbox.py
│
├── .gitignore
├── main.py                     # Entry point
├── README.md                   # You are here
└── requirements.txt            # Dependencies
```

## Installation

Go to the folder where you want to download the project:

```bash
cd your-projects-folder
```

Clone this repository:

```bash
git clone https://github.com/JacopoVisentin/LEDClock.git
cd LEDClock
```

Once inside your python virtual environment, install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Inside the project root directory, run:

```bash
python3 main.py
```

## Configuration

Not implemented yet

## License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
