from flask import Flask, redirect, render_template, request, session, url_for, redirect, jsonify
import json

pgn = Flask(__name__)

# Just do all of the routing in here
@pgn.route('/')
def main():
  return redirect('/index')

@pgn.route('/index')
def index():
    return render_template('index.html')

@pgn.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

if __name__ == '__main__':
  pgn.run(debug=True)