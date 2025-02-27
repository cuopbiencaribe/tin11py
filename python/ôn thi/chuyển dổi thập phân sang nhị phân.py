def decimal_to_binary(num):
    """Chuyển đổi số thập phân sang nhị phân bằng cách chia liên tục cho 2"""
    binary_num = ""
    while num > 0:
        remainder = num % 2
        binary_num = str(remainder) + binary_num
        num //= 2
    return binary_num

print(decimal_to_binary(100))
