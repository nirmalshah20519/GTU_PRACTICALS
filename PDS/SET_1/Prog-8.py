# Python program to print even numbers in a list

List= [2, 7, 5, 64, 14]
print(List)
List2=[]
for i in List:
    if i%2==0:
        List2.append(i)
print("Even numbers found in list are :", end='\n')
print(List2)
