# Wordle Solver - Assignment 3

**Author:** Tan Karageldi

## Overview

This project implements a Wordle Solver, an AI-based program designed to solve the popular Wordle puzzle. It uses techniques like entropy and information gain to optimize guesses, reducing the number of attempts needed to find the correct solution.

The program includes functionalities for:

- Generating a list of valid words from a dictionary.
- Evaluating guesses based on feedback and narrowing possible solutions.
- Selecting the best guess using information gain calculations.
- Demonstrating solutions for specific puzzles.

## Features

- **Word List Generator:** Creates a list of valid words of a specified length.
- **Letter Checker:** Matches guessed letters with the solution and provides feedback.
- **Information Gain Calculation:** Measures the effectiveness of each guess.
- **Best Guess Finder:** Identifies the optimal word to guess based on feedback and information gain.
- **Wordle Solver:** Simulates solving Wordle puzzles using an AI-based strategy.

## Usage

### 1. Prerequisites

- Ensure you have Python installed (version 3.x).
- A file named `linuxwords.txt` must be present in the working directory. It should contain a dictionary of words, one per line.

### 2. Running the Program

Run the Python script directly:

```bash
python wordle_starter.py
```

### 3. Main Outputs

- **Best 4-Letter Word:** Suggests the best word to start with for a 4-letter Wordle puzzle.
- **Best 5-Letter Word:** Suggests the best word to start with for a 5-letter Wordle puzzle.
- **Solutions for Specific Words:** Demonstrates solving Wordle for the words "BLANK" and "QUIRK."

## Functions

1. **`make_word_list(word_list_fname, n_letters, allow_proper_noun=False)`**  
   Generates a list of words from the dictionary file matching the specified length and rules.

2. **`check_letters(solution, guess)`**  
   Provides feedback for a guess by comparing it to the solution:

   - Uppercase for exact matches.
   - Lowercase for correct letters in the wrong position.
   - `_` for incorrect letters.

3. **`calculate_gain(guess, wordlist)`**  
   Calculates the information gain of a guess based on entropy.

4. **`give_best_guess(wordlist)`**  
   Identifies the best word to guess based on the word list and information gain.

5. **`wordle(solution, wordlist, n_guesses)`**  
   Simulates solving Wordle, narrowing solutions and printing progress.

## Notes

- The algorithm assumes that the feedback mechanism is consistent with Wordle's rules.
- To customize the program, modify the `n_letters`, `n_guesses`, or `wordlist` file as needed.
