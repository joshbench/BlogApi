from flask import Flask, request
import os, json
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

## Accepts 'body' and 'title' elements in json, and insterts
## them into the db
@app.route('/post', methods=['POST'])
def create_post():
    ## scrape title and body from request
    post_data = request.get_json()
    title = post_data['title']
    body = post_data['body']
    ## Set up a sqlite connection
    con = sqlite3.connect(r'blog.db')
    ## Create a cursor to execute the query
    cur = con.cursor()
    ## the post_id auto-iterates, so insert title and body
    cur.execute("INSERT INTO posts (title, body) VALUES (?,?);", (title, body))
    ## commit and close db connection
    con.commit()
    con.close()
    result = { 
        'result': 'success'
    }
    return json.dumps(result)

## Gets all posts from the db, no parameters
@app.route('/posts', methods=['GET'])
def get_posts():
    ## Set up a sqlite connection
    con = sqlite3.connect(r'blog.db')
    ## Create a cursor to execute the query
    cur = con.cursor()
    cur.execute("SELECT * FROM posts;")
    all_posts = (cur.fetchall())
    con.close()
    ## return the result as json
    return json.dumps(all_posts)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)