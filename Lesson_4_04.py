'''Write a Python program to reverse 123  to 321 in text.
Sample String : 'I have 123 books'
Expected Result : 'I have 321 books'''''

string_1 = input("input the string: ")
text_to_reverse = '123'
print(string_1.replace(text_to_reverse, text_to_reverse[::-1]))