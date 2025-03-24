"""
sort_people(people: list[Person], by: str) -> list[Person]
print_people(people: list[Person]
"""

from models.person import Person


def sort_people(people: list[Person], by: str) -> list[Person]:
    """
sort_people(people: list[Person], by: str) -> list[Person]
sort by:
  "name" — alphabetical
  "age" — ascending
  "vehicle_year" — newest to oldest (skip people with no vehicle)
"""
    if by.lower() == "name":
        people.sort(key=lambda person: person.name)
        return people

    if by.lower() == "age":
        people.sort(key=lambda person: person.age)
        return people

    if by.lower() in ["vehicle_year", "vehicle year", "year", "vehicle"]:
        people = [person for person in people if person.vehicle is not None]
        people.sort(key=vehicle_year_key, reverse=True)
        return people

    print(f"An error occurred -- Invalid: 'by={by}'.")
    return {}


def print_people(names: list[Person]):
    """
    print a list of people
    """
    for person in names:
        print(person)


def vehicle_year_key(person: Person) -> Person:
    """
    Helper function to get a vehicle's year or 1700 if they don't have a car
    """
    if person.vehicle is None:
        return 1700   # Defensive programming so that people without cars are at the end of the list
    return person.vehicle.year
