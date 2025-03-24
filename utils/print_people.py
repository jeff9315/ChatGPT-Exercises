from models.person import Person


def print_people(people: list[Person]):
    """Prints a list of Person objects."""
    for person in people:
        print(person)