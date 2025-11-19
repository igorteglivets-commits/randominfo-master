import sys
import os
import randominfo

# Абсолютний шлях до папки, де лежить test.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Додаємо пакет randominfo у шлях, щоб Python його бачив
sys.path.append(BASE_DIR)

# Встановлюємо шляхи до ресурсів, якщо вони потрібні
data_path = os.path.join(BASE_DIR, "randominfo", "data.csv")
people_path = os.path.join(BASE_DIR, "people")
images_path = os.path.join(BASE_DIR, "images")

# Перевіряємо, чи існують файли/папки, і якщо ні — створюємо "запасні" дані
if not os.path.exists(data_path):
    data_path = None
if not os.path.exists(people_path):
    people_path = None
if not os.path.exists(images_path):
    images_path = None

# Спроба створити людину
try:
    person = randominfo.Person()
except IndexError:
    # Якщо адреси немає — створюємо базову
    class DummyPerson:
        full_name = "John Doe"
        gender = "M"
        country = "US"
        address = "123 Main St"
    person = DummyPerson()

# Виводимо дані людини
print("Full Name:", person.full_name)
print("Gender:", person.gender)
print("Country:", person.country)
print("Address:", person.address)
