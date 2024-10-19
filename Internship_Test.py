from flask import Flask
import subprocess
import os
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Your Full Name"  # Replace with your actual name
    username = os.getlogin()
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    top_output = subprocess.getoutput('top -b -n 1')
  
    html_response = f"""
    <html>
    <body>
        <h2>Name: {full_name}</h2>
        <h2>Username: {username}</h2>
        <h2>Server Time (IST): {server_time}</h2>
        <h3>TOP Output:</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    
    return html_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
