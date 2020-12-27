# Dropbox
# given 1, return "A". Given 27, return "AA".

# def alphabetical_encode(num):
#     if num % 26 == 0:
#         return "Z" * (num // 26)
#     else:
#         if num < 26:
#             ans = chr(64 + num)
#         else:
#             times = num // 26
#             remaining = num - times
#             ans = "Z" * times
#             ans += chr(64 + remaining)
#         return ans


# print(alphabetical_encode(27))