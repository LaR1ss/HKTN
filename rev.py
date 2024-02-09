def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
user_input = input("Введите предложение: ")
reversed_sentence = reverse_sentence(user_input)
print("Обратное предложение :", reversed_sentence)
