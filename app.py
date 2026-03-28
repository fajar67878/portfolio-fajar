from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def simple_portfolio():
    return render_template('portfolio.html')

if __name__ == '__main__':
    # Ini penting agar Render bisa menentukan port sendiri
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)