# 🩺 Diabetes Prediction Model – Your First MLOps Project (FastAPI + Docker + K8s)

> 🎥 YouTube video for the project: **"Build Your First MLOps Project"**

This project helps you learn **Building and Deploying an ML Model** using a simple and real-world use case: predicting whether a person is diabetic based on health metrics. We’ll go from:

- ✅ Model Training
- ✅ Building the Model locally
- ✅ API Deployment with FastAPI
- ✅ Dockerization
- ✅ Kubernetes Deployment

---

## 📊 Problem Statement

Predict if a person is diabetic based on:
- Pregnancies
- Glucose
- Blood Pressure
- BMI
- Age

We use a Random Forest Classifier trained on the **Pima Indians Diabetes Dataset**.

---

## 🚀 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/iam-veeramalla/first-mlops-project.git
cd first-mlops-project
```

### 2. Create Virtual Environment

```
python3 -m venv .mlops
source .mlops/bin/activate    # For macOs
source .mlops/Scripts/activate   # For windows
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

## Train the Model

```
python train.py
```

## Run the API Locally

```
uvicorn main:app --reload
```

### Sample Input for /predict

```
{
  "Pregnancies": 2,
  "Glucose": 130,
  "BloodPressure": 70,
  "BMI": 28.5,
  "Age": 45
}
```

## Dockerize the API

### Build the Docker Image

```
docker build -t diabetes-prediction-model .
```

### Run the Container

```
docker run -p 8000:8000 diabetes-prediction-model
```

## Deploy to Kubernetes

```
kubectl apply -f diabetes-prediction-model-deployment.yaml
```

## port forwarding 
![image](https://github.com/user-attachments/assets/a0b63d1e-e2f4-4a71-b707-798a2938aab2)

## Output
![image](https://github.com/user-attachments/assets/e80359fb-1243-4ca7-84c8-9b92c80a18c0)

After changing the parameters 
![image](https://github.com/user-attachments/assets/5159037f-1ef6-4e67-a9ad-985c812b53e3)







