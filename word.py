word = 'GREETINGS'


def char_to_int(word):
    return [ord(char) - 64 for char in word]


new_word = []
word = char_to_int(word)
print(word)
i = 0
start = 1

while (i < len(word)):
    curr_word = word[i]
    for j in word[start:]:
        if j < curr_word:
            curr_word -= j
            break
    start += 1
    new_word.append(curr_word)
    i += 1
    print(new_word)