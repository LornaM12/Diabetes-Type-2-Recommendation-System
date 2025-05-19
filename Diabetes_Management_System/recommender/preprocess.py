
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def load_food_data(path="data/FoodData.csv"):
    df = pd.read_csv(path)

    # Select numeric columns for normalization
    cols_to_normalize = [
        'Glycemic Index', 'Calories', 'Carbohydrates', 'Protein', 'Fat',
        'Sodium Content', 'Potassium Content', 'Magnesium Content',
        'Calcium Content', 'Fiber Content'
    ]

    # Normalize  columns
    scaler = MinMaxScaler()
    df[cols_to_normalize] = scaler.fit_transform(df[cols_to_normalize])

    return df


def load_patient_data(path="data/PatientData.csv"):
    df = pd.read_csv(path)

    # Basic cleaning — remove missing values if any
    df.dropna(inplace=True)

    return df
