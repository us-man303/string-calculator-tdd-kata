# String Calculator

This repository contains a simple yet powerful String Calculator implemented in Python. The calculator is designed to perform basic arithmetic operations by summing numbers provided as strings with various delimiters.

## Features

- **Sum Up to Two Numbers**: The calculator can sum up to two numbers separated by commas.
- **Empty String Handling**: If an empty string is provided, the calculator will return `0`.
- **Handle Unknown Number of Inputs**: The calculator can handle an unknown number of inputs.
- **Support New Line Delimiters**: You can use new lines (`\n`) as delimiters along with commas.
- **Custom Delimiters**: The calculator supports custom delimiters defined at the beginning of the string.
- **Negative Number Exception**: Passing negative numbers will raise an exception with a message listing all the negative numbers.
- **Ignore Numbers Greater than 1000**: Numbers greater than 1000 will be ignored in the sum.
- **Delimiters of Any Length**: Custom delimiters can be of any length.
- **Multiple Custom Delimiters**: You can define multiple custom delimiters, even if they have different lengths.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/string-calculator.git
2. **setup the project:**
    cd string-calculator-tdd-kata
3. **setup virtual env:** (optional)
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Run the test_calcultor.py file:**
    python test_calculator.py