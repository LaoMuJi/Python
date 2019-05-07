import copy

def test_nums(temp):
    temp.append(33)

nums = [11,22]

test_nums(nums)

print(1,nums)

test_nums(copy.deepcopy(nums))

print(2,nums)

a=test_nums(copy.deepcopy(nums))

print(2,nums)

print(a)