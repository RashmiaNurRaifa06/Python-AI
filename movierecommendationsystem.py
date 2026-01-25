import pandas as pd
from textblob import TextBlob
from colorama import init, Fore, Style

init(autoreset=True)

df = pd.read_csv("imdb_top_1000.csv")

genres = sorted({g.strip() for x in df["Genre"].dropna() for g in x.split(",")})

moods = {
    "1": ("Happy", 0.2),
    "2": ("Relaxed", 0.1),
    "3": ("Sad", -0.2),
    "4": ("Excited", 0.3),
    "5": ("Dark", -0.3)
}

def recommendation(genre, mood_threshold, limit=5):
    data = df[df["Genre"].str.split(",").apply(lambda x: genre.lower() in [g.strip().lower() for g in x] if isinstance(x, list) else False)]
    if data.empty:
        return []
    results = []
    for _, row in data.sample(frac=1).iterrows():
        if pd.isna(row["Overview"]):
            continue
        polarity = TextBlob(row["Overview"]).sentiment.polarity
        if (mood_threshold >= 0 and polarity >= mood_threshold) or (mood_threshold < 0 and polarity <= mood_threshold):
            results.append((row["Series_Title"], row["Released_Year"], polarity))
            if len(results) == limit:
                break
    return results

def main():
    print(Fore.BLUE + Style.BRIGHT + "\nMovie Recommendation System\n")
    name = input(Fore.CYAN + "Enter your name: " + Fore.WHITE).strip()
    print(Fore.YELLOW + "\nAvailable Genres: ")
    for i, g in enumerate(genres, 1):
        print(f"{Fore.WHITE}{i}. {Fore.GREEN}{g}")
    while True:
        g = input(Fore.MAGENTA + "\nSelect genre (number or name): " + Fore.WHITE).strip()
        if g.isdigit() and 1 <= int(g) <= len(genres):
            genre = genres[int(g) - 1]
            break
        if g.lower() in [x.lower() for x in genres]:
            genre = next(x for x in genres if x.lower() == g.lower())
            break
        print(Fore.RED + "Invalid genre selection. Please try again.")
    print(Fore.CYAN + f"\nSelected genre: {genre}")
    print(Fore.YELLOW + "\nSelect your mood: ")
    for k, v in moods.items():
        print(f"{Fore.WHITE}{k}. {Fore.GREEN}{v[0]}")
    while True:
        m = input(Fore.MAGENTA + "Enter mood number: " + Fore.WHITE).strip()
        if m in moods:
            mood_name, mood_value = moods[m]
            break
        print(Fore.RED + "Invalid mood selection. Please try again.")
    movies = recommendation(genre, mood_value)
    print(Fore.YELLOW + Style.BRIGHT + f"\nRecommendations for {name} ({mood_name} mood):\n")
    if not movies:
        print(Fore.RED + "No matching movies found based on your preferences.")
        return
    for i, (title, year, score) in enumerate(movies, 1):
        color = Fore.GREEN if score >= 0 else Fore.RED
        print(f"{Fore.WHITE}{i}. {color}{title}{Fore.CYAN} ({year}) {Fore.WHITE}- Sentiment: {score:.2f}")

if __name__ == "__main__":
    main()
