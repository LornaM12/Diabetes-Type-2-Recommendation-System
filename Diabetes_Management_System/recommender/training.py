import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import joblib
import os


def train_food_clustering_model():
    # Load food data
    df = pd.read_csv("../data/FoodData.csv")

    # Nutritional features for clustering
    features = ["Calories", "Carbohydrates", "Protein", "Fat", "Fiber Content", "Glycemic Index"]

    X = df[features]

    # Drop missing values
    X = X.dropna()

    # Scale the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train KMeans
    kmeans = KMeans(n_clusters=5, random_state=42, n_init='auto')
    kmeans.fit(X_scaled)

    # Create a models folder and save
    os.makedirs("models", exist_ok=True)
    joblib.dump(scaler, "models/scaler.pkl")
    joblib.dump(kmeans, "models/kmeans_model.pkl")

    print("Model and scaler saved!")


if __name__ == "__main__":
    train_food_clustering_model()
