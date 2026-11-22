# Pig Latin translator: move the first letter to the end and add "ay"
pyg = 'ay'

original = input('Enter a word:')

# only translate non-empty words made of letters
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print(new_word)
else:
    print('empty')
