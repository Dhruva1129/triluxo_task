from flask_restful import Api, Resource
from app import app
from app.chatbot import Chatbot

api = Api(app)
api.add_resource(Chatbot, '/chat')
