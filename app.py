from flask import Flask, request
import os, json
import sqlite3
from sqlite3 import Error

app = Flask(__name__)



## Accepts 'body' and 'title' elements in json, and insterts
## them into the db
@app.route('/post', methods=['POST'])
def create_post():
    post_data = request.get_json()
    # Need to have this write to the db instead of printing
    print(post_data)
    return 'json posted'

## Gets all posts from the db, no parameters
@app.route('/posts', methods=['GET'])
def get_posts():
    ## Set up a sqlite connection
    con = sqlite3.connect(r'blog.db')
    ## Create a cursor to execute the query
    cur = con.cursor()
    cur.execute("SELECT * FROM posts;")
    all_posts = (cur.fetchall())
    ## return the result as json
    return json.dumps(all_posts)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)