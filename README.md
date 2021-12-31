# Coding Practice: Two Number Summation

This project is meant for me to practice coding interview questions with Python.
In this project, I am presented with the following task: write a function 
that takes in a non-empty of distinct integers and an integer representing a 
target sum. If any two numbers in the input array sum up to the target sum, 
the function should return them in the array (in any order). If no two 
numbers sum up to the target sum--the funciton should return an empty array. 
You cannot add a single integer to itself in order to obtain the target 
sum--assume that there will be at most one pair of numbers that will sum to 
the target number.

## Running The Project
**NOTE: Your IDE may configure the project implicitly as a module. BE SURE TO 
RUN STEP 4 BELOW BEFORE SUBMITTING LABS** 

1. Download and install Python on your computer
2. Navigate to the [TwoNumberSumSol3.Mod1]() directory
3. Run the program as a module: `python -m Mod1 -h`. This will print the help 
   message.
4. Run the program as a module (with real inputs): `python -m Mod1 <random 
   input file> <random output file>`
   a. IE: `python -m Mod1 input.txt output.txt`

The program's output will be displated in the output.txt file.

### Lab1 Usage:

```commandline
usage: python -m Mod1 [-h] 

optional arguments:
  -h, --help  show a help message and exits the program
```

Usage statements are very formalized

| Symbol    | Meaning   |
| ---           | ---       |
| [var]         | variable var is optional. |
| var           | variable var is required. All positional arguments are required.|
| -v, --version | This refers to a flag. One dash + one letter OR two dashes and a whole word. Some flags take one or more arguments |
| +             | This argument consumes 1 or more values |
| *             | This argument consumes 0 or more values |

### Project Layout

The following was my project's package layout:

* TwoNumberSum.Mod1/: `The parent or "root" folder containing all of the 
  projecs files`
    * README.md:
      `The README files that describes my programs and the nuances needed 
      to run the program`
    * Mod1/: 
      `The module of my program (per requirement).`
      * __init__.py 
        `This python file details critical functions, variables, and 
        classes that are exposed when scripts import the Lab1 module.`
      * __main__.py 
        `The starting point when the program runs, it handles command line 
        arguments.`
      * *.py 
        `Holds the scripts that perform the code.`