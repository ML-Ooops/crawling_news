import requests
from datetime import datetime, timedelta
import json
from pymongo import MongoClient
import schedule
import time

# Function to read categories from a file
def read_categories_from_file(file_path):
    with open(file_path, 'r') as file:
        categories = [line.strip() for line in file if line.strip()]
    return categories

# Read categories from 'categories.txt' file
categories = read_categories_from_file('categories.txt')

def fetch_and_store_news():
    # Set up MongoDB client (using localhost and default port)
    client = MongoClient('mongodb://localhost:27017/')
    
    # Select the database and collection
    db = client['news_database']
    collection = db['news_collection']

    # Clear existing data in the collection
    collection.delete_many({})
    print("Existing data cleared.")

    all_news_data = []

    for category in categories:
        for i in range(10):
            # Calculate the date range for each iteration
            end_date = datetime.today() - timedelta(days=i*5)
            start_date = end_date - timedelta(days=5)
            
            end_date_str = end_date.strftime('%Y-%m-%d')
            start_date_str = start_date.strftime('%Y-%m-%d')

            params = {
                "argument": {
                    "published_at": {
                        "from": start_date_str,
                        "until": end_date_str
                    },
                    "category": [category],
                    "sort": {
                        "date": "desc"
                    },
                    "return_from": "0",
                    "return_size": "10000",
                    "fields": [
                        "news_id",
                        "published_at",
                        "title",
                        "content",
                        "provider",
                        "byline",
                        "category",
                        "category_incident",
                        "provider_link_page",
                        "printing_page"
                    ]
                },
                "access_key": "newstoresample"
            }
            headers = {'Content-type': 'application/json'}
            response = requests.post("https://www.newstore.or.kr/api-newstore/v1/search/newsAllList.json", json=params, headers=headers)

            if response.status_code == 200:
                # Decode the response content
                response_data = response.json()
                if "returnObject" in response_data:
                    decoded_data = json.loads(response_data["returnObject"])
                    if isinstance(decoded_data, dict):
                        all_news_data.append(decoded_data)
                    elif isinstance(decoded_data, list):
                        all_news_data.extend(decoded_data)
                else:
                    print(json.dumps(response_data, indent=2, ensure_ascii=False))
            else:
                print(response.content)

    # Save all collected data to MongoDB
    if all_news_data:
        try:
            # Insert data
            collection.insert_many(all_news_data)
            print("Data successfully stored.")
        except Exception as e:
            print(f"Error occurred while storing data to MongoDB: {e}")

if __name__ == '__main__':
    # Initial execution
    fetch_and_store_news()
    print("first_search complete")
    #schedule.every(12).hours.do(fetch_and_store_news)

    schedule.every(1).minutes.do(fetch_and_store_news)

    while True:
        schedule.run_pending()
        time.sleep(1)