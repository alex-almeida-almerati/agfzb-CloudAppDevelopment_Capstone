import requests
import json
# import related models here
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth


# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    api_key = kwargs.get("api_key")
    response = None

    try:
        if api_key:
            # Basic authentication GET
            # Call get method of requests library with URL, parameters and apikey
            params = dict()
            params["text"] = kwargs["text"]
            params["version"] = kwargs["version"]
            params["features"] = kwargs["features"]
            params["return_analyzed_text"] = kwargs["return_analyzed_text"]
            params["language"] = "en"
            response = requests.get(url, params=params, headers={'Content-Type': 'application/json'}, 
                                        auth=HTTPBasicAuth('apikey', api_key))
        else:
            # no authentication Get
            # Call get method of requests library with URL and parameters
            response = requests.get(url, headers={'Content-Type': 'application/json'},
                                        params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result
        
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer
            print("Dealer",dealer_doc)
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"], state=dealer_doc["state"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)

    return results


def get_dealers_by_id(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url, dealerId=dealerId)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result
        
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer
            print("Dealer",dealer_doc)
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"], state=dealer_doc["state"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)

    return results


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list
def get_dealer_reviews_from_cf(url, dealerId):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url, id=dealerId)
    if json_result:
        # Get the row list in JSON as dealer_reviews
        dealer_reviews = json_result
        
        # For each dealer_review object
        for review in dealer_reviews:
            # Get its content in `doc` object
            review_doc = review
            print("Review",review_doc)
            # Create a CarDealer object with values in `doc` object
            review_obj = DealerReview(id=review_doc["id"], name=review_doc["name"],
                            dealership=review_doc["dealership"],
                            review=review_doc["review"], purchase=review_doc["purchase"],
                            purchase_date=review_doc["purchase_date"], car_make=review_doc["car_make"],
                            car_model=review_doc["car_model"], car_year=review_doc["car_year"],
                            sentiment="")
            review_obj.sentiment = analyze_review_sentiments(review_obj.review)
            print("review:" + review_obj.review + "- sentiment: " + review_obj.sentiment)
            results.append(review_obj)

    return results


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
def analyze_review_sentiments(dealerreview):
    api_key = "xp3Ed1i0p0KNhQDm3GV28nm8Wgr9BkVTQiFG0hIgkk1F"
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/cc779099-cc54-4a67-89c3-70f932c9737a/v1/analyze"
    text = dealerreview
    version = "2022-04-07"
    features = "sentiment"
    return_analyzed_text = "false"
    json_result = get_request(url, api_key=api_key, text=text, version=version, features=features, return_analyzed_text=return_analyzed_text)
    # print(json_result)
    sentiment = json_result["sentiment"]["document"]["label"]
    return sentiment



