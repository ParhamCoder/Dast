def is_sacred(num):
    num_str = str(num)
    if '3' in num_str and '5' in num_str and '7' in num_str:
        for digit in num_str:
            if digit not in ['3', '5', '7']:
                return False
        return True

def count_sacred_numbers(n):
    count = 0
    for i in range(1, n+1):
        if is_sacred(i):
            count += 1
    return count

n = int(input())
result = count_sacred_numbers(n)
print(result)
