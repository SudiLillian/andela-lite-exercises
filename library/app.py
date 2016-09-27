
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
db = SQLAlchemy(app)

@app.route("/")
def main():
  #define basic route
  return render_template('index.html')

@app.route("/about")
def about():
  #define basic route
  return render_template('about.html')

if __name__=="__main__":
  app.run(debug=True)
