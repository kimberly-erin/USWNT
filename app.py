import numpy as np
import pandas as pd
import pickle
import os
import json
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Routes
#################################################

@app.route('/get_prediction', methods=["POST", "GET"])
def get_table():

   for i in request.json:
       print(i["name"])
       if i["name"] == "Shots":
           Shots=i["value"]
       elif i["name"] == "assists":
           Assists=i["value"]
       elif i["name"] == "fwPass.Comp.Pct":
           fwPass=i["value"]
       elif i["name"] == "Cross.Comp.Pct":
           crossInput=i["value"]
       elif i["name"] == "Big.Chances":
           BigChancesInput=i["value"]
       elif i["name"] == "AD.Win.Pct":
           AdWinInput=i["value"]

   model_file=os.path.join("static","woso_finalized_model.sav")
   loaded_model = pickle.load(open(model_file, 'rb'))

   test_dict={"Shots":Shots,"Assists":Assists,"fwPass.Comp.Pct":fwPass,"Cross.Comp.Pct":crossInput,"Big.Chances":BigChancesInput,"AD.Win.Pct":AdWinInput}

   data=pd.DataFrame(test_dict,index=[0])
   result = loaded_model.predict(data)
   result = str(result)
  
   return result

@app.route("/")
def home():
    return render_template ('index.html')


if __name__ == "__main__":
    app.run()
