# an introduction to OOP in python, let us try to model a restaurant, use the -- init -- method having 2 attributes
# that describes the restaurant and two methods in the class, then create instances of restaurants from the class

# creating the class Restaurant, This is just but the beginning of interesting OOP

class Restaurant(object):

    def __init__(self,restaurantName,restaurantLocation):

        self.restaurantName = restaurantName
        self.restaurantLocation= restaurantLocation

    def describeRestaurant(self):

        descriptionName =print("This Restaurant Is Called ",self.restaurantName.title() +" and it is found in "+self.restaurantLocation.title())
        return descriptionName

    def openRestaurant(self):

        printOpenStatus= print("You Have Opened The Restaurant Successfully! Congratulations")
        return  printOpenStatus
    numberServed =0

    def setNumberServed(self,numberServed):
        self.numberServed = numberServed

    def increamentNumberServed(self,increamentingValue):
        self.numberServed+=increamentingValue

# use the class to create three instances

myRestaurant = Restaurant('Breeze Restaurant','Kisumu')
assumptaRestaurant = Restaurant('Giko','Muranga')
isaiahRestaurant = Restaurant('Isayer Restaurant','Mombasa')

print(myRestaurant.describeRestaurant())
print(assumptaRestaurant.describeRestaurant())
print(isaiahRestaurant.describeRestaurant())

myRestaurant.setNumberServed(25)

print("I have Served ",myRestaurant.numberServed," clients till now in ",myRestaurant.restaurantName)

print("\nI have seen 5 more clients being served, let us increament the number of served clients: ")

myRestaurant.increamentNumberServed(5)

print("\nMy Restaurant Now has,",myRestaurant.numberServed, "clients who are served")


# we can as well use OOP to modify attribute values directly, but this is not the appropriate way of handling it


