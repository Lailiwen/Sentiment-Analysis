#!/usr/bin/env python
# coding: utf-8

# In[1]:


from textblob import TextBlob


# In[2]:


from flask import Flask


# In[3]:


from flask import render_template, request


# In python, 2 underscores is a system word. Don't create variables starting with 2 underscores.

# In[4]:


app = Flask(__name__)


# A decorator (indicated by @) takes in a function, adds some functionality and returns it.

# In[5]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", result=r))
    else:
        return(render_template("index.html", result="waiting...."))


# In[ ]:


# to ensure this is your programme before cloud allows you to run
if __name__ == "__main__": 
    app.run()


# 127.0.0.1 is a reserved IP address to route back to yourself (Local Host). 5000 is the default port number for Flask.

# In[ ]:




