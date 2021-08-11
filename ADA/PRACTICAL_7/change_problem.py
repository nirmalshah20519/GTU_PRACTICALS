def change_problem(Arr, n, Amt ):
    if Amt==0:
        return 1
    if Amt<0:
        return 0
    if n<=0 and Amt>=1:
        return 0
    return change_problem( Arr,n-1,Amt ) + change_problem( Arr,n,Amt-Arr[n-1]);
 
print("Enter the list of coins/notes available :",end=' ')
arr = input().strip().split()
arr=list(map(int, arr))
n=len(arr)
amt=int(input("Enter the amount :"))
print("Number of solutions possible : ", change_problem(arr,n,amt))