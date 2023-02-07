array = [1,2,3,4,5]
#array = [3,2,1]

rev_sorted_array = sorted(array, reverse=True)

def use_division():
    grand_total = 1
    for i in rev_sorted_array:
        grand_total = grand_total * i

    result = []
    for j in array:
        result.append(int(grand_total/j))
    
    return result

def products(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result

use_division = use_division()
no_division = products(array)
print(use_division)
print(no_division)