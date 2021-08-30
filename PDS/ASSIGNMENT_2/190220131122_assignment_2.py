MyDit = {
  "clients": [
    {
      "id": "59761c23b30d971669fb42ff",
      "isActive": True,
      "age": 36,
      "name": "Dunlap Hubbard",
      "gender": "male",
      "company": "CEDWARD",
      "email": "dunlaphubbard@cedward.com",
      "phone": "+1 (890) 543-2508",
      "address": "169 Rutledge Street, Konterra, Northern Mariana Islands, 8551",
      "clients": {
        "id": "59761c23b30d971669fb42ff_updated",
        "isActive": True,
        "age": 36,
        "name": "Dunlap Hubbard",
        "gender": "male",
        "company": "CEDWARD",
        "email": "dunlaphubbard@cedward.com",
        "phone": "+1 (890) 543-2508",
        "address": "169 Rutledge Street, Konterra, Northern Mariana Islands, 8551",
        "clients": {
          "id": "59761c23b30d971669fb42ff_updated2",
          "isActive": True,
          "age": 36,
          "name": "Dunlap Hubbard",
          "gender": "male",
          "company": "CEDWARD",
          "email": "dunlaphubbard@cedward.com",
          "phone": "+1 (890) 543-2508",
          "address": "169 Rutledge Street, Konterra, Northern Mariana Islands, 8551",
          "clients": {
            "id": "59761c23b30d971669fb42ff_updated3",
            "isActive": True,
            "age": 36,
            "name": "Dunlap Hubbard",
            "gender": "male",
            "company": "CEDWARD",
            "email": "dunlaphubbard@cedward.com",
            "phone": "+1 (890) 543-2508",
            "address": "169 Rutledge Street, Konterra, Northern Mariana Islands, 8551"
          }
        }
      }
    },
    {
      "id": "59761c233d8d0f92a6b0570d",
      "isActive": True,
      "age": 24,
      "name": "Kirsten Sellers",
      "gender": "female",
      "company": "EMERGENT",
      "email": "kirstensellers@emergent.com",
      "phone": "+1 (831) 564-2190",
      "address": "886 Gallatin Place, Fannett, Arkansas, 4656"
    },
    {
      "id": "59761c23fcb6254b1a06dad5",
      "isActive": True,
      "age": 30,
      "name": "Acosta Robbins",
      "gender": "male",
      "company": "ORGANICA",
      "email": "acostarobbins@organica.com",
      "phone": "+1 (882) 441-3367",
      "address": "697 Linden Boulevard, Sattley, Idaho, 1035"
    }
  ]
} 

print("Enter search string : ",end=" ")
search = input()
s = []
k=0
prevFlag = 0;
flag=0;
ptr = 0;
searchKey = ""
for i in range(0,len(search)):
    if search[i] == '/' and search[i+1] != '/':
        prevFlag = flag
        flag = i+1
        str = search[prevFlag:flag-1]
        str = str.replace('/','')
        s.insert(k,str)
        k+=k
    elif search[i] == '/' and search[i+1] == '/':
        ptr = i;
        searchKey = search[ptr+2:]
if ptr:
    s.reverse()
    strng = "MyDit"
    for i in range(0,len(s)):
        b = s[i]
        if b.isdigit():
            strng = strng + "[" + s[i] + "]"
        else:
            strng = strng + "[\"" + s[i] + "\"]"
    temp = eval(strng)
    if searchKey:
        while temp:
            try:
                print(temp["id"])
                temp = temp["clients"]
            except:
                break;
else:
    s.insert(k,search[flag:])
    s.reverse()
    strng = "print(MyDit"
    for i in range(0,len(s)):
        b = s[i]
        if b.isdigit():
            strng = strng + "[" + s[i] + "]"
        else:
            strng = strng + "[\"" + s[i] + "\"]"
    strng = strng + ")"
    exec(strng)
