'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # if not zero then set it to be index 0
    notzero = []
    zero = []
    for i in range(len(arr)):
        # check if not zero
        if arr[i] != 0:
            # append to non zeros
            notzero.append(arr[i])
        # check if is zero
        else:
            # append to zeros
            zero.append(0)
    new_arr = notzero + zero
    # new_arr = new_arr[zero:]
    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 3, 1, 0, -2, 0]
    arr = [1, 2, 3, 0, 4, 0, 0]
    arr = [0, 0, 0, 0, 3, 2, 1] 

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")