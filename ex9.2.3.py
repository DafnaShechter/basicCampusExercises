def who_is_missing(file_name):
    with open(file_name, 'r') as f:
        nums = f.read().strip().split(',')
        nums = [int(num) for num in nums]
        nums.sort()

        missing_num = None
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                missing_num = nums[i] - 1
                break

        with open('found.txt', 'w') as f:
            f.write(str(missing_num))

        return missing_num
