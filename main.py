import csv  # Used to output to the result.csv file.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The dictionary used for numerical character comparison in-transit.
ALPHABETICAL_VALUE = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
ALPHABETICAL_VALUE_REDUCED = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9, 's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    """
    Takes in input, and calls the computation and output functions.
    """

    sentence = input("Sentence me, oh jury: ").lower()  # Gathers input from the user and stores it as the variable sentence, and automatically lowers it.

    with open('result.csv', 'w+', newline='') as csvfile:  # Opens a result.csv file for outputting the compuation to.
        outputfile = csv.writer(csvfile, delimiter=',', quotechar='"')  # Creates a writer function that is used to output to the result.csv file.
        word_length_total = 0  # Sets a variable to accumulate the total amount of characters in the sentence.
        sentence_total = 0  # Sets a variable for the total of each word converted character total.
        sentence_total_reduced = 0  # Sets a variable for the total of each word converted and reduced character total.
        first_letter_reduced_total = 0  # Sets a variable for the total of the converted reduced value of the first letter.
        sentence_total_deduced = 0  # Sets a variable for the total of each word converted and deduced character total.
        amount_of_words = 0  # Sets a variable to count the amount of words in the sentence.
        for word in sentence.split():  # For every word in the string variable sentence, gathered from the user:
            word_length, character_values, character_values_reduced, total_of_word, total_of_word_reduced, total_of_word_deduced = sentence_parse(word)  # For each word, call the sentenceparse() function, and output the variable associated, along with adding to the variables above the appropriate values.
            word_length_total += word_length  # Adds the word length to the variable word_length_total
            sentence_total += total_of_word  # Adds the total converted character value to the variable sentence_total
            sentence_total_reduced += total_of_word_reduced  # Adds the total converted and reduced character value to the variable sentence_total_reduced
            sentence_total_deduced += total_of_word_deduced  # Adds the total converted and deduced character value to the variable sentence_total_deduced

            try:  # Tries to add the first letter reduced total to the variable.
                first_letter_reduced_total += ALPHABETICAL_VALUE_REDUCED.get(word[:1])  # Adds the converted reduced chracter value to the variable first_letter_reduced_total
            except TypeError:  # However, if there is a non-alphabetical character in the first letter place:
                print("Please do not have any non-alphabetical characters in the first character place value!")  # Scream at the user to fix their input.
            word_output(word_length, character_values, character_values_reduced, total_of_word, total_of_word_reduced, total_of_word_deduced, word, outputfile)  # Call the output function to write to result.csv
            amount_of_words += 1  # Adds one to the variable amount_of_words for each word.

        total_output(word_length_total, sentence_total, sentence_total_reduced, first_letter_reduced_total, sentence_total_deduced, amount_of_words, outputfile)  # Calls the total_output function

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sentence_parse(word):
    """
    Parses the incoming sentence for its needed attributes for the table.
    """

    character_values = []  # Creates a list for each individual word that has each character listed as a variable to compare to the dictionary ALPHABET.
    total_of_word = 0  # Sets the sum of the character values to zero, to be used later in the code.
    total_of_word_reduced = 0  # Sets a variable for the total of each word reduced.
    character_values_reduced = []  # Sets a list variable for the converted reduced chracter values.
    word_length = 0  # Sets a variable for the word length

    for character in word:  # For each character in the word variable.
        if character not in ALPHABETICAL_VALUE:  # If the character is not in the standard alphabet, then skip it.
            pass  # Passes the value.
        else:  # If the character is in the standard alphabet:
            character_values.append(ALPHABETICAL_VALUE.get(character))  # Appends the basic number value to the character_values list, storing that value in its place.
            character_values_reduced.append(ALPHABETICAL_VALUE_REDUCED.get(character))  # Appends the reduced number value to the character_values_reduced list, storing that value in its place.
            word_length = word_length + 1  # Adds one to the variable word_length

    for item in character_values:  # For each number value in the list character_values:
        total_of_word += int(item)  # Add that value to the sum of the word variable total_of_word.

    for item in character_values_reduced:  # For each number value in the list character_values_reduced:
        total_of_word_reduced += int(item)  # Add that value to the sum of the word variable total_of_word_reduced.

    if sum(map(int, list(str(total_of_word_reduced)))) > 9:  # If the sum of both digits is greater than nine:
        total_of_word_deduced = sum(map(int, list(str(sum(map(int, list(str(total_of_word_reduced))))))))  # Redo the sum, which should make it less than 10 almost 90% of the time.
    else:  # If it is already a one-digit numberL
        total_of_word_deduced = sum(map(int, list(str(total_of_word_reduced))))  # Sets a variable for the converted deduced word totals of each word.

    return(word_length, character_values, character_values_reduced, total_of_word, total_of_word_reduced, total_of_word_deduced)  # Returns the computed values back to main()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def word_output(word_length, character_values, character_values_reduced, total_of_word, total_of_word_reduced, total_of_word_deduced, word, outputfile):
    """
    Outputs the words, their character values, word character total, and reduced and deduced versions of those, if applicable.
    """

    character_sum = equational_sum(character_values)  # Calls the equational_sum function for the equational sum total of the list character_values.
    character_sum_reduced = equational_sum(character_values_reduced)  # Calls the equational_sum function for the equational sum total of the list character_values_reduced.

    # Write all of the incoming information to the result file table.
    outputfile.writerow([word[:1].upper(), '=', ALPHABETICAL_VALUE_REDUCED.get(word[:1]), word_length, '1', word.upper(), character_sum, total_of_word, character_sum_reduced, total_of_word_reduced, total_of_word_deduced])  # Outputs the values to the result.csv file

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def equational_sum(total):
    """
    Takes in the number total and creates/returns the equational sum of that total.
    """

    summerize = ""  # summerization variable to be returned to the variable calling the function.

    if isinstance(total, int):
        if int(total) > 9:  # If the variable sentence_total_deduced is less than 9 ( meaning that this isn't needed because it is already deduced):
            iterable = 0  # Create an iterable variable
            for digit in str(total):  # For each individual number inside of the integer:
                if iterable == 0:  # If this is the first individual number coming through:
                    summerize = digit  # Set the variable sentence_total_deduced_sum to that individual number:
                else:  # if it is any other individual number:
                    summerize = "{}+{}".format(summerize, digit)  # Add the equational sum to the variable sentence_total_deduced_sum
                iterable = 1  # Set the iterable to 1, effectively telling the code to only use the else part of the conditional above when parsing digits after this.

    if isinstance(total, list):
        iterable = 0  # Creates an iterable variable.
        for item in total:  # For each number value in the total:
            if iterable == 0:  # If this is the first item:
                summerize = item  # Make it the first item in the string.
            else:  # If this isn't the first item:
                summerize = "{}+{}".format(summerize, item)
            iterable = 1  # Set the iterable to 1, effectively telling the code to only use the else part of the conditional above when parsing digits after this.

    return summerize

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def total_output(word_length_total, sentence_total, sentence_total_reduced, first_letter_reduced_total, sentence_total_deduced, amount_of_words, outputfile):
    """
    Outputs the original total, sentence totals, first letter totals, and the amount of words, along with the reduced and deduced versions of those, and their computational sums for easier reading.
    """

    # First block of equational sum variables to be outputted in the "ADD TO REDUCE" row.
    first_letter_deduced_sum = equational_sum(first_letter_reduced_total)  # Calls the equational_sum function for the equational sum total of the variable first_letter_reduced_total.
    word_length_sum = equational_sum(word_length_total)  # Calls the equational_sum function for the equational sum total of the variable word_length_total.
    amount_of_words_sum = equational_sum(amount_of_words)  # Calls the equational_sum function for the equational sum total of the variable amount_of_words.
    sentence_total_sum = equational_sum(sentence_total)  # Calls the equational_sum function for the equational sum total of the variable sentence_total.
    sentence_total_reduced_sum = equational_sum(sentence_total_reduced)  # Calls the equational_sum function for the equational sum total of the variable sentence_total_reduced.
    sentence_total_deduced_sum = equational_sum(sentence_total_deduced)  # Calls the equational_sum function for the equational sum total of the variable sentence_total_deduced.

    # First block of totallities between the numbers of an integer, to be outputted in the "SECOND TOTAL" row.
    first_letter_deduced_total = sum(map(int, list(str(first_letter_reduced_total))))  # Sets a variable for the total of the converted deduced values for the first letter of every word.
    word_length_deduced_total = sum(map(int, list(str(word_length_total))))  # Sets a variable for the total of the deduced values of the word length.
    amount_of_words_total = sum(map(int, list(str(amount_of_words))))  # Sets a variable for the total of the amount of words when reduced.
    sentence_second_total = sum(map(int, list(str(sentence_total))))  # Sets a variable for the second combined total of the sentence (reduced total).
    sentence_reduced_second_total = sum(map(int, list(str(sentence_total_reduced))))  # Sets a variable for the second combined total of the reduced sentence total (second reduced total).
    sentence_deduced_second_total = sum(map(int, list(str(sentence_total_deduced))))  # Sets a variable for the second combined total of the deduced sentence total (second deduced total).

    # Second block of equational sum variables to be outputted in the "REDUCE TO DEDUCE" row.
    first_letter_essence_sum = equational_sum(first_letter_deduced_total)  # Calls the equational_sum function for the equational sum total of the variable first_letter_deduced_total.
    word_length_essence_sum = equational_sum(word_length_deduced_total)  # Calls the equational_sum function for the equational sum total of the variable word_length_deduced_total.
    amount_of_words_essence_sum = equational_sum(amount_of_words_total)  # Calls the equational_sum function for the equational sum total of the variable amount_of_words_total.
    sentence_total_essence_sum = equational_sum(sentence_second_total)  # Calls the equational_sum function for the equational sum total of the variable sentence_second_total.
    sentence_total_reduced_essence_sum = equational_sum(sentence_reduced_second_total)  # Calls the equational_sum function for the equational sum total of the variable sentence_reduced_second_total.
    sentence_total_deduced_essence_sum = equational_sum(sentence_deduced_second_total)  # Calls the equational_sum function for the equational sum total of the variable sentence_deduced_second_total.

    #Second block of totallities between the numbers of an integer, to be outputted in the "ESSENCE OF NUMBER" row.
    first_letter_essence_total = sum(map(int, list(str(first_letter_deduced_total))))  # Sets a variable for the essence total of the first letter column.
    word_length_essence_total = sum(map(int, list(str(word_length_deduced_total))))  # Sets a variable for the essence total of the word length column.
    amount_of_word_essence_total = sum(map(int, list(str(amount_of_words_total))))  # Sets a variable for the essence total of the amount of words column.
    sentence_essence_total = sum(map(int, list(str(sentence_second_total))))  # Sets a variable for the essence total of the sentence total column.
    sentence_total_reduced_essence = sum(map(int, list(str(sentence_reduced_second_total))))  # Sets a variable for the essence total of the sentence total reduced column.
    sentence_total_deduced_essence = sum(map(int, list(str(sentence_deduced_second_total))))  # Sets a variable for the essence total of the sentence total deduced column.

    # The line below outputs all of the variables/numbers associated with the "First Total"
    outputfile.writerow(['', '', first_letter_reduced_total, word_length_total, amount_of_words, 'FIRST TOTAL', '', sentence_total, '', sentence_total_reduced, sentence_total_deduced])
    # The line below outputs all the variables/numbers associated with "Add to Reduce"
    outputfile.writerow(['', '', first_letter_deduced_sum, word_length_sum, amount_of_words_sum, 'ADD TO REDUCE', '', sentence_total_sum, '', sentence_total_reduced_sum, sentence_total_deduced_sum])
    # The line below outputs all the variables/numbers associated with the "Second Total"
    outputfile.writerow(['', '', first_letter_deduced_total, word_length_deduced_total, amount_of_words_total, 'SECOND TOTAL', '', sentence_second_total, '', sentence_reduced_second_total, sentence_deduced_second_total])
    # The line below outputs all of the variables/numbers associated with "Reduce to Deduce"
    outputfile.writerow(['', '', first_letter_essence_sum, word_length_essence_sum, amount_of_words_essence_sum, 'REDUCE TO DEDUCE', '', sentence_total_essence_sum, '', sentence_total_reduced_essence_sum, sentence_total_deduced_essence_sum])
    # The line below outputs all of the variables/numbers associated with the "Essence of Number"
    outputfile.writerow(['', '', first_letter_essence_total, word_length_essence_total, amount_of_word_essence_total, 'ESSENCE OF NUMBER', '', sentence_essence_total, '', sentence_total_reduced_essence, sentence_total_deduced_essence])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

main()  # Calls the main function.
