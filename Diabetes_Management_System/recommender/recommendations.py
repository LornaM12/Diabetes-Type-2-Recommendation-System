import pandas as pd
import joblib


def recommend_food_for_patient(patient):
    # Load models and food data
    scaler = joblib.load("models/scaler.pkl")
    kmeans = joblib.load("models/kmeans_model.pkl")
    food_df = pd.read_csv("../data/FoodData.csv")

    # Clean and scale Data
    features = ['Calories', 'Carbohydrates', 'Protein', 'Fat', 'Fiber Content', 'Glycemic Index']
    food_df = food_df.dropna(subset=features)
    food_scaled = scaler.transform(food_df[features])
    food_df['Cluster'] = kmeans.predict(food_scaled)

    # Carb selection
    carb = food_df[
        (food_df['Carbohydrates'] > 10) &
        (food_df['Glycemic Index'] <= 60)
        ].sort_values('Carbohydrates', ascending=False).head(1)

    # Protein selection
    protein = food_df[
        (food_df['Protein'] >= 5)
    ].sort_values('Protein', ascending=False).head(1)

    #  Vegetable Selection
    vegetable = food_df[
        (food_df['Fiber Content'] >= 1.5) &
        (food_df['Calories'] <= 100)
        ].sort_values('Fiber Content', ascending=False).head(1)


    plate = pd.concat([carb, protein, vegetable])


    if plate.empty:
        return pd.DataFrame({"Message": ["No foods found in current filters."]})

    return plate[['Food Name', 'Calories', 'Carbohydrates', 'Protein', 'Fat', 'Fiber Content', 'Glycemic Index']]


if __name__ == "__main__":
    patient = {
        "HbA1c": 10.2,
        "FBS": 100,
        "RBS": 200
    }

    print("Recommended Meal:")
    print(recommend_food_for_patient(patient))
