file = open('f2.txt', 'r')
data = file.read()
upper_case = 0
lower_case = 0

for txt in data:
    out = txt.split()
    for i in out:
        if i.isupper():
            upper_case = upper_case + 1
        elif i.islower():
            lower_case = lower_case + 1

print("UPPERCASE : ", upper_case)
print("LOWERCASE: ", lower_case)

file.close()

