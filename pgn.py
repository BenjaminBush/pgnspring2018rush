from flask import Flask, redirect, render_template, request, session, url_for, redirect, jsonify
import json
import requests, psycopg2, base64, datetime
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
 

pgn = Flask(__name__)

conn = psycopg2.connect("dbname='d298jccbr5sqa0' password='fd4e390377429e296d61a9dd027c1fb4907c68c4771a3ff91386ebbf4cc3a37e' user='wgbonvabycqzoi' host='ec2-23-23-245-89.compute-1.amazonaws.com' port='5432'")
conn.autocommit = True

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

		cur = conn.cursor()
		insert_pnm_query = """
			INSERT INTO pnms (
				first_name,
				last_name,
				email,
				student_id,
				phone,
				year,
				school,
				comments
			)
			VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
		
		cur.execute(insert_pnm_query, (
			first_name,
			last_name,
			email,
			student_id,
			phone,
			year,
			school,
			comment
		))

		cur.close()

	json_key = json.load(open('creds.json'))
	scope = ['https://spreadsheets.google.com/feeds']
	credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds

	file = gspread.authorize(credentials) # authenticate with Google
	sheet = file.open("dbtest").sheet1 # open sheet
	values = [first_name, last_name, email, student_id, phone, year, school, comment]
	sheet.resize(1)
	sheet.append_row(values);

	return render_template('success.html', values=values)

if __name__ == '__main__':
  pgn.run(debug=True)