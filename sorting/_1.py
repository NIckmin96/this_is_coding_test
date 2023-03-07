# 위에서 아래로

N = int(input())
nums = [int(input()) for _ in range(N)]

# 1.sorted
for num in sorted(nums, reverse=True) : 
    print(num, end = ' ')
    
# # 2. 선택 정렬
# for i in range(len(nums)) : 
#     for j in range(i, len(nums)) : 
#         if nums[i] < nums[j] : 
#             nums[i],nums[j] = nums[j],nums[i]
            
# for num in nums : 
#     print(num, end = ' ')

# # 3. 삽입 정렬
# for i in range(len(nums)) : 
#     for j in range(i, 0, -1):
#         if nums[j] > nums[j-1] : 
#             nums[j-1],nums[j] = nums[j], nums[j-1]
#         else : break
        
# for num in nums : 
#     print(num, end = ' ')
        