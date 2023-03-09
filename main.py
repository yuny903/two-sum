def twoSum(self, nums: List[int], target: int) -> List[int]:
  for i in range(0,lens(nums)):
	  for j in range(i+1,lens(nums)):
		  if nums[i]+nums[j]==target:
			  return [i,j]
		
  return [-1,-1]