
def twoSum( nums, target):
    hashmap = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[nums[i]] = i



nums = [1,2,3,4,5,6]
target = 7
# nums = list(map(int,input("put in the array ").split()))
# target = int(input("Enter the target "))

print(twoSum(nums,target))