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
    
    carMake = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=100)
    dealer_id = models.IntegerField()
    type = models.CharField(null=False, max_length=5, choices=TYPE_CHOICES, default=SEDAN)
    year = models.DateField(null=False)

    def __str__(self):
        message = ("Name: " + self.name + "\n"
                    + "Dealer Id: " + str(self.dealer_id) + "\n"
                    + "Type: " + self.type + "\n"
                    + "Year: " + str(self.year))
        return message


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, id, city, state, st, address, zip, lat, long, short_name, full_name):
        # Dealer id
        self.id = id
        # Dealer city
        self.city = city
        # Dealer state
        self.state = state
        # Dealer st
        self.st = st
        # Dealer address
        self.address = address
        # Dealer zip
        self.zip = zip
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer full name
        self.full_name = full_name

    def __str__(self):
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        # DealerReview dealership
        self.dealership = dealership
        # DealerReview name
        self.name = name
        # DealerReview purchase
        self.purchase = purchase
        # DealerReview review
        self.review = review
        # DealerReview purchase_date
        self.purchase_date = purchase_date
        # Location car_make
        self.car_make = car_make
        # Location car_model
        self.car_model = car_model
        # DealerReview car_year
        self.car_year = car_year
        # DealerReview sentiment
        self.sentiment = sentiment
        # DealerReview id
        self.id = id

    def __str__(self):
        return "DealerReview review: " + self.review

