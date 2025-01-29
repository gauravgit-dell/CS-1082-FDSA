#write a program to find the largest and smallest element in the array and second largest and second smallest in the array
arr =['10','89','9','56','4','80','8']
mini = 10
maxi = 10
secmaxi = 10
secmini = 10
print(arr)
for num in arr:
    num = int(num)
 
    if num < mini:
        secmini = mini
        mini=num
    if num > maxi:
        secmaxi=maxi
        maxi=num
    elif num > secmaxi and num !=maxi:
        secmaxi = num
    elif num < secmini and num != mini:
        secmini = num
    
        
print("smallest element is ",mini)
print("largest element is ",maxi)
print("second largest is",secmaxi)
print("second smallest element",secmini)

 
