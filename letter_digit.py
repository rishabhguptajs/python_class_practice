file = open('f2.txt', 'r')
data = file.read()

digit_num = 0
letter_num = 0

for txt in data:
    out = txt.split()
    for i in out:
        if i.isnumeric():
            digit_num = digit_num + 1
        elif i.isalpha():
            letter_num = letter_num + 1

print("LETTERS: ", letter_num)
print("DIGITS: ", digit_num)

file.close()

