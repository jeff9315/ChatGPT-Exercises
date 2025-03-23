"""
sort_people(people: list[Person], by: str) -> list[Person] that lets you sort by:

"name" — alphabetical

"age" — ascending

"vehicle_year" — newest to oldest (skip people with no vehicle)
"""

from models.person import Person


def sort_people(self, people: list[Person], by: str) -> list[Person]:
    """
sort_people(people: list[Person], by: str) -> list[Person] 
sort by:
  "name" — alphabetical
  "age" — ascending
  "vehicle_year" — newest to oldest (skip people with no vehicle)
"""
    self.people = people
    self.by = by
