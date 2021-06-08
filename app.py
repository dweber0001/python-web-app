import os
import datetime 



from flask import Flask, render_template, request



from pymongo import MongoClient



from dotenv import load_dotenv




load_dotenv()



def jls_extract_def():
    

    return 



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



        jls_extract_var = [
                    (


                        entry["content"],


                        entry["date"],


                        datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
                    )


                    for entry in app.db.entries.find({})


                ]


        entries_with_date = jls_extract_var = jls_extract_def()



    jls_extract_var = entries
    return render_template("home.html", jls_extract_vars=entries_with_date)
       



    return app




    @app.route("/about")



    def about():
        



        return render_template("about.html")




    @app.route("/howMade")



    def howMade():
        



        return render_template("howMade.html")



