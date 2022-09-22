
def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
<<<<<<< HEAD
    num = 0
    for i in numbers:
        if i >= num:
            num = i
    return num
=======
#Final Version
    max_num = max(numbers)
    return max_num

>>>>>>> e18bbbf8745176a41ff2e139ad7f7f5e3a537a28


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
