# Read input
n = int(input())
s = input()

# Count occurrences of 'A' and 'D'
count_A = s.count('A')
count_D = s.count('D')

# Determine the result
if count_A > count_D:
    print("Anton")
elif count_D > count_A:
    print("Danik")
else:
    print("Friendship")
