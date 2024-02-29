"""
Lab 6 - Strings and Tuples 
(100 marks in total, including 5 exercises - each 20 marks)

Author: Muskaan Hashmi
Due Date: This Friday (Mar. 1) 11am.
Submission: Upload your lab python file to your GitHub repository.

Objective:
1. Learn how to write a good python docstring for documenting functions'
purpose, parameters, return values. A good docstring helps other developers 
understand how to use the function and serves as documentation that can be 
displayed in tools like IDEs. A sample docstring has been written for exercise 1 and 2,
students need to write good docstrings for all the other exercises.
2. Review how to code simple Python functions and write unit tests using assert
3. Practice how to operate on strings and tuples (similar to lists, but strings and tuples are immutable)
4. Review iterations using loop
5. Review the boolean expression and conditionals
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Exercise 1 (20 marks: function implementation: 10 marks, unit tests: 10 marks)

Complete the function below to reverse a string.

For example, 
reverse_str("Abd") should return "dbA".
reverse_str("COMP115") should return "511PMOC".

Hint: the accumulator algorithm and the string concatenation using the operator '+'
"""
def reverse_str(s):
    """
    This function reverses string s.

    E.g., 
    >>> reverse_str('app')
    'ppa'

    Parameters:
    - s (string): The string to be reversed

    Returns:
    - (string): A reversed version of string s.

    """
  reversed_str = "" 
    for char in s:
        reversed_str = char + reversed_str 
    return reversed_str
    

# Your unit tests
import unittest

class TestReverseStr(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(reverse_str("hello"), "olleh")

    def test_palindrome(self):
        self.assertEqual(reverse_str("madam"), "madam")

    def test_sentence(self):
        self.assertEqual(reverse_str("hello world"), "dlrow olleh")

    def test_empty_string(self):
        self.assertEqual(reverse_str(""), "")

    def test_numbers_and_letters(self):
        self.assertEqual(reverse_str("COMP115"), "511PMOC")

# To run the tests
if __name__ == "__main__":
    unittest.main()

"""
Exercise 2 (20 marks: function implementation: 10 marks, unit tests: 10 marks)

Complete the function below to count how many vowels ('a', 'e', 'i', 'o', 'u') in a string.

For example, 
count_vowels("Apple") should return 2, since 'A' and 'e' are vowels.
count_vowels("Hmmm") should return 0, since there are no vowels.

Hint: you may want to convert the input string to its lowercase version using s.lower() first.
"""
def count_vowels(s):
    """
    This function counts the number of vowels in the string s.

    E.g., 
    >>> count_vowels("Apple")
    2

    Parameters:
    - s (string): The string in which vowels are counted.

    Returns:
    - (int): The total number of vowels in the string s.

    """
    vowels = "aeiou" 
    count = 0 
    for char in s.lower():
        if char in vowels:
            count += 1 
    return count
    

# Your unit tests
import unittest

class TestCountVowels(unittest.TestCase):
    def test_with_vowels(self):
        self.assertEqual(count_vowels("Apple"), 2)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("Hmmm"), 0)

    def test_mixed_case(self):
        self.assertEqual(count_vowels("Hello World"), 3)

    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_all_vowels(self):
        self.assertEqual(count_vowels("AeIoU"), 5)

    def test_numbers_and_letters(self):
        self.assertEqual(count_vowels("123AEiou"), 5)

# To run the tests
if __name__ == "__main__":
    unittest.main()



"""
Exercise 3 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to remove the duplicate characters in a string.

E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"

Hint: We have implemented a function removing duplicates for a list in week 6. Similar.
"""
def remove_duplicates(s):
    """
    Write your docstring
    """
    def remove_duplicates(s):
    seen = set()  # To keep track of seen characters
    result = ''  # Initialize the result string
    for char in s:
        if char not in seen:
            seen.add(char)  # Add unseen character to the set
            result += char  # Append unseen character to the result
    return result


# Your unit tests
import unittest

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates_simple(self):
        self.assertEqual(remove_duplicates("apple"), "aple")

    def test_case_sensitivity(self):
        self.assertEqual(remove_duplicates("Popsipple"), "Popsile")

    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates("pear"), "pear")

    def test_empty_string(self):
        self.assertEqual(remove_duplicates(""), "")

    def test_all_duplicates(self):
        self.assertEqual(remove_duplicates("aaaa"), "a")

# To run the tests
if __name__ == "__main__":
    unittest.main()



"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the lowerest index of a charactor t found in a string s, 
to return -1 if the character is not in the string.

E.g.,
find_index("Abd", 'b') == 1
find_index("Abdccc", 'c') == 3
find_index("Abd", 'w') == -1

Note: we should implement our own algorithm, not using the built-in function find().
"""
def find_index(s, t):
    """
    Write your docstring
    """
    def find_index(s, t):
    for i, char in enumerate(s):  
        if char == t:
            return i  
    return -1


# Your unit tests
import unittest

class TestFindIndex(unittest.TestCase):
    def test_character_present(self):
        self.assertEqual(find_index("Abd", 'b'), 1)

    def test_character_present_multiple_times(self):
        self.assertEqual(find_index("Abdccc", 'c'), 3)

    def test_character_absent(self):
        self.assertEqual(find_index("Abd", 'w'), -1)

    def test_empty_string(self):
        self.assertEqual(find_index("", 'a'), -1)

    def test_search_empty_character(self):
        self.assertEqual(find_index("Abd", ''), -1)

# To run the tests
if __name__ == "__main__":
    unittest.main()


"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the project completion day, 
given the current day in a week and estimated time of days to completion.

E.g.,
project_completion_day('Monday', 4) returns 'Friday'.
project_completion_day('Monday', 7) returns 'Monday'.
project_completion_day('Saturday', 2) returns 'Monday'.
project_completion_day('Saturday', 1) returns 'Sunday'.

Hint:
days_week.index(day) will return the index of the day in the tuple days_week.

"""

days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')
# Notice that days_week is a tuple, and it works the same if it's a list,
# since the index operation is the same for tuple and list.


def project_completion_day(day, days_to_completion):
    """
    Write your docstring
    """
    def project_completion_day(day, days_to_completion):
    index = days_week.index(day)
    completion_index = (index + days_to_completion) % 7  
    return days_week[completion_index]  


# Your unit tests
import unittest

class TestProjectCompletionDay(unittest.TestCase):
    def test_within_week(self):
        self.assertEqual(project_completion_day("Monday", 4), "Friday")

    def test_exact_week(self):
        self.assertEqual(project_completion_day("Monday", 7), "Monday")

    def test_weekend_wrap(self):
        self.assertEqual(project_completion_day("Saturday", 2), "Monday")

    def test_single_day(self):
        self.assertEqual(project_completion_day("Saturday", 1), "Sunday")

    def test_multiple_weeks(self):
        self.assertEqual(project_completion_day("Wednesday", 10), "Saturday")

# To run the tests
if __name__ == "__main__":
    unittest.main()



"""
Congratulations on finishing your lab6. Hope you feel more confident on function implementation.

Now you just need to upload it to your GitHub repository. That's all.
"""
