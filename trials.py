"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in the given array."""
    
    for item in items:
        print(item)

def get_all_evens(nums):
    # evenNums = []

    # for num in nums:
    #     if num % 2 == 0:
    #         evenNums.append(num)

    # return evenNums

    # List Comprehension
    return [num for num in nums if num % 2 == 0] 


def get_odd_indices(items):
    result = []

    for index, value in enumerate(items):
        if index % 2 != 0:
            result.append(value)
    
    return result



def print_as_numbered_list(items):
    for index, value in enumerate(items):
        print(f"{index + 1}. {value}")

    # i = 1
    # for item in items:
    #     print(f"{i}. {item}")
    #     i += 1
    


def get_range(start, stop):
    # nums = []
    # range(start, stop, step)
    # for num in range(start, stop):
    #     nums.append(num)

    # return nums
    return list(range(start, stop))


def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)
    
    return " ".join(chars)

# Camel case helloWorld
# Pascal case HelloWorld
def snake_to_camel(string):
    camel_case = []

    for word in string.split('_'):
        # word.slice(1) === word[1:]
        camel_case.append(f"{word[0].upper()}{word[1:]}")
  
    return "".join(camel_case)



def longest_word_length(words):
    # longest = len(words[0])

    # for word in words: 
    #     if longest < len(word): 
    #         longest = len(word)

    # return longest

    # List Comprehension
    return max([len(word) for word in words])

  
def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)

    return "".join(result)


def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
             parens -= 1

        if parens < 0:
            return False
    
    return parens == 0
    

def compress(string):
    compressed = []

    currChar = ''
    charCount = 0
    for char in string:
        if char != currChar: 
            compressed.append(currChar)
        
            if (charCount > 1):
                compressed.append(str(charCount))
      

            currChar = char
            charCount = 0

        charCount += 1
  

    compressed.append(currChar)
    if charCount > 1:
        compressed.append(str(charCount))
  

    return "".join(compressed)

