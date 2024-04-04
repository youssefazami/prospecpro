from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__,template_folder="listrace-v1.0/templates",static_folder='listrace-v1.0/assets')



# Configure MySQL------------------------------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'NGBS_Project'




mysql = MySQL(app)
#index-----------------------------------------------
@app.route('/')
def index():
    return render_template("index.html")


#login_page----------------------------------------
@app.route('/login_page', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        keyword = request.form['keyword']
        if keyword:
            return render_template('login_page.html')
    return render_template('login_page.html')

#sub_activity----------------------------------------    
@app.route('/sub_activity', methods=['GET', 'POST'])
def sub_activity():
    result='IT'
    if request.method == 'POST':
        keyword = request.form['keyword']
        if keyword:
            return render_template('sub_activity.html',result)
    return render_template('sub_activity.html')

#main_activity---------------------------------------- 
@app.route('/main_activity', methods=['GET', 'POST'])
def main_activity():
    if request.method == 'POST':
        keyword = request.form['keyword']
        if keyword:
            return render_template('main_activity.html')
    return render_template('main_activity.html')



#employe_number--------------------------------------
@app.route('/employe_number', methods=['GET', 'POST'])
def employe_number():
    if request.method == 'POST':
        keyword = request.form['keyword']
        if keyword:
            return render_template('employe_number.html')
    return render_template('employe_number.html')


#Company_list-------------------------------------------
@app.route('/Company_list', methods=['GET', 'POST'])
def Company_list():
    selected_size = request.args.get('size')
    if selected_size:
        query = "SELECT * FROM entreprises_it WHERE size_updated = %s"
        cursor = mysql.connection.cursor()
        cursor.execute(query, (selected_size,))
        result = cursor.fetchall()
        cursor.close()
        return render_template('Company_list.html', result=result)
    else:
        return "Size parameter not provided."

#job_offers--------------------------(not done yet)
@app.route("/job_offers/<company_name>")
def job_offers(company_name):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM offres WHERE company_name = %s", (company_name,))
    job_offers = cursor.fetchall()
    cursor.close()

    return render_template("job_offers.html", company_name=company_name, job_offers=job_offers)


if __name__ == '__main__':
    app.run(debug=True)
