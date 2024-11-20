# TAN KARAGELDI
# ASSIGNMENT 3
# ARTIFICIAL INTELLIGENCE - COMP 3651

import math

word_list_fname = "linuxwords.txt"
n_letters = 5
n_guesses = 5

## function for creating a word list given a file name and number of letters. 

def make_word_list(word_list_fname,n_letters,allow_proper_noun=False):
    # Initialization
    wordlist = [] # Initialize to an empty list
    # Open the file containing the list of words
    wordlist_file = open(word_list_fname, "r")
    # Loop through the lines (words) in the list
    word = wordlist_file.readline()
    while(len(word) > 0):
        # Remove leading and trailing whitespace, if any
        word = word.strip().lower()
        if((len(word) == n_letters) and word.isalpha()):
            if(allow_proper_noun or word.islower()):
                wordlist.append(word)
        # Read next word
        word = wordlist_file.readline()
    # Return the complete word list
    return wordlist

# function for checking letters of a guess against the solution, to see if they match or not.
def check_letters(solution, guess):
    result = ""
    for i in range(len(solution)):
        if guess[i] == solution[i]:
            result = result + guess[i].upper()
        elif guess[i] in solution:
            result = result + guess[i]
        else:
            result = result + "_"
    return result

## function for calculating the information gain of a guess given a wordlist

def calculate_gain(guess,wordlist):
    ## initialized a dictionary to store the counts of each feedback, will use this to calculate the entropy.
    feedback_counts = {}

    ## populate the dictionary with the counts of each feedback 
    for solution in wordlist:
        feedback = check_letters(solution,guess)
        if feedback in feedback_counts:
            feedback_counts[feedback] += 1
        else: 
            feedback_counts[feedback] = 1

    # ex_entropy variable is the entropy of the current wordlist
    ex_entropy = 0
    for count in feedback_counts.values():
        ex_entropy -= (count / len(wordlist) * math.log2(count / len(wordlist)))
    
    all_ent = math.log2(len(wordlist))
    gain = all_ent - ex_entropy
    
    return gain

# this function finds the best guess given a wordlist with n letters.
def give_best_guess(wordlist):
    # assign the m value to the highest possible float value.
    m = float("inf")
    best_guess = ""
    for guess in wordlist:
        info_gain = calculate_gain(guess,wordlist)
        # if the information gain is smaller than the current m value, update the m value and the best guess. 
        # I know we're supposed to maximize the information gain, but as the value of my calculate_gain function gets larger, 
        # i think the information gained from that word gets smaller. So, I decided to minimize the information gain to find the best guess.
        # When i printed out the feedback values dictionary from the previous function on words "fuzzy" and "lares", fuzzy had over 2000 "_____" feedback,
        # which does not give much information about the next step, while lares had the least from all the words i tried which was around 160.
        if info_gain < m:
            m = info_gain
            best_guess = guess
    return best_guess,m

def wordle(solution, wordlist,n_guesses):
    possible_solutions = wordlist
    solution = solution.lower()

    for i in range(n_guesses):
        # Find the best guess based on information gain, store both to print out.
        best_guess, gain = give_best_guess(possible_solutions)
        print(f"Guess {i + 1}: {best_guess}, Information Gain: {gain}")
        
        # Check if the guess matches the solution
        if best_guess == solution:
            break
        
        # Get feedback for the current guess and filter possible solutions
        feedback = check_letters(solution, best_guess)
        print(f"Feedback: {feedback}")

        # holder list is for storing the possible solutions that match the feedback
        holder = []

        for word in possible_solutions:
            check = check_letters(word,best_guess)
            if check == feedback:
                holder.append(word)

        possible_solutions = holder
        n_guesses -= 1

        print(f"Possible solutions: {len(possible_solutions)}")
        print("--------------------------------------------")

## first question 
def best_four_letter():
    wordlist = make_word_list(word_list_fname, 4)
    return give_best_guess(wordlist)

## second question 
def best_five_letter():
    wordlist = make_word_list(word_list_fname, 5)
    return give_best_guess(wordlist)

## solving sequences for BLANK and QUIRK
def solve():
    wordlist = make_word_list(word_list_fname, 5)
    solution1 = "BLANK"
    solution2 = "QUIRK"
    print("\n--------------SOLUTION FOR BLANK---------------\n")
    wordle(solution1, wordlist,5)
    print("\n--------------SOLUTION FOR QUIRK---------------\n")
    wordle(solution2, wordlist,5)

# FINISHED ASSIGNMENT. RUNNING ALL THE FUNCTIONS BELOW WILL GIVE MY ANSWERS AND THE SOLUTIONS FOR BLANK AND QUIRK.
print("Best 4-letter word:", best_four_letter())
print("Best 5-letter word:", best_five_letter())
print("Solving wordle:")
solve()

    
    