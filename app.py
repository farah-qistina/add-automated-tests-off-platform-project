from flask import Flask, jsonify, request

app = Flask(__name__)

balance = 0

