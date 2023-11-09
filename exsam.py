## Strings

# Mandatory problems:


# String Concatenation:
# Concatenate the strings 'Python', 'is', 'a', 'powerful', 'language' to create a single string, 'Python is a powerful language.'

a="python"
b= "is"
c="a"
d="powerful"
f="language"
space=""
print(a+space+b + space+c+space+d+space+ f)



# Variable Declaration:
# Declare a variable named topic and assign it the value "strings in Python."

topic="strings in Python."
print(topic)



# Printing with Escape Symbols:
# Print the following sentence, including the double quotes: "Learning about "Python" strings is fun."

sent= "Learning about \":Python\" strings is fun."
print(sent)


# String Length and Character Count:
# Calculate and print the length of the topic string. Also, count and print how many times the letter 's' appears in the string.

sent="Also, count and print how many times the letter 's' appears in the string."
print(sent.count('s'))


# Uppercase and Lowercase Conversion:
# Create a new variable called upper_topic by converting the topic string to uppercase. Then, create another variable called lower_topic by converting the topic string to lowercase.

sen="uppercase and lowercase conversion"
print(sen.isupper())

sent="UPPERCASE AND LOWERCASE CONVERSION"
print(sen.islower())

# String Formatting:
# Use f-strings to format the topic string in the following way: "Let's learn about {topic}."

name="Let's learn about topic."


# Substring Extraction:
# Extract and print the word 'Python' from the topic string.

sent=" Extract and print the word Python from the topic string."
topic=sent[22:29]
print(sent)

## Lists

## Mandatory problems:


# List Append and Extend:
# Create a list called programming_languages with the elements ['Python', 'Java']. Use the append() method to add 'C++' to the list. Then, use the extend() method to add ['JavaScript', 'Ruby'] to the list. Print the updated list.

programming_languages=['Python', 'Java']
programming_languages.append("C++")
programming_languages.extend ['JavaScript', 'Ruby']
print(programming_languages)


# List Insertion:
# Insert the string 'C#' at the third position in the programming_languages list and print the modified list.

programming_languages=['Python', 'Java']
programming_languages.append("C++")
programming_languages.insert(2)
print(programming_languages)




# List Removal:
# Remove the second element from the programming_languages list and print the updated list.



# List Clearing:
# Use a method to clear all elements from the programming_languages list and print the empty list.

programming_languages=['Python', 'Java','JavaScript', 'Ruby']
programming_languages.clear
print(programming_languages)

# List Index:
# Find and print the index of the element 'Java' in the programming_languages list.

# List Count:
# Count and print the number of times 'Python' appears in the programming_languages list.

# List Reversal:
# Reverse the order of elements in the programming_languages list and print the reversed list.


## Bonus problems


# List Copy:
# Create a new list languages_copy by copying the elements from the programming_languages list. Modify one element in the original list and ensure that the copy remains unchanged.

# List Slicing:
# Use slicing to create a new list first_two containing the first two elements from the programming_languages list.

# List Concatenation:
# Create a new list by concatenating the programming_languages list with another list containing ['Swift', 'Kotlin']. Print the resulting list.

# List Sorting:
# Sort the elements in the programming_languages list in reverse alphabetical order (descending) and print the sorted list.

# List Removal by Value:
# Remove all occurrences of 'JavaScript' from the programming_languages list and print the modified list.

# List Element Extraction:
# Use the pop() method to extract and print the last element of the programming_languages list, and then print the updated list without that element.

# List Element Counting:
# Count and print the total number of elements in the programming_languages list.
