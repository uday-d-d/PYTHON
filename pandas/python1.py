import pandas as pd


# 1) Create and Display DataFrame (Laptop Details)
laptops = {
    "Brand": ["Dell", "HP", "Lenovo", "Asus", "Apple"],
    "Model": ["Inspiron", "Pavilion", "ThinkPad", "VivoBook", "MacBook Air"],
    "Price": [45000, 50000, 55000, 48000, 90000]
}

df_laptops = pd.DataFrame(laptops)
print("=== Laptop Details DataFrame ===")
print(df_laptops)

# 2) Sort DataFrame by column values (Price)
df_sorted = df_laptops.sort_values(by="Price", ascending=False)
print("\n=== Laptops Sorted by Price (Descending) ===")
print(df_sorted)

# 3) Handle Missing Data in another DataFrame (Movie Records)
movies = {
    "Movie": ["Inception", "Avatar", "Titanic", "Interstellar"],
    "Year": [2010, 2009, None, 2014],
    "Rating": [8.8, None, 7.9, 8.6]
}

df_movies = pd.DataFrame(movies)
print("\n=== Movie Records DataFrame (With Missing Values) ===")
print(df_movies)

# Method 1: dropna()
df_dropna = df_movies.dropna()
print("\n=== Movie Records (After dropna) ===")
print(df_dropna)

# Method 2: fillna() 
df_filled = df_movies.fillna({
    "Year": df_movies["Year"].mean(),
    "Rating": df_movies["Rating"].mean()
})
print("\n=== Movie Records (After fillna)===")
print(df_filled)
