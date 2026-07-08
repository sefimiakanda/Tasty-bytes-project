from src.processing import clean_recipe_data

df = clean_recipe_data('data/recipe_site_traffic_2212.csv')
print(df.head())
print("Nettoyage réussi !")