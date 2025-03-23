"""
✅✅  Challenge #1
Create a class named Person with:

Properties:
    name (str)
    age (int)
    email (str)
A constructor to initialize these properties.
A __str__() method to return a nicely formatted string (e.g. "John Doe (35) <john@example.com>")
A method called get_info() that returns a dictionary of the person's attributes.

✅ Example Usage

p1 = Person("John Doe", 35, "john@example.com")
print(p1)  # Output: John Doe (35) <john@example.com>
print(p1.get_info())
# Output: {'name': 'John Doe', 'age': 35, 'email': 'john@example.com'}

✅ Learning Objectives
Define a class with properties
Write a constructor (__init__)
Use the __str__ method for clean printing
Return structured data using a dictionary

🔥 Optional Stretch
Add basic email validation:

If the email doesn't contain "@" and ".", raise a ValueError.

🧠 What’s Coming Next
Future challenges will expand this class to include:

Comparisons (e.g., sort people by age or name)
Filtering (e.g., find all people under 30)
Formatting (e.g., name capitalization)
Relationships (e.g., assigning people to vehicles or organizations)
Later: loading people from a file (TSV or JSON)

✅✅ Challenge #2: Validations & Formatting in the Person Class
You're going to:

✅ Improve formatting by capitalizing names automatically.
✅ Add basic input validation (email format, non-negative age).
✅ Practice raising exceptions for bad input.

* Format name: Strip leading and trailing spaces and capitalize each part of the name
* Age Validation: Raise a ValueError if age is negative
* Email Validation: Raise a ValueError if the email does not contain both "@" and "."

✅ Example Usage: p1 = Person("   john      DOE    ", 42, "john.doe@gmail.com")
* print(p1)  # Output: John Doe (42) <john.doe@gmail.com>

✅ Invalid examples:
* p2 = Person("Jane Smith", -5, "jane@example.com")
# Raises: ValueError("Age must be non-negative")

* p3 = Person("Bob Builder", 40, "bobbuilder_at_email.com")
# Raises: ValueError("Invalid email address")

✅ Enhancements made by Jeff
* Reduce intermediate spaces to one space within the name field by using a regEx.
* Email address muct contain exactly 1 @ sign.
* Email address must contain a . somewhere AFTER the @ sign

✅ Notes by Jeff:
* Following all required positional arguments, I can specify a '*' 
  to indicate that the remaining args MUST be keyword. 
  Otherwise all args can be posiional or keyword.
  Example:
    def __init__(self, name: str, *, age: int = 0, email: str = "")

✅ Question by Jeff:


🧠 Learning Goals
Reinforce __init__() customization
Use .strip() and .title() for string formatting
Use raise ValueError(...) to guard against bad data
Improve readability and robustness
✅ Your Task
Update your __init__() method to add these validations and formatting steps.
Add some tests in your main.py file to try both valid and invalid inputs.
Paste your updated Person class here when you're ready and I’ll give feedback!
"""

from utils.helper_functions import re


class Person:
    """Person"""

    def __init__(self, name: str, age: int = 0, email: str = "", vehicle=None):
        self.name = name.title().strip()
        self.name = re.sub(" +", " ", self.name)
        self.age = age
        self.email = email
        self.vehicle = vehicle

        if self.age < 0:
            raise ValueError(
                f"Invalid age — '{self.age}' — must be non-negative")
        if self.email.count("@") != 1:
            raise ValueError(
                f"Invalid email address — '{self.email}' — Must contain exactly 1 @ sign")
        if re.search(r"@.*\.", self.email) is None:
            raise ValueError(
                f"Invalid email address — '{self.email}' — Must contain a period after the @ sign")

    def __str__(self):
        """
        print(p1)  => John Doe (35) <john@example.com>
        print(p1.get_info()) => {'name': 'John Doe', 'age': 35, 'email': 'john@example.com'}
            """
        if self.vehicle is None:
            return f"{self.name} ({self.age}) <{self.email}> — doesn't drive"
        return f"{self.name} ({self.age}) <{self.email}> — drives a {self.vehicle}"
        # return f"{{'name': '{self.name}', 'age': {self.age}, 'email': '{self.email}'}}"

    def get_info(self):
        """
        returns a dictionary of the person's attributes.   
        """
        return {'name': self.name, 'age': self.age, 'email': self.email}
