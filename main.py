"""Main"""

from models.person import Person
from models.vehicle import Vehicle
from utils.helper_functions import startup
from utils.print_people import print_people
from utils.sort_people import sort_people

startup()

# Vehicles
car1 = Vehicle("Toyota", "Camry", 2020)
car2 = Vehicle("Honda", "Accord", 2018)
car3 = Vehicle("Tesla", "Model 3", 2022)

# People
people = [
    Person("    Jeff     Miller    ", age=45,
           email="jeff@example.com", vehicle=car1),
    Person("    Jeff     Miller    ", age=45,
           email="jeff@example.com", vehicle=car1),
    Person("Alice Johnson", age=30, email="alice@example.com", vehicle=car3),
    Person("Bob Smith", age=50, email="bob@example.com", vehicle=car2),
    Person("Cathy Brown", age=22, email="cathy@example.com"),
    Person("Dan Adams", age=35, email="dan@example.com"),
]

print("\n\n===== People By Name =====")
print_people(sort_people(people, sort_by="name"))

print("\n\n===== People By Age ===== ")
print_people(sort_people(people, sort_by="age"))


print("\n\n===== People By Descending Vehicle Date ===== ")
try:
    print_people(sort_people(people, sort_by="vehicle_year"))
except Exception as e:
    print(e)


try:
    print("\n========== P1 =====\n")
    car = Vehicle("Toyota", "Camry", 2020)
    jeff = Person("Jeff Miller", age=45, email="jeff@example.com", vehicle=car)
    janice = Person("Janice Joplin", age=12, email="janice@example.com")
    print(jeff)
    print(car)
    print(janice)
except ValueError as e:
    print("❌ Error creating person or car:", e)
    print('a')


try:
    print("\n======= P0 ========\n")
    p0 = Person("John Doe")
    print(p0)
    print(f"{p0.get_info()}")
except ValueError as e:
    print("❌ Error creating person:", e)


try:
    print("\n========== P1 =====\n")
    person = Person("    John      Doe     ", email="john@example.com", age=35)
    print(person)
    print(f"{person.get_info()}")
except ValueError as e:
    print("❌ Error creating person:", e)
    print('a')


try:
    print("\n========== P2 =====\n")
    person = Person("    John      Doe     ", -0, "john@example.com")
    print(person)
    print(f"{person.get_info()}")
except ValueError as e:
    print("❌ Error creating person:", e)

try:
    print("\n========== P3 =====\n")
    person = Person("    John      Doe     ", 35, "john@example.com")
    print(person)
    print(f"{person.get_info()}")
except ValueError as e:
    print("❌ Error creating person:", e)

try:
    print("\n========== P4 =====\n")
    person = Person("    John      Doe     ", 35, "john.jones@example.com")
    print(person)
    print(f"{person.get_info()}")
except ValueError as e:
    print("❌ Error creating person:", e)

try:
    print("\n========== ERR1 =====\n")
    person = Person("    John      Doe     ", -7, "john@example.com")
    print(person)
    print(f"{person.get_info()}")
except ValueError as e:
    print("❌ Error creating person:", e)

try:
    print("\n========== ERR2 =====\n")
    person = Person("    John      Doe     ", 35, "john@exa@mple.com")
    print(person)
    print(f"{person.get_info()}")
except ValueError as e:
    print("❌ Error creating person:", e)

try:
    print("\n========== ERR3 =====\n")
    person = Person("    John      Doe     ", 35, "johnexample.com")
    print(person)
    print(f"{person.get_info()}")
except ValueError as e:
    print("❌ Error creating person:", e)

try:
    print("\n========== ERR4 =====\n")
    person = Person("    John      Doe     ", 35, "john.jones@examplecom")
    print(person)
    print(f"{person.get_info()}")
except ValueError as e:
    print("❌ Error creating person:", e)


