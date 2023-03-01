def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res


test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

print(f"The original list : {test_list}")


res = prod([ele for sub in test_list for ele in sub])

print(f"The total element product in lists is : {str(res)}")
