def is_two(input_value):
    return input_value == 2 or input_value == "2" or input_value == 2.0 # checks to see if the input value is the number to or the string 2 or the float 2.0
#is_two(2.0)





def is_vowel(char):
    # checks if char matches any of these string vowels
    return char == 'A' or char == 'a' or char == 'E' or char == 'e' or char == 'I' or char == 'i' or char == 'O' or char == 'o' or char == 'U' or char == 'u'
#is_vowel('a')





def is_consonant(char):
    return char.isalpha() and not is_vowel(char) #ensures character is aplhabetic and is not a vowel
#print(is_consonant('B'))





def cap_if_consonant(word):
    #checks that the first char in a word is alphabetic and not a vowel
    if word and word[0].isalpha() and not word[0].lower() in "a, e, i, o, u":
        return word[0].upper() + word[1:] # Uppercases the first character in the word and then returns the rest of the word in lowercase
    else:
        return word

# Testing
# word = "codeup"
# result = cap_if_consonant(word)
# print(result)




def calculate_tip(tip_percentage, bill_total):
    if 0 <= tip_percentage <= 1: # ensures the tip will be a valid percentage
        tip_amount = tip_percentage * bill_total # calculates tip_amount with multiplication
        return tip_amount
    else:
        return "Invalid tip percentage, please enter a value between 0 and 1."

# Test the function
# tip_percentage = 0.20
# bill_total = 100
# tip = calculate_tip(tip_percentage, bill_total)
# print(f"Tip amount: ${tip:.2f}")





def apply_discount(original_price, discount_percentage):
    if 0 <= discount_percentage <= 1: #ensures discount_percentage is between 0 and 1
        discount_amount = discount_percentage * original_price #computes the discount amount
        return discount_amount
    else:
        return "Invalid discount percentage, please enter a value between 0 and 1."

# Testing
# discount_percentage = 0.15
# original_price = 100
# discounted_price = original_price - apply_discount(original_price, discount_percentage)
# print(f"Discounted price: ${discounted_price:.2f}")





def handle_commas(number_string):
    # Remove commas and convert to a number
    number_string = number_string.replace(",", "")
    try:
        number = int(number_string) #casting number_string to integer
        return number
    except ValueError:
        try:
            number = float(number_string) #casting number_string to floating-point
            return number
        except ValueError:
            return "Invalid input: not a valid number"
        
        
        
        
def get_letter_grade(score):
    #checks to see if score is in the specified range and returns the appropriate letter grade
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 0 <= score < 60:
        return "F"
    else:
        return "Invalid score: Score must be between 0 and 100"

# Testing
# score = 100
# letter_grade = get_letter_grade(score)
# print(f"Letter grade: {letter_grade}")





def remove_vowels(input_string):
    # Remove vowels from string input
    vowels = "AEIOUaeiou"
    result = ''.join([char for char in input_string if char not in vowels])
    return result

# Testing function
# input_string = "Hello World!"
# new_string = remove_vowels(input_string)
# print(new_string)






import re #imports more python functions


def normalize_name(input_string):
    
    normalized = input_string.strip().lower() #takes away white spaces and makes characters lower cased.
    
    normalized = normalized.replace(" ", "_") #replaces spaces with underscores
    
    normalized = re.sub(r'[^a-zA-Z0-9_]', '', normalized) #Return the string obtained by replacing the leftmost non-overlapping occurrences of the pattern in string by the replacement repl.  repl can be either a string or a callable;
    
    return normalized


# Test the funtion
# input_string = "   %First Name Henry"
# normalized_string = normalize_name(input_string)
# print(normalized_string)




def cumulative_sum(numbers):
    #initializing the variables
    cumulative = []
    total = 0
    for number in numbers:
        #computes the total by adding each number and appends the total
        total += number
        cumulative.append(total)
    return cumulative

# Testing
# result1 = cumulative_sum([1, 1, 1])
# print(result1)

# result2 = cumulative_sum([1, 2, 3, 4])
# print(result2)