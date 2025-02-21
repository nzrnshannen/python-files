import json
from faker import Faker

fake = Faker()
Faker.seed(54321)

num_of_stores = 100

stores_data = []
for i in range(1, num_of_stores + 1):
    store = {
        "id": i,  
        "name": fake.company(),
        "location": fake.address(),
        "image_url": fake.image_url(width=640, height=480),  
        "rating": round(fake.pyfloat(left_digits=1, right_digits=2, min_value=3.0, max_value=5.0), 2),
        "membership_link": fake.url(),
        "points": fake.random_int(min=1, max=1000)
    }
    stores_data.append(store)

with open('test_dummy.json', 'w') as json_file:
    json.dump(stores_data, json_file, indent=4)

print("Data saved to test_dummy.json")
