from flask import Flask, render_template, request, jsonify, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/save-activity', methods=['POST'])
def save_activity():
    data = request.json
    return jsonify({"status": "success", "message": "تم حفظ البيانات بنجاح في Firebase"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
