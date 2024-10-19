products = [
{
"id": 1,
"name": "IPHONE 13",
"category": "Electronics",
"price" : 2500,
"colors" : ["gray", "black"],
"size": ["small", "medium", "large"],
"stock": [{
"gray-small" : 25,
"gray-medium" : 30,
"gray-large" : 34
},
{
"black-small": 23,
"black-medium": 23,
"black-large": 25
}],
},

{
"id": 2,
"name": "IPHONE 15",
"category":"Electronics",
"price" : 2500,
"colors" : ["gray", "black"],
"size": ["small", "medium", "large"],
"stock": [{
"gray-small" : 25,
"gray-medium" : 30,
"gray-large" : 34
},
{
"black-small": 23,
"black-medium": 23,
"black-large": 25
}],
},

{
"id": 3,
"name": "IPHONE 16",
"category":"Electronics",
"price" : 2500,
"colors" : ["gray", "black"],
"size": ["small", "medium", "large"],
"stock": [{
"gray-small" : 25,
"gray-medium" : 30,
"gray-large" : 34
},
{
"black-small": 23,
"black-medium": 23,
"black-large": 25
}],
}
]

print(products)
products[2]["name"] = "IPHONE 16 PROMAX"
print ("")

#TODO ACCESS STOCK OF products[2]	
print("Accessing stock of Product 2")
print(products[2]["stock"])
print("")

#TODO ACCESS INDEX 3 STOCK OF products[2]
print("Accessing index 3 of stock in products")
print(products[2]["stock"][0])
print("")

#TODO CHANGE black small quantity - products[2]
products[2]["stock"][black_small_index]["black-small"] = 20
print("Updated stock for Product #3:")
print(products[2]["stock"])
black_small_index = 1  

 

 

 

 