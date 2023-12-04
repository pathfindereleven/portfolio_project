import requests

url = "https://mp-search-api.tcgplayer.com/v1/search/request?q=&isList=false&mpfev=2017"

data = {
    "algorithm": "sales_exp_fields_experiment",
    "from": 100,
    "size": 50,
    "filters": {
        "term": {},
        "range": {},
        "match": {}
    },
    "listingSearch": {
        "context": {
            "cart": {}
        },
        "filters": {
            "term": {
                "sellerStatus": "Live",
                "channelId": 0,
                "sellerKey": [
                    "bb74f3e2"
                ]
            },
            "range": {
                "quantity": {
                    "gte": 1
                }
            },
            "exclude": {
                "channelExclusion": 0
            }
        }
    },
    "context": {
        "cart": {},
        "shippingCountry": "US"
    },
    "settings": {
        "useFuzzySearch": True,
        "didYouMean": {}
    },
    "sort": {}
}


x =requests.post(url, json = data) 
print(x.text)