import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import RobustScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.processing import clean_recipe_data
import os

# Créer le dossier models s'il n'existe pas
os.makedirs('models', exist_ok=True)

# 1. Charger et nettoyer
df = clean_recipe_data('data/recipe_site_traffic_2212.csv')

# 2. Séparer features (X) et target (y)
X = df.drop(columns=['high_traffic', 'recipe'])
y = df['high_traffic'].map({'High': 1, 'Low': 0})

# 3. Créer le pipeline de transformation
numeric_features = ['calories', 'carbohydrate', 'sugar', 'protein', 'servings']
categorical_features = ['category']

preprocessor = ColumnTransformer([
    ('num', RobustScaler(), numeric_features),
    ('cat', OneHotEncoder(drop='first'), categorical_features)
])

# 4. Pipeline complet : Prétraitement + Modèle
model = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

# 5. Entraînement
model.fit(X, y)

# 6. Sauvegarde
joblib.dump(model, 'models/best_model.joblib')
print("Modèle sauvegardé dans models/best_model.joblib !")