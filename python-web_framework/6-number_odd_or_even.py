"""
Copy the previous task to a new script that starts a Flask web application:
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    even_or_odd = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', number=n, even_or_odd=even_or_odd)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
