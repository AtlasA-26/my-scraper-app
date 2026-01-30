import feedparser
import pandas as pd
import os
from datetime import datetime

# Sources to scrape
SOURCES = {
    "PubMed": "https://pubmed.ncbi.nlm.nih.gov/rss/search/1M_D0Zf...",
    "AJOL Africa": "https://www.ajol.info/index.php/index/rss",
    "ArXiv Biotech": "http://export.arxiv.org/rss/q-bio"
}

def run_scrape():
    results = []
    for name, url in SOURCES.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:10]:
            # Simple logic to tag Africa-centric content
            region = "Africa" if "africa" in entry.title.lower() or "ajol" in name.lower() else "Global"
            results.append({
                "Date": datetime.now().strftime("%Y-%m-%d"),
                "Source": name,
                "Region": region,
                "Headline": entry.title,
                "Link": entry.link
            })
    
    df = pd.DataFrame(results)
    
    # Ensure directory exists
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/research_data.csv", index=False)

if __name__ == "__main__":
    run_scrape()




