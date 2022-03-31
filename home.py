from flask import Flask

myapp_obj = Flask(__name__)

name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

@myapp_obj.route("/")
def home():
	return '''
	<html>
	<body>
		<h1>Welcome'''+name+'''!<h1>

		<ahref="www.google.com">notgoogle</a>

		<ul>
			<li>''' + city_names[0] + '''</li>
			<li>''' + city_names[1] + '''</li>
			<li>''' + city_names[2] + '''</li>
			<li>''' + city_names[3] + '''</li>
		</ul>
	</body>
	</html>'''

myapp_obj.run()
