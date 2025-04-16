This is a machine learning (ML)-based diet recommendation model tailored for individuals living with Type 2 Diabetes (T2D). 
The model is capable of generating personalized, balanced meal plans that support glycemic control.

The ML model takes as input a set of user-specific health parameters, including HbA1c levels, fasting blood sugar (FBS), Random Blood Sugars (TBS) and body mass index (BMI). 
Based on these features, the model predicts and recommend suitable daily meal plans composed of nutrient-rich foods that help regulate blood glucose levels.
The model combines content-based filtering to match users with meals that align with their nutritional requirements and blood sugar management goals, and cosine similarity to measure 
the closeness between a user's profile and the nutritional profiles of available meal options. 

Additionally,a clustering algorithm (K-Means) is used to group similar food items, enabling more structured and diverse meal planning. 
 Random Forest Classifier is also used to categorize patients based on their level of glycemic control, allowing the recommendation engine to provide more targeted and relevant dietary suggestions.

