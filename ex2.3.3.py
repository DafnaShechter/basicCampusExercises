# Prompt user to input the number of bricks collected by each pig
num = input("Enter three digits (each digit for one pig): ")

# Extract individual digits and convert them to integers
hundreds = int(num) // 100
tens = (int(num) % 100) // 10
ones = int(num) % 10

# Calculate total number of bricks
total_bricks = hundreds + tens + ones

# Calculate number of bricks per pig and remainder
bricks_per_pig = total_bricks // 3
remainder = total_bricks % 3

# Print the results
print(total_bricks)
print(bricks_per_pig)
print(remainder)
print(remainder == 0)
