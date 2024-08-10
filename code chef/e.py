def min_operations_to_make_beautiful(t, test_cases):
    results = []
    
    for _ in range(t):
        n, k, a = test_cases[_]
        operations = 0
        for i in range(n // 2):
            if a[i] != a[n - i - 1]:
                diff = abs(a[i] - a[n - i - 1])
                if diff % k != 0:
                    operations = -1
                    break
                operations += max(a[i], a[n - i - 1]) - min(a[i], a[n - i - 1]) - 1
        results.append(operations)
    
    return results

# Reading input
import sys
input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1
test_cases = []

for _ in range(t):
    n, k = map(int, data[index:index + 2])
    index += 2
    a = list(map(int, data[index:index + n]))
    index += n
    test_cases.append((n, k, a))

results = min_operations_to_make_beautiful(t, test_cases)

# Output the results
for result in results:
    print(result)
