def solution(phone_number):
    phone_number = list(phone_number)
    for i in range(len(phone_number)-4):
        phone_number[i] = "*"
    return ''.join(phone_number)


print(solution("01033334444"))
print(solution("027778888"))
