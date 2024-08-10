import math
from sys import stdin, stdout

def is_non_decreasing(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

def solve():
    input = stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index+n]))
        index += n
        
        if n == 3:
            gcd_seq = [math.gcd(a[0], a[1]), math.gcd(a[1], a[2])]
            if gcd_seq[0] <= gcd_seq[1]:
                results.append("YES")
            else:
                results.append("YES")
            continue
        
        prefix_gcd = [0] * n
        suffix_gcd = [0] * n
        
        prefix_gcd[0] = a[0]
        for i in range(1, n):
            prefix_gcd[i] = math.gcd(prefix_gcd[i-1], a[i])
        
        suffix_gcd[n-1] = a[n-1]
        for i in range(n-2, -1, -1):
            suffix_gcd[i] = math.gcd(suffix_gcd[i+1], a[i])
        
        non_decreasing = False
        
        for i in range(n):
            if i == 0:
                current_gcd_seq = [suffix_gcd[1]]
            elif i == n-1:
                current_gcd_seq = [prefix_gcd[n-2]]
            else:
                current_gcd_seq = [math.gcd(prefix_gcd[i-1], suffix_gcd[i+1])]
            
            if is_non_decreasing(current_gcd_seq):
                non_decreasing = True
                break
        
        if non_decreasing:
            results.append("YES")
        else:
            results.append("NO")
    
    stdout.write("\n".join(results) + "\n")

# To run the solve function
if __name__ == "__main__":
    solve()
