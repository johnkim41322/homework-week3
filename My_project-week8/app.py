from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():  # 함수명 수정 - 이름만 보고 접속되는 페이지를 확인할 수 있게!
    return render_template('index.html')

@app.route('/list')
def list_page():  # 함수명 수정 - 이름만 보고 접속되는 페이지를 확인할 수 있게!
    return render_template('list.html')

@app.route('/areas', methods=['GET'])
def getArea():
    areas = list(db.areas.find({}, {"_id":False}))
    return jsonify({'result': "success", "areas":areas})

@app.route('/sizes', methods=['GET'])
def getSize():
    sizes = list(db.sizes.find({},{"_id":False}))
    return jsonify({'result': "success", "sizes":sizes})

@app.route('/manufacturers', methods=['GET'])
def getManufacturers():
    manufacturers = list(db.manufacturers.find({},{"_id":False}))
    return jsonify({'result': "success", "manufacturers":manufacturers})

@app.route('/models', methods=['GET'])
def getModels():
    manufacturer_idx = request.args.get("manufacturer_idx")
    models = list(db.models.find({"manufacturer_idx":int(manufacturer_idx)},{"_id":False}))
    return jsonify({'result': "success", "models":models})

@app.route('/stores', methods=['GET'])
def getStroes():
    area = request.args.get("area")
    size_idx = request.args.get("size_idx")
    manufacturer_idx = request.args.get("manufacturer_idx")
    model_idx = request.args.get("model_idx")
    price = db.prices.find_one({"size_idx":int(size_idx), "manufacturer_idx":int(manufacturer_idx), "model_idx":int(model_idx)},{"_id":False})
    stores = list(db.stores.find({"Area1":area, "WorkshopIdx":{"$in":price["WorkshopIdxs"]}},{"_id":False}))

    return jsonify({'result': "success", "stores":stores})

@app.route('/store', methods=['POST'])
def setStore():
    content = request.json
    print(content['stores'])
    db.stores.insert_many(content['stores'])
    return jsonify({'result': "success"})

@app.route('/tire', methods=['POST'])
def setTire():
    return jsonify({'result': "success"})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)