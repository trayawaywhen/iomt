from models import Session, JsonData

from io import BytesIO
import base64

from matplotlib.figure import Figure
from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a session
session = Session()

# Query the database for all JSON data
all_data = session.query(JsonData).all()

session.close()

# Print the extracted data
for item in all_data:
    print(f"ID: {item.id}, Data: {item.data}")


def sensor_data_graph():
    sensor_data = all_data()
    residents = sensor_data['residents']
    falls = sensor_data['falls']

    fig = Figure()
    ax = fig.add_subplot()

    bar_labels = residents

    ax.bar(residents, falls, label=bar_labels)

    ax.set_ylabel('Antal fald')
    ax.set_title('Fald')
    ax.legend(title='Beboere')

    buf = BytesIO()

    fig.savefig(buf, format='png')

    return base64.b64encode(buf.getbuffer()).decode('ascii')





def graph():
    fig = Figure()
    ax = fig.add_subplot()

    persons = ['Bjarne', 'Lis', 'Inge', 'Børge']
    counts = [40, 100, 30, 55]
    bar_labels = ['Bjarne', 'Lis', 'Inge', 'Børge']
    bar_colors = ['tab:pink', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(persons, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('Antal fald')
    ax.set_title('Fald')
    ax.legend(title='Personer')

    buf = BytesIO()

    fig.savefig(buf, format='png')

    return base64.b64encode(buf.getbuffer()).decode('ascii')