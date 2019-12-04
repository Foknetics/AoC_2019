def decreasing(password):
    list_password = [int(digit) for digit in str(password)]
    return list_password != sorted(list_password)


def adjacent(password):
    last_digit = password[0]
    for digit in password[1:]:
        if digit == last_digit:
            return True
        last_digit = digit
    return False


puzzle_input = '146810-612564'
start, end = puzzle_input.split('-')

valid_passes = []
for password in range(int(start), int(end)+1):
    if decreasing(password):
        continue
    if adjacent(str(password)):
        valid_passes.append(password)

print(f'Potential valid passwords: {len(valid_passes)}')
