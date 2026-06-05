nums1=[1,3]
nums2=[4,2]
result = nums1 + nums2
result.sort()
print(result)
if len(result)%2!=0:
    mid=len(result)//2
    print(result[mid])
else:
    mid1=len(result)//2
    mid2=mid1-1
    print((result[mid1]+result[mid2])/2)
    
    