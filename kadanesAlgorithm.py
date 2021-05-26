def max_subarray(numbers):
    best_sum = float('-inf')
    best_start = best_end = 0
    current_sum = 0
    for current_end, x in enumerate(numbers):
        if current_sum <= 0:
            current_start = current_end
            current_sum = x
        else:
            current_sum += x
        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1
    return best_sum, best_start, best_end
a = [-13, -3, -25, -20, -3, 16, -7]
print ("Maximum contiguous sum is", max_subarray(a))




#  the time complexity of Kadane’s Algorithm is O(n).