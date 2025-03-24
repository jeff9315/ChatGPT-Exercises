from models.person import Person


def filter_people_by_vehicle(people: list[Person], make: str = None, model: str = None,

                             year: int = None) -> list[Person]:
    """
    Filter people by any combination of make, model, vehicle year.
    If an attribute value is 'None' ignore it.
    """
    def _filter_people_vehicle_by_make(people: list[Person]) -> list[Person]:
        """"""
        return people

    def _filter_people_vehicle_by_model(people: list[Person]) -> list[Person]:
        """"""
        return people

    def _filter_people_vehicle_by_year(people: list[Person]) -> list[Person]:
        """"""
        return people

    if make is not None:
        _filter_people_vehicle_by_make(people)
        return people
    if model is not None:
        _filter_people_vehicle_by_model(people)
        return people
    if year is not None:
        _filter_people_vehicle_by_year(people)
        return people