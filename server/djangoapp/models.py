from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100)
    description = models.CharField(null=False, max_length=100)
    
    def __str__(self):
        message = ("Name: " + self.name + "\n" \
                    + "Description: " + self.description)
        return message


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    COUPE = "Coupe"
    TYPE_CHOICES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon"),
        (COUPE, "Coupe")
    ]

    carMake = models.ForeignKey(CarMake, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=100)
    dealer_id = models.IntegerField()
    type = models.CharField(null=False, max_length=5, choices=TYPE_CHOICES, default=SEDAN)
    year = models.DateField(null=False)

    def __str__(self):
        message = ("Name: " + self.name + "\n"
                    + "Dealer Id: " + self.dealer_id + "\n"
                    + "Type: " + self.type + "\n"
                    + "Year: " + self.year)
        return message


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
