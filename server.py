import json
from models import Session, JsonData

# Create a session
session = Session()

# Example JSON data
data_to_insert = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}


def extract_from_broker():
    try:
        messsage = subscribe.simple("paho/test/topic", hostname="192.168.1.100")
        result = json.loads(message.payload.decode())
        return result
    except Exception:
        return Exception


# Create a new JsonData instance
json_data = JsonData(data=data_to_insert)

# Add and commit the new data
session.add(json_data)
session.commit()
session.close()

print("Data inserted successfully.")
