Direction = ['Ishan','Vyavya','Nirutya','Agney']
Tourism_dict = {
    'Ishan' : [{'Palace_Name' : 'Ita Fort','isTaken' : False},
               {'Palace_Name' : 'Bhimaknagar Fort','isTaken': True},
               {'Palace_Name' : 'Lalgarh', 'isTaken': False },
               {'Palace_Name' : 'Chandramahal','isTaken': True},
               {'Palace_Name' : 'Matibag Palace','isTaken': True}
              ],
    'Vyavya' : [{'Palace_Name': 'City Palace','isTaken': False },
                {'Palace_Name': 'Hawa Mahal','isTaken': False},
                {'Palace_Name': 'Jal Mahal','isTaken':True},
                {'Palace_Name': 'Bikaner Fort','isTaken':True},
                {'Palace_Name': 'AchalGarh Fort','isTaken':True},
                {'Palace_Name': 'Jhalawar Fort','isTaken':False},
                {'Palace_Name': 'Akabri Fort','isTaken':False},
                {'Palace_Name': 'Lake Place','isTaken':True},
                {'Palace_Name': 'Gobindgarh','isTaken':True},
                {'Palace_Name': 'AkhnoorFort','isTaken':True},
                {'Palace_Name': 'QilaMubarak','isTaken':False},
                {'Palace_Name': 'FirozaShah Palace','isTaken':False},
                {'Palace_Name': 'Sisra Fort','isTaken':False}
              ],
    'Nirutya' : [{'Palace_Name': 'Bhujia Fort','isTaken': False },
                 {'Palace_Name': 'Surat Castle','isTaken': False },
                 {'Palace_Name': 'Uparkot Fort','isTaken': True },
                 {'Palace_Name': 'Chatarpati Shivaji Parnera Fort','isTaken': True },
                 {'Palace_Name': 'Maharaj Sayajirav Gaikwad Fort','isTaken': True },
                 {'Palace_Name': 'Shivneri Fort','isTaken': False },
                 {'Palace_Name': 'Lohagad Fort','isTaken': False },
                 {'Palace_Name': 'Murud Janjira','isTaken': False },
                 {'Palace_Name': 'Suvarnadurg','isTaken': True },
              ],
    'Agney' : [{'Palace_Name': 'Barabti Fort','isTaken': False },
                {'Palace_Name': 'Chundanag Gada Fort','isTaken': False },
                {'Palace_Name': 'Old Fort','isTaken': True},
                {'Palace_Name': 'Vellore Fort','isTaken': True},
                {'Palace_Name': 'Bobbili Fort','isTaken': True}
               ]
}
def guide(choice):
    if choice == 1:
        palace = Tourism_dict['Ishan']
        for i in range(0,len(palace)):
            if palace[i]['isTaken'] == False:
                print(palace[i]['Palace_Name'])
    elif choice == 2:
        palace = Tourism_dict['Vyavya']
        for i in range(0,len(palace)):
            if palace[i]['isTaken'] == False:
                print(palace[i]['Palace_Name'])
    elif choice == 3:
        palace = Tourism_dict['Nirutya']
        for i in range(0,len(palace)):
            if palace[i]['isTaken'] == False:
                print(palace[i]['Palace_Name'])
    elif choice == 4:  
       palace = Tourism_dict['Agney']
       for i in range(0,len(palace)):
           if palace[i]['isTaken'] == False:
               print(palace[i]['Palace_Name'])
    else:
        for dirName in Direction:
            palace = Tourism_dict[dirName]
            for i in range(0,len(palace)):
                if palace[i]['isTaken'] == False :
                    print(palace[i]['Palace_Name'])
                            
print("\n Welcome !!\n")
print(" Select Any One Direction")
print(" 1. North East India \n 2. North West India \n 3. South West India \n 4. South East India \n 5. All India")
print("Enter any direction from above :")
choice = int(input())
print("\nForts Avilable in Your Direction :")
guide(choice)
