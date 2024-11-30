# Take n input
n = int(input())

# Take list input as a single line of digits
digits = input()


# Initialize total
total = 0

# Loop through each digit and add its integer value to total
for digit in digits:
    total += int(digit)

# Print the total
print(total)

    