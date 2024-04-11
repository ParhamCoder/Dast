def diff_operation(num):
    digits = list(str(num))
    asc_digits = sorted(digits)
    desc_digits = sorted(digits, reverse=True)
    asc_num = int(''.join(asc_digits))
    desc_num = int(''.join(desc_digits))
    diff = desc_num - asc_num
    return diff

def get_final_diff(num, k):
    final_diff = num
    for _ in range(k):
        final_diff = diff_operation(final_diff)
    return final_diff
num = int(input("First num: "))
k = int(input("Count: "))
result = get_final_diff(num, k)
print("total :", result)
