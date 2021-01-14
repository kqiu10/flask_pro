from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Student(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with same name '{}' already exists.".format(name)}, 400
        data = request.get_json()
        item = {"name": name, "price": 12.00}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Student, "/student/<string:name>")  # http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
