import os
import datetime 
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.microblog
    
    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert({"content": entry_content, "date": formatted_date})

        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
            )
            for entry in app.db.entries.find({})
        ]

        return render_template("home.html", entries=entries_with_date)

    return app

    @app.route("/about")
    def aboutpage():
        title = "About this site"
        paragraph = ["I am transitioning to development after a long career working in the medical records field. When faced with the option of finding another job after a team-wide layoff at my company, or attending training for a new career; I jumped at the chance to go to school to learn programming. I am excited for the opportunity to utilize the skills I have learned over the past almost three years, and to continue to learn and grow in this field."]

        pageType = 'about'

        return render_template("about.html", title=title, paragraph=paragraph, pageType=pageType)
    app.run()
    
    @app.route("/howMade")
    def howMade():

            title = "How this app was made"
            paragraph = ["This app is a result of working through the Web Developer Bootcamp with Flask and Python certificate class by Teclado by Jose Salvatierra. This app utilizes HTML5, CSS3, Python, Flask, Jinja2, MongoDB, GitHub and is deployed on Heroku. I learned a lot building this Microblog.  I customized it a bit for my preferences and added a link to a .NET sample doctor's office website that I created as a portfolio.  I hope you like my work!  Thanks for visiting!  Denise"]

            pageType = 'howMade'

            return render_template("howMade.html", title=title, paragraph=paragraph, pageType=pageType)
    app.run()
