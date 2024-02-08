e_counter = 0

sentence = input("Type a sentence: ")

sentence_list = list(sentence)

for letter in sentence_list:
    if letter == "e":
        e_counter += 1

print(f"The sentence contains 'e' {e_counter} times.")
