import pandas as pd
from sklearn.preprocessing import RobustScaler

def clean_recipe_data(file_path):
    # 1. Charger les données
    df = pd.read_csv(file_path)
    
    # 2. Imputation des valeurs manquantes (Nutrition)
    # On groupe par catégorie pour plus de précision
    cols_to_fill = ['calories', 'carbohydrate', 'sugar', 'protein']
    for col in cols_to_fill:
        df[col] = df.groupby('category')[col].transform(lambda x: x.fillna(x.median()))
    
    # 3. Correction des catégories (ex: Chicken Breast -> Chicken)
    df['category'] = df['category'].replace('Chicken Breast', 'Chicken')
    
    # 4. Nettoyage des servings (suppression du texte)
    df['servings'] = df['servings'].astype(str).str.extract(r'(\d+)').astype(int)
    
    # 5. Imputation du target 'high_traffic'
    df['high_traffic'] = df['high_traffic'].fillna('Low')
    
    return df