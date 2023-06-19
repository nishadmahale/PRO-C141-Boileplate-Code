from flask import Flask, jsonify, request
import pandas as pd

articles_data = pd.read_csv('articles.csv')
all_articles = articles_data[['url' , 'title' , 'text' , 'lang' , 'total_events']]
liked_articles = []
not_liked_articles = []
articles=[]
user_liked_articles=[]
user_disliked_articles=[]
app = Flask(__name__)

def assign_val():
    m_data = {
        "url": all_articles.iloc[0,0],
        "title": all_articles.iloc[0,1],
        "text": all_articles.iloc[0,2] or "N/A",
        "lang": all_articles.iloc[0,3],
        "total_events": all_articles.iloc[0,4]
    }
    return m_data

# API to display first article
@app.route("/get-article")
def get_article():
    articles.get(articles_data)

    return 'Write code to display the first item in all_articles list'
articles.show_csv(articles_data)
   


# API to move the article into liked articles list
@app.route("/liked-article")
def liked_article():
    user_liked_articles.get(liked_article)
    

    return 'Write code to shift first article into liked_articles list'
articles.merge(user_liked_articles)


# # API to move the article into not liked articles list
@app.route("/unliked-article")
def unliked_article():
    user_disliked_articles.get[not_liked_articles]


    return 'Write code to shift first article into not_liked_articles list'
articles.merge(user_disliked_articles)
# run the application
if __name__ == "__main__":
    app.run()