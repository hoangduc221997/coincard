# print("{:,}".format(52123.42346273))
def int_digits(n):
    return [n] if n<10 else int_digits(n/10)+[n%10]

print(int_digits(100))
