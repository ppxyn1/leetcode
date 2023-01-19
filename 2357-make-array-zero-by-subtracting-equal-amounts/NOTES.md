작은 수 부터 하나씩 제외시키면 해결 되는것 같다.?
​
​
아래 코드 Time Limit Exceeded issue에 대해 생각해보기!
​
# counter
count = 0
# while loop
while sum(nums) !=0:
for i in nums:
if i == 0:
# remove 0
nums.remove(i)
# choose a minimum number
idx = min(nums)
# subtract it from each element
nums = list(map(lambda a:a-idx, nums))
# increment the counter
count +=1
return count