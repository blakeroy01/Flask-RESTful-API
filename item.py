import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field can not be left blank"
    )

    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        
        return {'message': 'Item not found'}, 404

    
    @classmethod
    def find_by_name(Item, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return{'item': {'name': row[0], 'price': row[1]}}

    @jwt_required()
    def post(self, name):

        # Error first approach
        if self.find_by_name(name):
            return {'message': "An item with name '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()

        item = {
            'name': name,
            'price': data['price']
        }

        try:
            self.insert(item)
        except:
            return {'message': "An error occured"}, 500

        return item, 201

    @classmethod
    def insert(Item, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

    @jwt_required()
    def delete(self, name):
        if self.find_by_name(name):
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = "DELETE FROM items WHERE name=?"
            cursor.execute(query,(name,))
            connection.commit()
            connection.close()
            return {'message': "Item: '{}' Deleted".format(name)}

        return {'message': "Item: '{}' was not found!".format(name)}

    @jwt_required()
    def put(self, name):

        data = Item.parser.parse_args()

        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}

        if item is None:
            try:
                self.insert(updated_item)
            except:
                return {'message': "An error occured inserting"}, 500
        else:
            try:
                self.update(updated_item)
            except:
                return {'message': "An error occured inserting"}, 500
        return item

    def update(Item, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'], item['name']))

        connection.commit()
        connection.close()

class ItemList(Resource):
    def get(self):
        return {'items': items}
