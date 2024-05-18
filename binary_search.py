#Binary Search in python
arr=[3,4,6,7,8,9]
target=4
low=0
high=len(arr)-1
index=-1
while low<=high:
    mid=(low+high)//2
    mid_element=arr[mid]
    if target==mid_element:
        index=mid
        break
    elif target<mid_element:
        high=mid-1
    elif target>mid_element:
        low=mid+1

if(index==-1):
    print("Target Not Found")
else:
    print(f"The Index of the Target is {index}")
