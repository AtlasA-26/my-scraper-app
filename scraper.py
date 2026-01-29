import pandas as pd
import feedparser # You'll need to add 'feedparser' to requirements.txt
from datetime import datetime

# 1. Target RSS Feeds (Example: Global Biotech News)
FEEDS = {
    'Nature Biotech': 'https://www.nature.com/nbt.rss',
    'ScienceDaily': 'https://www.sciencedaily.com/rss/matter_energy/biotechnology.xml'
}

def run_scraper():
    new_entries = []
    for source, url in FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]: # Get top 5 from each
            new_entries.append({
                'Date': datetime.now().strftime('%Y-%m-%d'),
                'Source': source,
                'Breakthrough': entry.title,
                'URL': entry.link
            })
    
    # 2. Update your CSV database
    df_new = pd.DataFrame(new_entries)
    try:
        df_existing = pd.read_csv('data/research_data.csv')
        df_final = pd.concat([df_existing, df_new]).drop_duplicates(subset=['Breakthrough'])
    except FileNotFoundError:
        df_final = df_new
        
    df_final.to_csv('data/research_data.csv', index=False)
    print("Scraper finished: CSV updated.")

if __name__ == "__main__":
    run_scraper()


