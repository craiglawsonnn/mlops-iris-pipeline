# MLOps Iris Pipeline
## Overview

This project is to demonstrate a complete MLOps pipeline for an Iris flower classification machine learning model using GitHub Actions, Docker, Flask, and Google Cloud Platform (GCP).

The application trains a Random Forest classifier using the Iris dataset from Scikit-learn and exposes prediction functionality through a Flask REST API.

The project implements multiple MLOps stages including:
- Data preprocessing
- Model training and testing
- Continuous Integration (CI)
- Continuous Delivery (CD)
- Continuous Training (CT)
- Docker containerization
- Cloud deployment on Google Cloud VM

## Technologies Used
- Python
- Flask
- Scikit-learn
- Docker
- GitHub Actions
- Google Cloud Platform (GCP)
- Pytest

## Pipeline Stages
### Data Preprocessing
Dataset loading and train/test split performed using Scikit-learn

### Model Training & Testing
A Random Forest classifier is trained and validated automatically

### Continuous Integration (CI)
GitHub Actions automatically installs dependencies, trains the model, and runs automated tests on every push

### Continuous Delivery (CD)
Docker images are automatically built and pushed to Docker Hub using GitHub Actions

### Continuous Training (CT)
The model retraining workflow can run manually or on a scheduled basis using GitHub Actions

## Architecture
Developer -> GitHub Repository -> GitHub Actions -> Docker Hub -> Google Cloud VM -> Flask API

## Running Locally
Clone my repository:
```bash
git clone https://github.com/craiglawsonnn/mlops-iris-pipeline.git
cd mlops-iris-pipeline
```

To create the virtual environment:
```bash
python -m venv venv
```

Activate environment:
```bash
venv\Scripts\activate
or
source venv/bin/activate
```

Installing dependencies and libraries:
```bash
pip install -r requirements.txt
```

To train the model:
```bash
python src/train.py
```

Running Flask API:
```bash
python app.py
```

The application is available at:
http://127.0.0.1:5000


## Running with Docker
Build Docker image:

```bash
docker build -t mlops-iris-api .
```

Run container:
```bash
docker run -p 5000:5000 mlops-iris-api
```

## API Usage
### Health Check
curl http://127.0.0.1:5000

Example response:
{
  "endpoint": "/predict",
  "message": "Iris Classification API is running"
}

### Prediction Endpoint
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}'

Example response:
{
  "prediction": "setosa"
}

## GitHub Actions Workflows

### CI - Test ML Pipeline
- Installs project dependencies
- Trains the machine learning model
- Executes automated API tests using Pytest

### Continuous Training
- Retrains the model automatically
- Supports scheduled and manual retraining workflows

### CD - Build and Push Docker Image
- Builds Docker container image automatically
- Pushes image to Docker Hub using GitHub Secrets

## Deployment
The Flask API is deployed as a Docker container on a Google Cloud Platform Virtual Machine (VM)

Deployment flow:
GitHub -> GitHub Actions -> Docker Hub -> Google Cloud VM -> Flask API

## Branching Strategy
The following branching strategy was implemented:
- main -> production ready code
Changes are validated through GitHub Actions before being merged into the main branch

## References
- https://flask.palletsprojects.com/
- https://docs.docker.com/
- https://docs.github.com/actions
- https://scikit-learn.org/
- https://cloud.google.com/

## Troubleshooting

- Chatgpt (chatgpt.com)
- Claude 