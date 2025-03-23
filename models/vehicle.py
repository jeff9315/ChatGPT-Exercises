""" 
Vehicle Class

✅✅ Challenge  # 3: Introduce a Vehicle Class
🔧 Your Task:
* Create a Vehicle class with:
    * make(str)
    * model(str)
    * year(int)
* Add a vehicle property to the Person class that stores a Vehicle object ( or None by default).
* Update __str__() in Person to include the vehicle if available.

✅ Example ... in main()
car = Vehicle("Toyota", "Camry", 2020)
jeff = Person("Jeff Miller", age=45, email="jeff@example.com", vehicle=car)
print(jeff)

🖨 Expected Output
Jeff Miller(45) < jeff@example.com > — drives a 2020 Toyota Camry

🧠 Design Notes:
* Keep Vehicle simple for now—we’ll expand it later.
* Don’t worry yet about validating the year or adding VINs.
* Allow Person(..., vehicle=None) if they don’t have a vehicle.

🔥 Bonus(Optional):
* Add a __str__() method in Vehicle so printing it returns:
  "2020 Toyota Camry"

Ready to give it a try ? 
Create your Vehicle class and update your Person class to accept a vehicle. 
Then show me your updated test output! I’ll review it when you’re done. 🚀

"""


class Vehicle:
    """
    Vehicle
    """

    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
