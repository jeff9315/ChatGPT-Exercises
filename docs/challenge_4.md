# Challenge #4: Filtering and Sorting People (with and without Vehicles)
We'll break this into two parts:

## 🔹 Part 1: Sorting People
Write a function sort_people(people: list[Person], by: str) -> list[Person] that lets you sort by:
  * "name" — alphabetical
  * "age" — ascending
  * "vehicle_year" — newest to oldest (skip people with no vehicle)

📌 Example usage:
```
sorted_by_name = sort_people(people, by="name")
sorted_by_age = sort_people(people, by="age")
sorted_by_vehicle = sort_people(people, by="vehicle_year")
```

## Sample Input
```
# Vehicles
car1 = Vehicle("Toyota", "Camry", 2020)
car2 = Vehicle("Honda", "Accord", 2018)
car3 = Vehicle("Tesla", "Model 3", 2022)

# People
people = [
    Person("Jeff Miller", age=45, email="jeff@example.com", vehicle=car1),
    Person("Alice Johnson", age=30, email="alice@example.com", vehicle=car3),
    Person("Bob Smith", age=50, email="bob@example.com", vehicle=car2),
    Person("Cathy Brown", age=22, email="cathy@example.com"),
    Person("Dan Adams", age=35, email="dan@example.com"),
]
```
## Expected Output
🔹 sort_people(people, by="name")
```
Alice Johnson (30) <alice@example.com> — drives a 2022 Tesla Model 3  
Bob Smith (50) <bob@example.com> — drives a 2018 Honda Accord  
Cathy Brown (22) <cathy@example.com> — doesn't drive  
Dan Adams (35) <dan@example.com> — doesn't drive  
Jeff Miller (45) <jeff@example.com> — drives a 2020 Toyota Camry  
```
🔹 sort_people(people, by="age")
```
Cathy Brown (22) <cathy@example.com> — doesn't drive  
Alice Johnson (30) <alice@example.com> — drives a 2022 Tesla Model 3  
Dan Adams (35) <dan@example.com> — doesn't drive  
Jeff Miller (45) <jeff@example.com> — drives a 2020 Toyota Camry  
Bob Smith (50) <bob@example.com> — drives a 2018 Honda Accord  
```
🔹 sort_people(people, by="vehicle_year")
```
Alice Johnson (30) <alice@example.com> — drives a 2022 Tesla Model 3  
Jeff Miller (45) <jeff@example.com> — drives a 2020 Toyota Camry  
Bob Smith (50) <bob@example.com> — drives a 2018 Honda Accord  
```

## 🔹 Part 2: Filtering People
Write a function filter_people_by_vehicle(people: list[Person], make: str = None, model: str = None, year: int = None) -> list[Person]

It returns a list of people whose vehicle matches the given filter.

Any combination of filters can be passed

If a filter is None, ignore it

📌 Example usage:

```
toyota_owners = filter_people_by_vehicle(people, make="Toyota")
honda_2018 = filter_people_by_vehicle(people, make="Honda", year=2018)
```

📌 Expected output:
```
Jeff Miller (45) <jeff@example.com> — drives a 2020 Toyota Camry
```
## 🧠 Learning Goals:
Lambda functions or key= for sorting

Using isinstance() or hasattr() to check for a Vehicle

Optional keyword filtering

Clean separation of logic into helper functions

## ✅ Your Task:
Add the sort_people() and filter_people_by_vehicle() functions.

Test with a list of people (some with vehicles, some without).


