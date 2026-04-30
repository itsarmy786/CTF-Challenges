#!/usr/bin/env python3
from flask import Flask,request,make_response
app=Flask(__name__)
FLAG="KH3L0{xss_r3fl3ct3d_c00k13_st34l}"
@app.route("/")
def index():return "<h1>Search</h1><form action=/search><input name=q><button>Search</button></form>"
@app.route("/search")
def search():
    q=request.args.get("q","")
    return f"<h1>Results for: {q}</h1><p>No results found.</p><!-- Flag for admin cookie: {FLAG} -->"
@app.route("/admin")
def admin():
    if request.cookies.get("role")=="admin":return f"Flag: {FLAG}"
    return "Access denied",403
if __name__=="__main__":app.run(port=5002)
