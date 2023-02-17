# 시각

N = int(input())

# 1hour = 60*60 = 3600s * 24 = 86400s
cnt = 0
for i in range((N+1)*60*60) : 
    h = i//(60*60)
    m = (i-h*(60*60))//60
    s = i-h*60*60-m*60
    
    if ('3' in str(h)) | ('3' in str(m)) | ('3' in str(s)):
        cnt +=1
        
print(cnt)