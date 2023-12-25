import random
import faker
from datetime import datetime, timedelta
import json

# Create a Faker instance
fake = faker.Faker()


# Function to generate a random date
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )


start_date = datetime(2020, 1, 1)
end_date = datetime(2022, 12, 31)

# Generate the data
data = []
for i in range(100):
    data.append(
        {
            "id": i,
            "title": fake.sentence(
                nb_words=3
            ),  # Generate a 3-word sentence as song title
            "performer": fake.name(),  # Generate a random name as artist name
            "peak_position": str(random.randint(1, 100)),
            "time_on_chart": str(random.randint(1, 52)),
            "chart_debut": random_date(start_date, end_date).strftime("%Y-%m-%d"),
        }
    )

# Write the data to a JSON file
with open("data.json", "w") as f:
    json.dump(data, f)
