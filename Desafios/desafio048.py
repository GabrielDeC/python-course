s = 0
for i in range (0, 501, 3):
    if i%3 == 0 and i%2 != 0:
        s = s + i
print(s)