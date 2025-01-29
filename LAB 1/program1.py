#write a program to find the largest and smallest element in the array
arr =['10','89','9','56','4','80','8']
mini = 10
maxi = 10
print(arr)
for num in arr:
    num = int(num)
 
    if num < mini:
        mini=num
    if num > maxi:
        maxi=num
print("smallest element is ",mini)
print("largest element is ",maxi)
