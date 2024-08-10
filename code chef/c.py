import sys
import math
from collections import defaultdict

def solve_permutation_problems(test_cases):
    results = []
    
    for n, p in test_cases:
        # Create a dictionary to store the positions of each number
        pos = defaultdict(list)
        for i in range(n):
            pos[p[i]].append(i + 1)
        
        count = 0
        # Check pairs (i, j) where 1 <= i < j <= n
        for i in range(1, n + 1):
            for j in range(i * 2, n + 1, i):
                # Only valid pairs (i, j) where j is a multiple of i
                if i < j and (p[i - 1] * p[j - 1]) % (i * j) == 0:
                    count += 1
        
        results.append(count)
    
    return results

# Reading input
input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1
test_cases = []

for _ in range(t):
    n = int(data[index])
    index += 1
    p = list(map(int, data[index:index + n]))
    index += n
    test_cases.append((n, p))

results = solve_permutation_problems(test_cases)

# Output the results
for result in results:
    print(result)
