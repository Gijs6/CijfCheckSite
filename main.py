from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read().strip()


@app.route("/check/cijfer")
def cijfcheck():
    try:
        score = float(read_file('score.txt'))
    except ValueError:
        score = read_file('score.txt') # If grades aren't a number but a letter or something
    
    subject = read_file('subject.txt')
    test_name = read_file('test_name.txt')
    date_time_file = datetime.strptime(read_file('datetime.txt'), "%d/%m/%Y %H:%M:%S")
    date = date_time_file.strftime("%a %d %b %Y")
    time = date_time_file.strftime("%H:%M:%S")
    new_average = read_file('new_average.txt')
    data = {
        "score": score,
        "subject": subject,
        "test_name": test_name,
        "date": date,
        "time": time,
        "new_average": new_average,
    }
    return render_template('check.html', data=data)


if __name__ == '__main__':
    app.run()
