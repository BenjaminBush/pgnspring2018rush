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
		last_name = request.form['last_name']
		email = request.form['email']
		student_id = request.form['student_id']
		phone = request.form['phone']
		year = request.form['year']
		school = request.form['school']
		comment = request.form['comment']
	return render_template('success.html', first_name=first_name,
		last_name=last_name, email=email, student_id=student_id,
		phone=phone, year=year, school=school, comment=comment)

if __name__ == '__main__':
  pgn.run(debug=True)