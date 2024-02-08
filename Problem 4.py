char_counter = 0

char = input("Type a letter you want to count: ")

sentence = input("Now type the sentence you want to count the letter in: ")
sentence_list = list(sentence)

for letter in sentence_list:
    if letter == char:
        char_counter += 1

print(f"\nThe sentence contains '{char}' {char_counter} times.")
