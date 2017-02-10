import csv

with open('tester_filt_2_short.csv') as ListOfLists:
    for InternalList in ListOfLists:
        # if InternalList.rfind('"')
        iList = InternalList.split()
        print(' ************* START OF INTERNAL LIST ************* ')
        print(iList)
        for item in iList:
            print(item)
        print(' ************* END OF INTERNAL LIST ************* ')


