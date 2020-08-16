#!/usr/bin/env python
# coding: utf-8

# In[4]:


from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import requests
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/scrape_mars_15"
mongo = PyMongo(app)

@app.route("/")
def home():
    mars_data = mongo.db.collection.find_one()
    return render_template("index.html", mars_data = mars_data)

@app.route("/scrape")
def scrape():
    scraped_data = scrape_mars.scrape_all()
    mongo.db.collection.update({}, scraped_data, upsert=True)
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




