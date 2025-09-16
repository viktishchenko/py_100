datas = {
    "data" : [ {
    "type" : "location",
    "subType" : "city",
    "name" : "Paris",
    "iataCode" : "PAR",
    "address" : {
      "countryCode" : "FR",
      "stateCode" : "FR-75"
    },
    "geoCode" : {
      "latitude" : 48.85341,
      "longitude" : 2.3488
    },
    "relationships" : [ {
      "id" : "BVA",
      "type" : "Airport",
      "href" : "#/included/airports/BVA"
    }, {
      "id" : "CDG",
      "type" : "Airport",
      "href" : "#/included/airports/CDG"
    }, {
      "id" : "ORY",
      "type" : "Airport",
      "href" : "#/included/airports/ORY"
    }, {
      "id" : "XCR",
      "type" : "Airport",
      "href" : "#/included/airports/XCR"
    } ]
  }, {
    "type" : "location",
    "subType" : "city",
    "name" : "Le Touquet-Paris-Plage",
    "iataCode" : "LTQ",
    "address" : {
      "countryCode" : "FR",
      "stateCode" : "FR-62"
    },
    "geoCode" : {
      "latitude" : 50.52432,
      "longitude" : 1.58571
    },
    "relationships" : [ {
      "id" : "LIL",
      "type" : "Airport",
      "href" : "#/included/airports/LIL"
    } ]
  } ],
  "included" : {
    "airports" : {
      "XCR" : {
        "subType" : "Airport",
        "name" : "Chalons-Vatry",
        "iataCode" : "XCR",
        "address" : {
          "countryCode" : "FR",
          "stateCode" : "FR-75"
        },
        "geoCode" : {
          "latitude" : 48.77611,
          "longitude" : 4.18444
        }
      },
      "CDG" : {
        "subType" : "Airport",
        "name" : "Charles de Gaulle",
        "iataCode" : "CDG",
        "address" : {
          "countryCode" : "FR",
          "stateCode" : "FR-75"
        },
        "geoCode" : {
          "latitude" : 49.01278,
          "longitude" : 2.55
        }
      },
      "ORY" : {
        "subType" : "Airport",
        "name" : "Orly",
        "iataCode" : "ORY",
        "address" : {
          "countryCode" : "FR",
          "stateCode" : "FR-75"
        },
        "geoCode" : {
          "latitude" : 48.72528,
          "longitude" : 2.35944
        }
      },
      "BVA" : {
        "subType" : "Airport",
        "name" : "Beauvais-Tille",
        "iataCode" : "BVA",
        "address" : {
          "countryCode" : "FR",
          "stateCode" : "FR-75"
        },
        "geoCode" : {
          "latitude" : 49.45444,
          "longitude" : 2.11278
        }
      },
      "LIL" : {
        "subType" : "Airport",
        "name" : "Lesquin",
        "iataCode" : "LIL",
        "address" : {
          "countryCode" : "FR",
          "stateCode" : "FR-59"
        },
        "geoCode" : {
          "latitude" : 50.57037,
          "longitude" : 3.10643
        }
      }
    }
  }
}
# print(f'datas["data"]>>> {datas["data"]}')
# [{'type': 'location', 'subType': 'city', 'name': 'Paris', 'iataCode': 'PAR', 'address': {'countryCode': 'FR', 'stateCode': 'FR-75'}, 'geoCode': {'latitude': 48.85341, 
# 'longitude': 2.3488}, 'relationships': [{'id': 'BVA', 'type': 'Airport', 'href': '#/included/airports/BVA'}, {'id': 'CDG', 'type': 'Airport', 'href': '#/included/airports/CDG'}, {'id': 'ORY', 'type': 'Airport', 'href': '#/included/airports/ORY'}, {'id': 'XCR', 'type': 'Airport', 'href': '#/included/airports/XCR'}]}, {'type': 'location', 'subType': 'city', 'name': 'Le Touquet-Paris-Plage', 'iataCode': 'LTQ', 'address': {'countryCode': 'FR', 'stateCode': 'FR-62'}, 'geoCode': {'latitude': 50.52432, 'longitude': 1.58571}, 'relationships': [{'id': 'LIL', 'type': 'Airport', 'href': '#/included/airports/LIL'}]}]
# print(f'datas["included"]>>> {datas["included"]}')
# {'airports': {'XCR': {'subType': 'Airport', 'name': 'Chalons-Vatry', 'iataCode': 'XCR', 'address': {'countryCode': 'FR', 'stateCode': 'FR-75'}, 'geoCode': {'latitude': 48.77611, 'longitude': 4.18444}}, 'CDG': {'subType': 'Airport', 'name': 'Charles de Gaulle', 'iataCode': 'CDG', 'address': {'countryCode': 'FR', 'stateCode': 'FR-75'}, 'geoCode': 
# {'latitude': 49.01278, 'longitude': 2.55}}, 'ORY': {'subType': 'Airport', 'name': 'Orly', 'iataCode': 'ORY', 'address': {'countryCode': 'FR', 'stateCode': 'FR-75'}, 'geoCode': {'latitude': 48.72528, 'longitude': 2.35944}}, 'BVA': {'subType': 'Airport', 'name': 'Beauvais-Tille', 'iataCode': 'BVA', 'address': {'countryCode': 'FR', 'stateCode': 'FR-75'}, 'geoCode': {'latitude': 49.45444, 'longitude': 2.11278}}, 'LIL': {'subType': 'Airport', 'name': 'Lesquin', 'iataCode': 'LIL', 'address': {'countryCode': 'FR', 'stateCode': 'FR-59'}, 'geoCode': {'latitude': 50.57037, 'longitude': 3.10643}}}}

# Status code 200. Airport IATA: {
#   "meta" : {
#     "count" : 33,
#     "links" : {
#       "self" : "https://test.api.amadeus.com/v1/reference-data/locations/cities?keyword=PARIS&max=1000"
#     }
#   },

# Status code 200. Airport IATA: {
#   "meta" : {
#     "count" : 2,
#     "links" : {
#       "self" : "https://test.api.amadeus.com/v1/reference-data/locations/cities?include=AIRPORTS&keyword=PARIS&max=2"
#     }
#   },