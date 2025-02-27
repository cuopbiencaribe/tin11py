def permute(nums):
    result = []

    # Nếu danh sách trống, trả về một danh sách trống
    if len(nums) == 0:
        return []

    # Nếu danh sách có một phần tử, trả về danh sách chứa phần tử đó
    if len(nums) == 1:
        return [nums]

    # Lặp qua từng phần tử trong danh sách
    for i in range(len(nums)):
        # Chọn phần tử hiện tại
        current = nums[i]

        # Lấy phần còn lại của danh sách trừ phần tử hiện tại
        remaining = nums[:i] + nums[i+1:]

        # Tạo ra các hoán vị của phần còn lại
        for p in permute(remaining):
            result.append([current] + p)

    return result

# Ví dụ sử dụng hàm permute
elements = [1, 2, 3]
permutations = permute(elements)

# Hiển thị các hoán vị
for permutation in permutations:
    print(permutation)
