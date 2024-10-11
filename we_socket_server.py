from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()
app = Flask(__name__)

class WebSocketServer:
    def __init__(self, debug=False):
        self.create_app(debug)

    def create_app(self, debug=False):
        app.debug = debug
        socketio.init_app(app, cors_allowed_origins="*")
        return app

# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.hash_table = self.create_buckets()
#
#     def create_buckets(self):
#         return [[] for _ in range(self.size)]
#
#     def set_val(self, key, val):
#         hashed_key = hash(key) % self.size
#         bucket = self.hash_table[hashed_key]
#         found_key = False
#         for index, record in enumerate(bucket):
#             record_key, record_val = record
#             if record_key == key:
#                 found_key = True
#                 break
#         self.hash_table[key].append(val)
#
#     def get_val(self, key):
#         return self.hash_table[key]
#
#     def __str__(self):
#         return str(self.hash_table)
#
#     def __repr__(self):

