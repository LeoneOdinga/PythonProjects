'''Global Variables'''
auxArray=[]  # list to hold the kth largest elements to be returned
copyArray =[] # A Copy Of The Original List

'''==================Beginning Function Declarations================'''
# function to check if value entered not exceed number of elements
def valueOfKIsValid(validK,array):
    if (validK> len(array)):
        return False
    return True

#function to filter the top k largest elements from the list passed
def returnMax(listOfNumbers,k):
    if not valueOfKIsValid(k,listOfNumbers):
        print("The value of K cannot exceed ",len(listOfNumbers))
        exit()
    while(k <=len(listOfNumbers)):
        listOfNumbers.sort(reverse=True)
        counter = 0
        while counter < k:
            auxArray.append(listOfNumbers[counter])
            counter += 1
        break

#function to fill in the list with user's input
def userFillArray(array,size):
    count = 1
    while count <= size:
        array.append(int(input("Enter Value For Element:" + str(count) + " ")))
        count += 1

#linear search function to search the position of a given element
def linearSearch(arrayToSearch,searchValue):
    for index,i in enumerate(arrayToSearch):
        if i == searchValue:
            return index
    return -1

#function to write the number output in form of ordinals i.e 1st,2nd,3rd
SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
def ordinal(num):
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = SUFFIXES.get(num % 10, 'th')
    return str(num) + suffix
'''==================End Of Function DEclarations===================='''

'''===========================Output Section=========================='''

list =[] # declare an empty list. User will use to enter his/her desired values. We can also generate a random list

numberOfElements=int(input("Enter The Number Of Elements In The Array(Size Of Array): "))

input("Proceed To Fill The Array List With The "+str(numberOfElements)+" Elements.Press Enter To Proceed...")

userFillArray(list,numberOfElements)

copyArray = list.copy()

valueOfK = int(input("How Many Top Largest Elements Do You Want To Show ?"))

print("Showing Top "+str(valueOfK)+" Largest Elements: ") if valueOfKIsValid(valueOfK,list) else print("Error! Cannot Show Results!")
print(returnMax(list,valueOfK))

for index,i in enumerate(auxArray):
    print(ordinal(index+1),"Largest Number is ",i," And Is Found At Index(Position) ",linearSearch(copyArray,i))

    '''===========================End Of Output Section=================='''

    '''
    using dictionaries,store information about the lust and the related position in the list, then using a searching algorithm, find the associated index in the dictionary using the key attribute
    '''
