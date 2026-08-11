
country_code={
    "India":91,
    "USA":1,
    "UK":44,
    "China":12,
    "France":3
    }
print(country_code)
print(country_code["USA"])
print(country_code["UK"])
print(country_code.get("China"))
country_code["China"]=100
print(country_code["China"])
print("i am printing with for loop")
for i in country_code:
    print(country_code[i])