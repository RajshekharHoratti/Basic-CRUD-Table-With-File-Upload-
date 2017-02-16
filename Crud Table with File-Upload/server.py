import os
from flask import Flask, render_template, request, jsonify
import json
import ntpath

__author__ = 'Rajshekhar Horatti'
app = Flask(__name__, static_url_path='/static')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def AddAsset(data):
    try:
        with open('/home/raj/Documents/MyProjects/Crud Table/Assets/data.json') as f:
            addasset = json.load(f)
            addasset.append(data)
            with open('/home/raj/Documents/MyProjects/Crud Table/Assets/data.json', 'w') as f:
                json.dump(addasset, f)

    except:
        addasset = []
        addasset.append(data)
        with open('/home/raj/Documents/MyProjects/Crud Table/Assets/data.json', 'w') as f:
            json.dump(addasset, f)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/", methods=['GET', 'POST'])
def CreateAsset():
    target = os.path.join(APP_ROOT)
    name = request.form['name']
    id = request.form['id']
    videofile = request.form['file']
    head, tail = ntpath.split(videofile)
    Data = {
        'name': name,
        'id': id,
        'file': tail,
    }
    AddAsset(Data)

    return render_template("index.html")


@app.route("/assets", methods=['GET'])
def assets():
    with open('/home/raj/Documents/MyProjects/Crud Table/Assets/data.json') as f:
        showassets = json.load(f)
        return json.dumps(showassets)


@app.route("/assets/", methods=['DELETE'])
def AssetDEL():
    print('WRITE CODE TO DELETE ASSET')


@app.route("/assets/", methods=['GET'])
def AssetGET():
    id = request.args.get('id')
    with open('/home/raj/Documents/MyProjects/Crud Table/Assets/data.json') as f:
        item = json.load(f)
        for i in item:
            if i.get('id') == id:
                getasset = i
        return jsonify(getasset)


@app.route("/assets/", methods=['POST', 'PUT'])
def AssetPUTPOST():
    print('WRITE CODE TO UPDATE ASSET')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)