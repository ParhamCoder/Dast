def diff_operation(num):
    # تبدیل عدد به لیست اعداد
    digits = list(str(num))
    # مرتب کردن اعداد به صورت صعودی و نزولی
    asc_digits = sorted(digits)
    desc_digits = sorted(digits, reverse=True)
    # تبدیل اعداد به عدد
    asc_num = int(''.join(asc_digits))
    desc_num = int(''.join(desc_digits))
    # محاسبه عدد اختلافی
    diff = desc_num - asc_num
    return diff

def get_final_diff(num, k):
    final_diff = num
    for _ in range(k):
        final_diff = diff_operation(final_diff)
    return final_diff

# دریافت ورودی از کاربر
num = int(input("عدد اولیه را وارد کنید: "))
k = int(input("تعداد مراحل مورد نظر را وارد کنید: "))

# محاسبه عدد اختلافی نهایی
result = get_final_diff(num, k)
print("عدد اختلافی نهایی:", result)
