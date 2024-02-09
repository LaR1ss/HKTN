def is_palindrome(word):
    word = word.lower().replace(" ", "")
    if word == word[::-1]:
        return True
    else:
        return False
user_input = input("Введите слово: ")
if is_palindrome(user_input):
    print(user_input, "палиндромом.")
else:
    print(user_input, "не палиндромом.")
