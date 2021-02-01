from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from getNews import top_headlines

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=["POST", "GET"])
def index():

    if request.method == "POST":
        region = request.form["region"]
        if region == 'USA':
            region = 'us'
        elif region == 'Australia':
            region = 'au'
        elif region == 'Canada':
            region = 'ca'
        elif region == 'United Kingdom':
            region = 'gb'
        elif region == 'New Zealand':
            region = 'nz'
        
        topic = request.form["topic"].lower()
        
        result = top_headlines(region, topic)
        print(result)
        return render_template("index.html", dict = result)
    else:
        return render_template("index.html")
        
        

if __name__=='__main__':
    app.run(debug=True)