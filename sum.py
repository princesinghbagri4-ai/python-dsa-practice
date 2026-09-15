def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:

        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return True

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return False


print(two_sum_sorted([1,2,3,4,5,6,7,8,9], 13))
print(two_sum_sorted([1,3,5,7,9], 6))
print(two_sum_sorted([1,3,5,7,9], 20))