from io import BytesIO
import base64

from matplotlib.figure import Figure

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