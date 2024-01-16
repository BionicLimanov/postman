from json import dumps
import json
import pprint
from flask import Flask, request, jsonify
import flask
import requests

app = Flask(__name__)


url = "http://10.1.111.7:30809/api/collections/ENV/records/"
response = requests.get(url)
@app.get("/bebas")
def get_bebas():
    
    # buat dic baru trs print custom
    data = response.json()
    response_data= []
    for item in data["items"]:
        response_data.append({
            "hdfs_api": item["HDFS_API"],
            "HDFS_datanote":item["HDFS_PORT"]
        })
        # custom response
    response_json = {
        "halo " : "test1",
        "halo" : "test2",
        "response" : response_data
    }
    

    return response_json



@app.post("/postkepostman")
def post_bebas():
    url = "http://10.1.111.7:30809/api/collections/ENV/records/"
    resp_json = request.get_json()
    response = requests.post(url, json=resp_json)

    return response.json()


@app.delete("/deletedata/<url_param>")
def delete_bebas(url_param):
    url = "http://10.1.111.7:30809/api/collections/ENV/records/" + url_param
    response = requests.delete(url)

    return "complete"


# buat dic baru trs print custom
# data = response.json()
# response_json= []
# for item in data["items"]:
#     response_data.append({
#         "hdfs_api": item["HDFS_API"],
#         "HDFS_datanote":item["HDFS_PORT"]
#     })
#     # custom response
#     response_json = {

#     }

# print(get_bebas())

# pala = print(json.dumps(get_bebas, indent=4))
# pprint(get_bebas)



if __name__ == "__main__":
    app.run(debug=True)