from flask import Flask, jsonify, request
from config import Config
from models import Message
from crypto import encrypt_text, decrypt_token

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error' : 'آدرس پیدا نشد'}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'error' : 'خطای داخلی سرور'}), 500

@app.route('/')
def home():
    return jsonify({
        'message' : 'رمزنگاری حرفه ای API',
        'endpoints' : [
            '/encrypt',
            '/decrypt'
        ]
    }), 200

#----------------------------رمزنگاری-----------------------------

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()

    if not data:
        return jsonify({'error' : 'بدنه درخواست خالی است'}), 400
    
    if 'text' not in data or not data['text']:
        return jsonify({'error' : 'خالی است text فیلد'}), 400
    
    token = encrypt_text(data['text'])

    msg = Message.create(encrypted=token)

    return jsonify({
        'id' : msg.id,
        'token' : token
    }), 201

#----------------------------رمزگشایی-----------------------------

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()

    if not data:
        return jsonify({'error' : 'بدنه درخواست خالی است'}), 400
    
    if 'token' not in data or not data['token']:
        return jsonify({'error' : 'خالی است token فیلد'}), 400    
    
    text, error = decrypt_token(data['token'])

    if error:
        return jsonify({'error' : error}), 400
    
    return jsonify({'text' : text}), 200

if __name__ == '__main__' :
    app.run(debug=True)