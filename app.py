from flask import Flask, request
import os, json

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def create_post():
    post_data = request.get_json()
    print (post_data)
    return 'json posted'

@app.route('/posts', methods=['GET'])
def get_posts():
    message = {
        'uid': '11289364',
        'title': 'title',
        'body': 'content'
    }
    return json.dumps(message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)