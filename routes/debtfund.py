from src import app
from flask import render_template

@app.route('/debtfund', methods=['GET', 'POST'])
def debtfund_index():
    return render_template("debtfund/index.html")
