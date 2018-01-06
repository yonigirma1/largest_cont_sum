#Finding largest conti.. SUM

def largest_cont_sum(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for num in [1:]:
        current_sum = max(current_sum + num, num)

        max_sum = max(max_sum, current_sum)

    return max_sum
    
