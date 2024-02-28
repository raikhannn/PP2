#1
import re
def match_string(text):
    pattern = r'ab*'
    if re.fullmatch(pattern, text):
        return True
    else:
        return False
# Test the function
test_strings = ["a", "ab", "abb", "abbb", "ac", "abc", "aab", "bb"]
for string in test_strings:
    if match_string(string):
        print(f"'{string}' matches the pattern.")
    else:
        print(f"'{string}' does not match the pattern.")

#2
import re
def match_string(text):
    pattern = r'ab{2,3}'
    if re.fullmatch(pattern, text):
        return True
    else:
        return False
# Test the function
test_strings = ["ab", "abb", "abbb", "abbbb", "ac", "abc", "aab", "bb"]
for string in test_strings:
    if match_string(string):
        print(f"'{string}' matches the pattern.")
    else:
        print(f"'{string}' does not match the pattern.")

#3
import re
def find_sequences(text):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, text)
# Test the function
test_text = "This_is_a_test_sentence_with_some_words_joined_with_underscore."
sequences = find_sequences(test_text)
print("Sequences found:")
for sequence in sequences:
    print(sequence)

#4
import re
def find_sequences(text):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, text)
# Test the function
test_text = "This Is A Test Sentence With Some Words Joined With Underscore."
sequences = find_sequences(test_text)
print("Sequences found:")
for sequence in sequences:
    print(sequence)

#5
import re
def match_string(text):
    pattern = r'^a.*b$'
    if re.match(pattern, text):
        return True
    else:
        return False
# Test the function
test_strings = ["acb", "a1234b", "axb", "a5678b", "acbd", "abc", "ab", "abab"]
for string in test_strings:
    if match_string(string):
        print(f"'{string}' matches the pattern.")
    else:
        print(f"'{string}' does not match the pattern.")

#6
import re
def replace_with_colon(text):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', text)
# Test the function
test_text = "This is a test, for replacing spaces. and, commas."
result = replace_with_colon(test_text)
print("Original text:", test_text)
print("After replacement:", result)

#7
def snake_to_camel(snake_case):
    words = snake_case.split('_')
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case
# Test the function
snake_case_string = "hello_world_this_is_snake_case"
camel_case_string = snake_to_camel(snake_case_string)
print("Snake case:", snake_case_string)
print("Camel case:", camel_case_string)

#8
import re
def split_at_uppercase(string):
    pattern = r'[A-Z]'
    split_strings = re.findall(pattern, string)
    if split_strings:
        return re.split(pattern, string)
    else:
        return [string]
# Test the function
test_string = "SplitThisStringAtUpperCaseLetters"
result = split_at_uppercase(test_string)
print("Original string:", test_string)
print("After splitting at uppercase letters:", result)

#9
import re
def insert_spaces(text):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.sub(pattern, ' ', text)
# Test the function
test_text = "ThisIsAExampleStringWithWordsStartingWithCapitalLetters"
result = insert_spaces(test_text)
print("Original text:", test_text)
print("After inserting spaces:", result)

#10
def camel_to_snake(camel_case):
    snake_case = ''
    for i, char in enumerate(camel_case):
        if i > 0 and char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char.lower()
    return snake_case
# Test the function
camel_case_string = "ConvertThisCamelCaseStringToSnakeCase"
snake_case_string = camel_to_snake(camel_case_string)
print("Camel case:", camel_case_string)
print("Snake case:", snake_case_string)
