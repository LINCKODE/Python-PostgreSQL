#!/usr/bin/env python3
# 
# A buggy web service in need of a database.
import bleach
from flask import Flask, request, redirect, url_for

from forumdb import get_posts, add_post, remove_post

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>DB Forum</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 display: flex;
                 justify-content: space-between;
                 align-items: center;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
      .remove-button {
        color: white;
        background-color:red;
        border: 3px black solid;
        border-radius: 7px;
        transition-duration: 200ms;
        font-size: 1.25em;
      }
      .remove-button:hover {
        color: black;
        background-color: white;
        border-color: red;
      }
      .remove-button:active {
        color: red;
        background-color: black;
        border-color: red;
        transition-duration: 50ms;
      }
    </style>
  </head>
  <body>
    <h1>DB Forum</h1>
    <form method=post>
      <div><textarea id="content" name="content"></textarea></div>
      <div><button id="go" type="submit">Post message</button></div>
    </form>
    <!-- post content will go here -->
    <div class=post>
      <h2><b>Erase everything</b></h2>
      <form action="/del" method=post>
          <input type="hidden" id="idd" name="idd" value="ALL">
          <button class="remove-button" type="submit" value="Submit">REMOVE</button>
        </form>
    </div>
%s
  </body>
</html>
'''

# HTML template for an individual comment
POST = '''\
    <div class=post>
        <em class=date>%s</em>
        <br>
        %s
        <form action="/del" method=post>
          <input type="hidden" id="idd" name="idd" value="%s">
          <button class="remove-button" type="submit" value="Submit">REMOVE</button>
        </form>
    </div>
'''


@app.route('/', methods=['GET'])
def main():
    '''Main page of the forum.'''
    posts = "".join(POST % (date, text, int) for text, date, int in get_posts())
    html = HTML_WRAP % posts
    return html


@app.route('/', methods=['POST'])
def post():
    '''New post submission.'''
    message = request.form['content']
    add_post(bleach.clean(message))
    #add_post(message)
    return redirect(url_for('main'))


@app.route('/del', methods=['POST'])
def delete():
    remove_post(request.form['idd'])
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
