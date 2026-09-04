# Brainfuck Interpreter 

![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-grey)


A pure Python interpreter for the esoteric programming language **Brainfuck**.

This implementation focuses on code readability and modern Python practices, utilizing **Type Hinting** and **Pattern Matching** (`match/case`) to process instructions on an 'infinite' tape.

## Features
* **Standard Compliance:** Implements all 8 standard Brainfuck commands (`<`, `>`, `+`, `-`, `.`, `,`, `[`, `]`).
* **8-Bit Cell Wrapping:** Cells wrap around 0-255 (overflows reset to 0, underflows to 255).
* **Buffered Input:** Handles input streams efficiently using a `deque`.
* **Tape Visualization:** Includes a debug method to visualize the memory tape and the current head position.

## Requirements
* **Python 3.10+** (Required for `match/case` syntax).

## Usage

### 1. Installation
Clone the repository:
```bash
git clone https://github.com/Alireza2317/brainfuck-interpreter
cd brainfuck-interpreter
```

### 2. Create a Brainfuck File
Create a file named `hello.bf` with the standard "Hello World" code:
```brainfuck
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
```
(or use a code you already have)

### 3. Run the Interpreter
Pass the filename as a command-line argument:
```bash
python bf_int.py hello.bf
```

**Output:**
```text
Hello World!
```

## Project Structure

* **`BFFileReader` Class:** Handles file I/O and strips non-command characters (comments) from the source code.
* **`BFCompiler` Class:** The core logic.
    * `init_tape()`: Initializes a memory array of 10,000 cells.
    * `run()`: Recursive execution loop that handles nested brackets `[...]` logic.
    * `print_tape()`: A debug utility to print the current state of memory.

## Debugging
You can uncomment `compiler.print_tape()` in the `main` block to see a visual representation of memory after execution:

```text
TAPE=[0x0, 0x0, <0x48>("H")>, 0x65("e"), 0x6c("l"), ...]
```

## What is Brainfuck?
Brainfuck is a minimalist esoteric programming language created in 1993. It operates on a simple array of memory cells (the "tape") and uses only 8 commands to perform all calculations.

| Command | Description |
| :---: | :--- |
| `>` | Move the pointer to the right |
| `<` | Move the pointer to the left |
| `+` | Increment the memory cell at the pointer |
| `-` | Decrement the memory cell at the pointer |
| `.` | Output the character signified by the cell at the pointer |
| `,` | Input a character and store it in the cell at the pointer |
| `[` | Jump past the matching `]` if the cell at the pointer is 0 |
| `]` | Jump back to the matching `[` if the cell at the pointer is nonzero |
