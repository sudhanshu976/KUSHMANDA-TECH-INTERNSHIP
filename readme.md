# Project Documentation

## Overview

This documentation provides a comprehensive guide on the development and deployment process of a plant disease prediction system using ChatGPT, TensorFlow, Flask, SQLite3, Docker, and Kubernetes. The project involves data collection, model training using transfer learning (MobileNetV2), creating a Flask web application, storing predictions in a SQLite database, and deploying the application using Docker and Kubernetes.

## Project Structure

- **1_Roadmap_and_ChatGPT:**
  - Contains details of the initial project roadmap and how ChatGPT was utilized for clear vision.

- **2_Jupyter_Notebook:**
  - `notebook.ipynb` contains the code for data collection, preparation, model selection, training, evaluation, and testing.

- **3_PlantVillage_Dataset:**
  - Dataset used for training the model. [PlantVillage Dataset](https://www.kaggle.com/datasets/arjuntejaswi/plant-village)

- **4_Flask_App:**
  - `app.py`: Flask application code.
  - `templates/home.html`: HTML template for the web interface.
  - `static/upload.js`: JavaScript file for handling image uploads.
  - CSS styling is included within the HTML file.

- **5_SQLite_Database:**
  - `instance/predictions.db`: SQLite database to store prediction information.

- **6_Dockerization:**
  - `Dockerfile`: Configuration for Docker image.
  - Commands for building and running the Docker image.

- **7_Kubernetes_Deployment:**
  - Guidelines and commands for deploying the Flask app using Kubernetes and Minikube.

## Model Training

- **Data Preparation:**
  - TensorFlow was used for data extraction, splitting, visualization, prefetching, etc.
  
- **Model Selection:**
  - MobileNetV2 was chosen for its efficiency, small size (15 MB), and suitability for mobile and edge devices.

- **Fine-tuning:**
  - Additional layers (resize_rescale and data_augmentation) were added to prevent overfitting.
  - The model was fine-tuned on the custom dataset for approximately 15 epochs, resulting in satisfactory training, validation, and test accuracy.

## Flask Application

- A Flask web application was developed to interact with the trained model.
- The interface, implemented with HTML, CSS, and JS, accepts user-uploaded images for prediction.

## Database Integration

- SQLite3 and Flask-SQLAlchemy were used to create a database (`predictions.db`).
- The database stores prediction timestamps, input images, and prediction results.

## Dockerization

- The Flask application was Dockerized for portability and ease of deployment.
- A `Dockerfile` was created to build a Docker image (`my-flask-app`).

## Kubernetes Deployment

- Kubernetes deployment involved pushing the Docker image to DockerHub.
- Minikube was used to deploy five replicas of the Flask app as pods.

## Usage

1. Clone the repository.
2. Follow the steps outlined in each section of the documentation.
3. For Flask app testing, run the Docker image locally.
4. For production deployment, use the provided Kubernetes deployment guidelines.

## Contributors

- [Your Name]
- [Other contributors, if any]

## License

This project is licensed under the [MIT License](LICENSE).
