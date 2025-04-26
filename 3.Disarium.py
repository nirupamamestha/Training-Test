def disarium(num):
    num_str = str(num)
    total = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    return total == num

def find_first_n_disarium(n):
    disarium_numbers = []
    num = 1
    while len(disarium_numbers) < n:
        if disarium(num):
            disarium_numbers.append(num)
        num += 1
    return disarium_numbers

def find_disarium_in_range(start, end):
    disarium_numbers = [num for num in range(start, end + 1) if disarium(num)]
    return disarium_numbers


n = 10
start, end = 1, 200

print(f"First {n} Disarium numbers: {find_first_n_disarium(n)}")
print(f"Disarium numbers between {start} and {end}: {find_disarium_in_range(start, end)}")
