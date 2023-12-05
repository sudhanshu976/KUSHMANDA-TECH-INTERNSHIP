from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image

class_names = [
    'Tomato_Bacterial_spot',
    'Tomato_Early_blight',
    'Tomato_Late_blight',
    'Tomato_Leaf_Mold',
    'Tomato_Septoria_leaf_spot',
    'Tomato_Spider_mites_Two_spotted_spider_mite',
    'Tomato__Target_Spot',
    'Tomato__Tomato_YellowLeaf__Curl_Virus',
    'Tomato__Tomato_mosaic_virus',
    'Tomato_healthy'
]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for prediction logs
class PredictionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    image_filename = db.Column(db.String(255))
    predicted_class = db.Column(db.String(50))

# Load the TensorFlow model
model = tf.keras.models.load_model('model.h5')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('home.html', result="No file selected")

    image = request.files['file']

    try:
        # Instead of saving the image, directly open it
        image = Image.open(image)
        image = image.resize((224, 224))
        img_array = img_to_array(image)
        img_array = np.expand_dims(img_array, axis=0)
        #img_array /= 255.0

        # Clear the TensorFlow session to ensure the model uses the updated graph
        tf.keras.backend.clear_session()

        # Make predictions
        predictions = model.predict(img_array)
        result = class_names[np.argmax(predictions[0])]

        # Log the prediction
        log_prediction(request.files['file'].filename, result)

        return render_template('home.html', result=result)
    except Exception as e:
        return render_template('home.html', result=str(e))

# Log prediction to the database
def log_prediction(image_filename, predicted_class):
    prediction_log = PredictionLog(image_filename=image_filename, predicted_class=predicted_class)
    db.session.add(prediction_log)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8080,debug=True)
    # Create database tables before running the app
