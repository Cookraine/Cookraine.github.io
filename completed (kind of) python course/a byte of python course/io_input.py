# punc = (',', '.', '!', '?', '-', '—', ';', ':', '…', '"', ' ')
import string

def remove_punctuations(word):
    return "".join(i.lower() for i in word if i in string.ascii_letters)

def reverse(text):
    return text[::-1]


def is_palindrome(text):
    text = remove_punctuations(text)
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")