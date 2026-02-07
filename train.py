# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset from a working source (Kaggle/hosted)
url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
df = pd.read_csv(url)

print("✅ Columns:", df.columns.tolist())  # Debug print

# Prepare data
X = df[["Pregnancies", "Glucose", "BloodPressure", "BMI", "Age"]]
y = df["Outcome"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save
joblib.dump(model, "diabetes_model.pkl")
print("✅ Model saved as diabetes_model.pkl")
#python -m venv .mlops
#.mlops\Scripts\activate
#uvicorn main:app --reload
#pip install -r requirements.txt
#python train.py
#docker build -t diabetes-prediction-model .
#code Dockerfile
#ls
# docker run -p 8000:8000 diabetes-prediction-model
# docker images
#kubectl version --client
#kubectl cluster-info
#code k8s-deploy.yml
# kubectl apply -f k8s-deploy.yml
# kubectl get deployments
# kubectl get pods
#  kubectl get services
#docker tag diabetes-prediction-model:latest  aryammanshah/diabetes-model-demo:v1
# docker push aryammanshah/diabetes-model-demo:v1
# kubectl port-forward svc/diabetes-api-service 8000:80
