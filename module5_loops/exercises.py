# Module 5: Loops Examples

# 1. While loop counting down
n = 5
while n > 0:
    print("Countdown:", n)
    n -= 1
print("Blastoff!")

# 2. For loop summing numbers
numbers = [5, 4, 3, 2, 1]
total = 0
for num in numbers:
    total += num
print("Sum:", total)

# 3. Using break/continue
for num in [9, 41, 12, 3, 74, 15]:
    if num == 3:
        print("Found 3, skipping")
        continue
    if num == 74:
        print("Stopping at 74")
        break
    print("Processing:", num)
