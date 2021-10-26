
# unordered Linear Search, search the position of a given value in an unsorted list

def linearSearch(listToSearch,searchValue):
    for index,i in enumerate(listToSearch):
        if i == searchValue:
            return index
    return -1

#ordered Linear Search, search the position of a given value in a sorted list

# This function determined if an item is in a given sorted list, You can Also return the index position where the item is located

def orderedLinearSearch(listToSearch,searchValue):
    for item in listToSearch:
        if item == searchValue:
            return True
        elif item > searchValue:
            return False

# Let us Try This in main

ourListOfNumbers =[11,23,45,26,47,38,39,45,34]

search1 =23

print(f"The number {search1} is found at index {linearSearch(ourListOfNumbers,search1)}")
ourListOfNumbers.sort() 
print("Item Found On List ") if orderedLinearSearch(ourListOfNumbers,search1) == True else print("Item Not Found")
