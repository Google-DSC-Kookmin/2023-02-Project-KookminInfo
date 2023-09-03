import pymongo
from crawl import scrape_kookmin_news

# Initialize MongoDB client and database connection
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Update with your MongoDB connection details
db = client["kookmin_news"]  # Replace "kookmin_news" with your database name
collection = db["posts"]

def save_to_mongodb(url):
    # Get data from crawling
    post_data_list = scrape_kookmin_news(url)

    # Insert each post data item into MongoDB one by one
    for post_data in post_data_list:
        collection.insert_one(post_data)

    # Close the MongoDB client
    client.close()

def check_saved_data():
    # Query all documents in the collection and print them
    saved_data = collection.find()

    for document in saved_data:
        print(document)

    # Close the MongoDB client
    client.close()


if __name__ == "__main__":
    url = 'https://www.kookmin.ac.kr/user/kmuNews/notice/7/index.do'
    save_to_mongodb(url)
    check_saved_data()
    print("saving complete")
