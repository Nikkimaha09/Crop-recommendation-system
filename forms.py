from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

class CropRecommendationForm(FlaskForm):
    nitrogen = FloatField('Nitrogen (kg/ha)', validators=[DataRequired()])
    phosphorus = FloatField('Phosphorus (kg/ha)', validators=[DataRequired()])
    potassium = FloatField('Potassium (kg/ha)', validators=[DataRequired()])
    temperature = FloatField('Temperature (°C)', validators=[DataRequired()])
    humidity = FloatField('Humidity (%)', validators=[DataRequired()])
    rainfall = FloatField('Rainfall (mm)', validators=[DataRequired()])
    submit = SubmitField('Get Recommendation')