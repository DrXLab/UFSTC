import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)
data1 = pd.read_csv("start_table.csv")
data2 = pd.read_csv("end_table.csv")
start_matrix = []
end_matrix = []
for i in range(0, len(data1)):
    rowdata = list(data1.loc[i])
    start_matrix.append(rowdata)
for i in range(0, len(data2)):
    rowdata = list(data2.loc[i])
    end_matrix.append(rowdata)


@app.route('/')
def index():
    return render_template('3DCube.html', data1=start_matrix, data2=end_matrix)


if __name__ == '__main__':
    app.run()
