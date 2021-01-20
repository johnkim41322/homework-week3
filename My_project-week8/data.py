from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbsparta

areas = []
areas.append({"area_idx":1, "text":"강원"})
db.areas.insert_many(list(areas))

sizes = []
sizes.append({"size_idx":1, "text":"245/45/20"})
sizes.append({"size_idx":2, "text":"255/45/20"})
sizes.append({"size_idx":3, "text":"265/45/20"})
db.sizes.insert_many(list(sizes))

manufacturers = []
manufacturers.append({"manufacturer_idx":1, "text":"벤츠"})
manufacturers.append({"manufacturer_idx":2, "text":"현대"})
manufacturers.append({"manufacturer_idx":3, "text":"기아"})
manufacturers.append({"manufacturer_idx":4, "text":"쉐보레"})
db.manufacturers.insert_many(list(manufacturers))

models = []
models.append({"manufacturer_idx":1, "model_idx":1, "text":"S-Class"})
models.append({"manufacturer_idx":1, "model_idx":2, "text":"E-Class"})
models.append({"manufacturer_idx":1, "model_idx":3, "text":"C-Class"})
models.append({"manufacturer_idx":1, "model_idx":4, "text":"A-Class"})
db.models.insert_many(list(models))

prices = []
prices.append({"manufacturer_idx":1, "model_idx":1, "size_idx":1, "price":"50000", "WorkshopIdxs":[1,2]})
db.prices.insert_many(list(prices))