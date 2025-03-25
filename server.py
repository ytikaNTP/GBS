from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import time
from datetime import datetime

app = Flask(__name__, static_folder='static')

# Настройка CORS с явным разрешением всех источников
CORS(app, 
     resources={
         r"/*": {
             "origins": "*",
             "methods": ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
             "allow_headers": ["Content-Type"]
         }
     },
     supports_credentials=True)

# Хранилище данных
tickets = []
activity_log = []

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, PATCH, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/tickets', methods=['GET', 'POST', 'OPTIONS'])
def handle_tickets():
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
            
            # Валидация обязательных полей
            required = ['phone', 'name', 'productLink', 'comment']
            if not all(data.get(field) for field in required):
                return jsonify({
                    "status": "error",
                    "message": "Не заполнены обязательные поля"
                }), 400

            # Создание нового тикета
            new_ticket = {
                "id": int(time.time() * 1000),
                "phone": data['phone'],
                "name": data['name'],
                "productLink": data['productLink'],
                "comment": data['comment'],
                "social": data.get('social', ''),
                "images": data.get('images', [])[:5],
                "tags": [],
                "created_at": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                "status": "new"
            }

            tickets.append(new_ticket)
            log_activity(f"Создана заявка #{new_ticket['id']}")
            
            return jsonify({
                "status": "success",
                "ticket": new_ticket
            }), 201

        except Exception as e:
            print(f"Ошибка: {str(e)}")
            return jsonify({
                "status": "error",
                "message": "Внутренняя ошибка сервера"
            }), 500

    elif request.method == 'GET':
        sorted_tickets = sorted(tickets, key=lambda x: x['id'], reverse=True)
        return jsonify(sorted_tickets)

    return jsonify({"status": "success"})

@app.route('/tickets/<int:ticket_id>', methods=['DELETE', 'PATCH', 'OPTIONS'])
def handle_ticket(ticket_id):
    ticket = next((t for t in tickets if t['id'] == ticket_id), None)
    if not ticket:
        return jsonify({
            "status": "error",
            "message": "Заявка не найдена"
        }), 404

    if request.method == 'DELETE':
        try:
            tickets.remove(ticket)
            log_activity(f"Удалена заявка #{ticket_id}")
            return jsonify({"status": "success"}), 200
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500

    elif request.method == 'PATCH':
        try:
            data = request.get_json()
            if 'tags' in data:
                valid_tags = {'contacting', 'rejected', 'spam', 'clown'}
                ticket['tags'] = [
                    tag for tag in list(set(data['tags']))
                    if tag in valid_tags
                ]
                log_activity(f"Обновлены теги для #{ticket_id}")
            
            return jsonify({
                "status": "success",
                "ticket": ticket
            }), 200
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500

    return jsonify({"status": "error"}), 405

@app.route('/activity', methods=['GET'])
def get_activity():
    return jsonify(activity_log[-10:])

def log_activity(message):
    activity_log.append({
        "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "message": message
    })

@app.route('/')
def serve_frontend():
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    if not os.path.exists('static'):
        os.makedirs('static', exist_ok=True)
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        threaded=True
    )
