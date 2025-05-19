import pandas as pd

df = pd.read_csv("FoodData.csv")

# Show basic info
print(df.info())

# Show how many foods are marked suitable for diabetes
print("Suitable for Diabetes == 1:", df[df['Suitable for Diabetes'] == 1].shape[0])

# Show some foods with fiber, protein, and carbs
print(df[['Food Name', 'Calories', 'Carbohydrates', 'Protein', 'Fat', 'Fiber Content', 'Glycemic Index', 'Suitable for Diabetes']].sort_values(by='Carbohydrates', ascending=False).head(10))
