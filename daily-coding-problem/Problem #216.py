# This problem was asked by Facebook.

# Given a number in Roman numeral format, convert it to decimal.

# The values of Roman numerals are as follows:
# If the next number is greater than the current, we subtract. else add.
# For the input XIV, for instance, you should return 14.
# 10 + 5 - 1 = 14

roman_conv = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

# MMMDCCCCLXXXXIX

def convert(roman, ans=0):
    if len(roman) == 1:
        ans += roman_conv[roman[0]]
        return ans
    if roman_conv[roman[0]] >= roman_conv[roman[1]]:
        ans += roman_conv[roman[0]]
        roman = roman[1:]
        if not roman:
            return ans
        return convert(roman, ans)
    else:
        ans += roman_conv[roman[1]] - roman_conv[roman[0]]
        roman = roman[2:]
        if not roman:
            return ans
        return convert(roman, ans)

print(convert("MMMCMXCIX"))

def convert_roman_to_digit(rd):
    if len(rd) == 2:
        if roman_conv[rd[1]] > roman_conv[rd[0]]:
            return roman_conv[rd[1]] - roman_conv[rd[0]]
        else:
            return roman_conv[rd[1]] + roman_conv[rd[0]]
    answer = roman_conv[rd[0]]
    rd = rd[1:]
    i = 1
    while i < len(rd):
        if i == len(rd)-1:
            answer += roman_conv[rd[i]]
        else:
            if roman_conv[rd[i]] > roman_conv[rd[i - 1]]:
                temp = roman_conv[rd[i]] - roman_conv[rd[i - 1]]
                answer += temp
            else:
                temp = roman_conv[rd[i]] + roman_conv[rd[i - 1]]
                answer += temp
        i+=1
    return answer

def digit_to_roman(num):
    while num:
        pass
