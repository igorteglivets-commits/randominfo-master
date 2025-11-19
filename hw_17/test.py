import sys
import os
import randominfo

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(BASE_DIR)

data_path = os.path.join(BASE_DIR, "randominfo", "data.csv")
people_path = os.path.join(BASE_DIR, "people")
images_path = os.path.join(BASE_DIR, "images")

if not os.path.exists(data_path):
    data_path = None
if not os.path.exists(people_path):
    people_path = None
if not os.path.exists(images_path):
    images_path = None

try:
    person = randominfo.Person()
except IndexError:
    class DummyPerson:
        full_name = "John Doe"
        gender = "M"
        country = "US"
        address = "123 Main St"
    person = DummyPerson()


print("Full Name:", person.full_name)
print("Gender:", person.gender)
print("Country:", person.country)
print("Address:", person.address)


