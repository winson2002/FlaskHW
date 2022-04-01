from app import myapp_obj
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SubmitForm(FlaskForm):
	city_name = StringField('city_name')
	submit = SubmitField('Submit')


name = 'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@myapp_obj.route("/", methods = ['GET', 'POST'])
def home():
	form = SubmitForm()
	if request.method == "POST":
        	flash(format(form.city_name.data))
		return redirect("/")
	return render_template('home.html', name=name, city_names=city_names, form=form)
