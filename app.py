from flask import Flask, request
import os, json

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
    # placeholder json while I configure the db
    message = {
        'uid': '11289364',
        'title': 'title',
        'body': 'content'
    }
    return json.dumps(message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)