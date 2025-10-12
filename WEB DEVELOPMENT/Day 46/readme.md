# 🎵 Billboard to Spotify Playlist  

This project creates a private Spotify playlist containing the Billboard Hot 100 songs from any date you choose.  
It scrapes Billboard’s website for the top 100 songs of that day and adds them to a Spotify playlist in your account.

---

## ✨ Features
- Scrapes Billboard Hot 100 songs for a given date.  
- Searches and matches songs on Spotify.  
- Creates a **new private** Spotify playlist each run.  
- Adds all found songs to the playlist.  
- Prints the playlist link for easy access.

---

## 🚀 Setup

### 1. Clone this Repository
```bash
git clone https://github.com/Hiteshchr7/100-Days-of-Code.git
```

### 2. Navigate to Project Folder
```bash
cd "100-Days-of-Code/WEB DEVELOPMENT/Day 46"
```

### 3. Install Dependencies
Make sure you have **Python 3.8+** installed, then run:
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file inside the project folder with the following keys:
```env
sp_client_id=your_spotify_client_id
sp_client_secret=your_spotify_client_secret
redirect_uri=http://localhost:8888/callback
```

> ⚠️ Keep your `.env` file private. Do not commit it to GitHub.

### 5. Note about token cache
This project uses Spotipy and caches OAuth tokens to the path used in the script:
```
WEB DEVELOPMENT/Day 46/token.txt
```
Make sure this path exists or update `cache_path` in the script if you prefer a different location.

### 6. Run the Script
```bash
python spotify.py
```
Enter the date in `YYYY-MM-DD` format (e.g., `2000-08-19`).  
The script will scrape Billboard, create a new playlist, add tracks that exist on Spotify, and print the playlist link.

---

## ⚠️ Important Notes
- **Creates a new playlist every run** (no reuse/deduplication).  
- Some Billboard songs may not exist on Spotify and will be skipped (the script prints skipped titles).  
- The Spotify token file (`token.txt`) and your `.env` file should **never** be committed to GitHub.

### `.gitignore` suggestion
Add the following to `.gitignore`:
```
.env
token.txt
WEB DEVELOPMENT/Day 46/token.txt
__pycache__/
*.pyc
```

---

## 📌 Example
```
What year would you like to travel to? Type the data in this format YYYY-MM-DD: 2000-08-19
Created playlist: 2000-08-19 Top_100_Billboards
Tracks added: 95 | Skipped: 5
🔗 https://open.spotify.com/playlist/2I7jy73bglgTSdBAutLkDm
```

---

## 🛠 Requirements
- Python 3.8+  
- spotipy  
- requests  
- beautifulsoup4  
- python-dotenv

Install them via:
```bash
pip install spotipy requests beautifulsoup4 python-dotenv
```

---

## 📄 License
This project is part of [Hiteshchr7/100-Days-of-Code](https://github.com/Hiteshchr7/100-Days-of-Code).  
Feel free to use and modify it for learning purposes.
