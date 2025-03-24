"""
sort_people(people: list[Person], by: str) -> list[Person]
filter_people_by_vehicle(people: list[Person], make, model, year)
"""

from typing import Literal

# from models import person
from models.person import Person

# from models.vehicle import Vehicle


def sort_people(people: list[Person],
                sort_by: Literal["name", "age", "vehicle_year"]) -> list[Person]:
    """
sort_people(people: list[Person], by: str) -> list[Person]
sort by:
  "name" — alphabetical
  "age" — ascending
  "vehicle_year" — newest to oldest (skip people with no vehicle)
"""
    if sort_by.lower() == "name":
        people.sort(key=lambda person: person.name)
        return people

    if sort_by.lower() == "age":
        people.sort(key=lambda person: person.age)
        return people
        

    if sort_by.lower() == "vehicle_year":
        people = [person for person in people if person.vehicle is not None]
        people.sort(key=vehicle_year_key, reverse=True)
        return people

    raise ValueError(f"Invalid Value in sort-by parameter: {sort_by} ")
    # print(f"An error occurred -- Invalid: 'by={sort_by}'.")
    # return {}


def vehicle_year_key(person: Person) -> int:
    """
    Helper function to get a vehicle's year or 1700 if they don't have a car
    """
    if person.vehicle is None:
        return 1700   # Defensive programming so that people without cars are at the end of the list
    return person.vehicle.year




