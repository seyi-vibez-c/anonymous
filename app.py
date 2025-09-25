#from flask import Flask, redirect, request,url_for,render_template
#import sqlite3

#app = Flask(__name__)

#def get_connection_db():
#    conn = sqlite3.connect("messages_db.db")
#    conn.row_factory = sqlite3.Row
#    return conn
#    

#@app.route("/", methods=["POST", "GET"])
#def home():
#    if request.method == "POST":
#        messages = request.form["message"]
#        conn = get_connection_db()
#        conn.execute("INSERT INTO messages (message) VALUES (?)", (messages))
#        conn.commit()
#        conn.close()
#        return redirect("/")
#    return render_template("index.html")
#    
#@app.route("/check")
#def check():
#    conn= get_connection_db()
#    messages = conn.execute("SELECT * FROM messages").fetchall()
#    
#    return render_template("message.html", messages=messages)


#if __name__ == "__main__":
#    app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create table if it doesn't exist
def create_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS messages
        (id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT)
    ''')
    conn.close()

create_table()

# Route to post data to database
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        conn = get_db_connection()
        conn.execute('INSERT INTO messages (message) VALUES (?)', (message,))
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template('index.html')

# Route to fetch all data from database
@app.route('/messages')
def messages():
    conn = get_db_connection()
    messages = conn.execute('SELECT * FROM messages').fetchall()
    conn.close()
    return render_template('message.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)