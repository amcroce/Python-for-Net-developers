nums = [1,5,8,10,7,2]

# for in is similar to foreach in c#
for n in nums:
    print(f"The value is {n}")

# enumerate() function allows you to loop over a list and have an automatic counter
for idx, n in enumerate(nums, start=1):
    print(f"Index {idx} has value {n}")