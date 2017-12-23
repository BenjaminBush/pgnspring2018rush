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

@pgn.route('/register', methods=['POST'])
def register():
	if request.method == 'POST':
		first_name = request.form['first_name']
	return render_template('success.html', name=first_name)

if __name__ == '__main__':
  pgn.run(debug=True)