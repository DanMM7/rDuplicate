def remove_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# Run the program
if __name__=='___main__':
    # Ask user to input the list of numbers
    nums = list(map(int, input("Enter the list of numbers: ").split()))

    remove_duplicates(nums)

    print("test")

