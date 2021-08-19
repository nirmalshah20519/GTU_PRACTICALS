def lcs(Str_1, Str_2, m, n):  
    if m == 0 or n == 0:
       return 0;
    elif Str_1[m-1] == Str_2[n-1]:
       return 1 + lcs(Str_1, Str_2, m-1, n-1);
    else:
       return max(lcs(Str_1, Str_2, m, n-1), lcs(Str_1, Str_2, m-1, n));

Str_1 = "ABBBDCADACDACACBDBBDACA"
Str_2 = "ABACDDACACDBAAACDBDACDA"
print("## Longest common subsequence")
print("String 1 : ",Str_1)
print("String 2 : ",Str_2)
print ("Length of LCS is ", lcs(Str_1, Str_2, len(Str_1), len(Str_2)))
