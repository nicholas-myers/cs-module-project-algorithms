'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''



def sliding_window_max(nums, k):
    # Your code here
    maxnums = []
    increment = 0
    while increment < len(nums):
        # this will always be first window    
        window = nums[increment:k+increment]
        max_num = window[0]
        if len(window) == k:
            for num in window:
                if num > max_num:
                    max_num = num
            maxnums.append(max_num)
        print(window)
        # this shifts the window over one
        increment+=1
        
    return maxnums

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
