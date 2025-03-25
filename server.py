from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import time
from datetime import datetime
import logging

app = Flask(__name__, static_folder='static')
CORS(app, supports_credentials=True, origins="*")

# Настройка логирования
logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Временное хранилище данных
tickets = []
activity_log = []

@app.route('/tickets', methods=['GET', 'POST'])
def handle_tickets():
    if request.method == 'POST':
        try:
            data = request.json
            
            # Валидация обязательных полей
            required_fields = ['phone', 'name', 'productLink', 'comment']
            missing_fields = [field for field in required_fields if not data.get(field)]
            if missing_fields:
                return jsonify({
                    "status": "error",
                    "message": f"Не заполнены обязательные поля: {', '.join(missing_fields)}"
                }), 400

            # Создание нового тикета
            new_ticket = {
                "id": int(time.time() * 1000),
                "phone": data['phone'],
                "name": data['name'],
                "productLink": data['productLink'],
                "comment": data['comment'],
                "social": data.get('social', ''),
                "images": data.get('images', [])[:5],  # Лимит 5 изображений
                "tags": [],
                "created_at": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                "status": "new"
            }

            tickets.append(new_ticket)
            log_activity(f"Создана заявка: {new_ticket['name']} (ID: #{new_ticket['id']})")
            
            return jsonify({
                "status": "success",
                "ticket": new_ticket
            }), 201

        except Exception as e:
            app.logger.error(f"Ошибка создания заявки: {str(e)}")
            return jsonify({
                "status": "error", 
                "message": "Внутренняя ошибка сервера"
            }), 500

    elif request.method == 'GET':
        # Сортировка по дате (новые сверху)
        sorted_tickets = sorted(tickets, key=lambda x: x['id'], reverse=True)
        return jsonify(sorted_tickets)

@app.route('/tickets/<int:ticket_id>', methods=['DELETE', 'PATCH'])
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
            app.logger.error(f"Ошибка удаления заявки: {str(e)}")
            return jsonify({
                "status": "error",
                "message": "Ошибка при удалении"
            }), 500

    elif request.method == 'PATCH':
        try:
            data = request.json
            if 'tags' in data:
                # Валидация и обработка тегов
                valid_tags = {'contacting', 'rejected', 'spam', 'clown'}
                new_tags = list(set([tag for tag in data['tags'] if tag in valid_tags]))
                ticket['tags'] = new_tags
                log_activity(f"Обновлены теги для заявки #{ticket_id}")
            
            return jsonify({
                "status": "success",
                "ticket": ticket
            }), 200
        except Exception as e:
            app.logger.error(f"Ошибка обновления тегов: {str(e)}")
            return jsonify({
                "status": "error",
                "message": "Ошибка обновления"
            }), 500

@app.route('/activity')
def get_activity():
    return jsonify(activity_log[-10:])  # Последние 10 записей

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
    app.run(host='0.0.0.0', port=5000)
