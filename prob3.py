array1 = [3,4,-1,1]
# array1 = [1,2,0]
sorted_array = sorted(array1)

def first_missing_positive(nums):
    if not nums:
        return 1
    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            if nums[i] == nums[v - 1]:
                break
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(nums) + 1

def first_missing_positive(nums):
    s = set(nums)
    i = 1
    while i in s:
        i += 1
    return i

next_member = 0
for i in range(len(sorted_array)):
    next_member = sorted_array[i] + 1
    if sorted_array[i] == 0:
        continue
    elif next_member == 0:
        continue
    elif next_member >= len(sorted_array):
        print(next_member)
        break

    if sorted_array[i+1] != next_member:
        print(next_member)
        break
   
    
