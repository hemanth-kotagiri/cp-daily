firstString = input()
secondString = input()

def main():
    temp = 0
    while temp<len(firstString):
        if firstString[temp].lower()==secondString[temp].lower():
            temp+=1
        else:
            if ord(firstString[temp].lower())>ord(secondString[temp].lower()):
                return 1
            return -1
    return 0


print(main())