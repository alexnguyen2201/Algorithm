def sum_equal_to_k(nums, k):
  dp = set()
  dp.add(0)

  for num in nums:
    next_dp = set()
    for t in dp:
      next_dp.add(t)
      next_dp.add(t + num)

    dp = next_dp
  
  return k in dp

print(sum_equal_to_k([1,5,11,5], 11))


"""
def sum_equal_to_k(nums, k):
  dp = {0}

  for num in nums:
    next_dp = set()
    for t in dp:
      next_dp |= {t, t+num}
      
    dp = next_dp
  
  return k in dp
  
  
>>> sum_equal_to_k([1,5,11,5], 11)
>>> True


Time complexity: O(len(nums)*sum(nums))
Space complexity: O(sum(nums))
"""