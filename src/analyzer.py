import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import os

# Set Seaborn theme
sns.set_theme(style="whitegrid", palette="muted")

# Path to dataset CSV file
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'spotify_dataset.csv')

# Load CSV file from 'data' folder
def load_data(path):
    if not os.path.exists(path):
        print(f"Error: File not found at {path}")
        return pd.DataFrame()
    df = pd.read_csv(path)
    df = df.dropna(subset=['track_name', 'artists', 'track_genre', 'popularity'])
    return df

# Creating and saving 'Top genres' bar chart
def top_genres(df, n=10):
    os.makedirs("../images", exist_ok=True)
    top = df.groupby('track_genre')['popularity'].sum().sort_values(ascending=False).head(n)
    print("\nTop genres by popularity:")
    print(top)
    sns.barplot(x=top.values, y=top.index)
    for index, value in enumerate(top.values):
        plt.text(value, index, f"{value:,}", va='center')
    plt.title(f"Top {n} genres by total popularity")
    plt.xlabel("Total Popularity")
    plt.savefig("../images/top_genres.png")
    plt.show()
    
# Create and save popularity distribution histogram   
def popularity_distribution(df):
    plt.figure(figsize = (8, 5))
    sns.histplot(df['popularity'], bins = 20, kde = True, color="skyblue", edgecolor="black")
    plt.title("Popularity Distribution")
    plt.xlabel("Popularity")
    plt.ylabel("Count")
    plt.savefig("../images/popularity_distribution.png")
    plt.show()

# Entry point
def main():
    df = load_data(DATA_PATH)
    if df.empty:
        return
    print(f"Loaded {len(df)} tracks")
    top_genres(df)
    popularity_distribution(df)

if __name__ == "__main__":
    main()
