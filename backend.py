import json
from flask import Flask
from flask_cors import CORS
from bokeh.embed import json_item
from bokeh.plotting import figure

app = Flask(__name__)
CORS(app)

x = [1, 2, 3, 4, 5]
y1 = [6, 7, 2, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [4, 5, 5, 7, 2]

def make_plot():
	p = figure(title="Multiple line example", x_axis_label="x", y_axis_label="y")
	p.line(x, y1, legend_label="Temp.", line_color="blue", line_width=2)
	p.line(x, y2, legend_label="Rate", line_color="red", line_width=2)
	p.line(x, y3, legend_label="Objects", line_color="green", line_width=2)
	return p

@app.route("/")
def root():
	p = make_plot()
	return json.dumps(json_item(p))

if __name__ == "__main__":
	app.run()
