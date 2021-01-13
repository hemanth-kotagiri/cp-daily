vowels = ["A","E","I","O","U","Y"]
given = input()
solution = ''
for i in range(len(given)):
    now = given[i]
    if now not in vowels:
        if now.upper() in vowels:
            continue
        solution+="."+now.lower()

print(solution)
