Text = input("Input your text? :")
Text_low = Text.lower()

letter_count = {}
for letter in Text_low:
    letter_count[letter] = Text_low.count(letter)

for key in sorted(letter_count):
    print(key, ":", str(letter_count[key]))