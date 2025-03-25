<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GreenBottle | Cashback System</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <button class="btn admin-btn" onclick="showAdminLogin()">
        🔒 Админ-панель
    </button>

    <div class="main-container" id="mainContainer">
        <!-- Прогресс-бар -->
        <div class="progress-bar">
            <div class="progress-item active">
                <div class="progress-bubble">1</div>
                Подготовка
            </div>
            <div class="progress-item">
                <div class="progress-bubble">2</div>
                Инструкция
            </div>
            <div class="progress-item">
                <div class="progress-bubble">3</div>
                Анкета
            </div>
        </div>

        <!-- Шаг 1: Подготовка -->
        <div class="step active" id="step1">
            <h2>📸 Шаг 1: Подготовка</h2>
            <ul>
                <li>Скриншот личного кабинета с покупкой</li>
                <li>Ссылка на купленный товар</li>
                <li>Скриншот 5-звёздочного отзыва</li>
            </ul>
            <button class="btn" onclick="nextStep()">Далее →</button>
        </div>

        <!-- Шаг 2: Инструкция -->
        <div class="step" id="step2">
            <h2>📋 Правила заполнения</h2>
            <ol>
                <li>Указывайте только правдивую информацию</li>
                <li>Номер телефона должен быть привязан к карте</li>
                <li>Укажите банк для перевода в комментарии</li>
            </ol>
            <button class="btn" onclick="nextStep()">Продолжить →</button>
        </div>

        <!-- Шаг 3: Анкета -->
        <div class="step" id="step3">
            <h2>✍️ Заполните анкету</h2>
            <form id="ticketForm" class="compact-form">
                <div class="form-group">
                    <label>Телефон</label>
                    <input type="tel" name="phone" pattern="\+7\d{10}" placeholder="+7 XXX XXX XX XX" required>
                </div>

                <div class="form-group">
                    <label>ФИО/Псевдоним</label>
                    <input type="text" name="name" placeholder="Иван Иванов" required>
                </div>

                <div class="form-group">
                    <label>Ссылка на товар</label>
                    <input type="url" name="productLink" placeholder="https://www.ozon.ru/" required>
                </div>

                <div class="form-group">
                    <label>Комментарий (банк)</label>
                    <textarea name="comment" placeholder="FPIbank Как с вами связаться?" rows="3" required></textarea>
                </div>

                <div class="form-group">
                    <label>Профиль в соц. сети (Telegram, VK, OK ...)</label>
                    <input type="url" name="social" placeholder="https://www.ozon.ru/">
                </div>

                <div class="form-group">
                    <label>Скриншоты (макс. 5)</label>
                    <div class="file-upload" onclick="document.getElementById('fileInput').click()">
                        📁 Перетащите или выберите файлы
                    </div>
                    <input type="file" id="fileInput" multiple accept="image/*" hidden>
                    <div id="preview" class="images-preview"></div>
                </div>

                <button type="button" class="btn" onclick="submitForm()">🚀 Отправить</button>
            </form>
        </div>

        <!-- Шаг 4: Подтверждение -->
        <div class="step" id="step4">
            <h2>🎉 Готово!</h2>
            <p>Ваша заявка будет рассмотрена в течение 16 дней.</p>
        </div>
    </div>

    <!-- Админ-панель -->
    <div class="admin-panel" id="adminPanel">
        <div class="admin-header">
            <div>
                <h1>🛠 Панель администратора</h1>
                <button class="btn btn-refresh" onclick="updateAdminPanel()">🔄 Обновить</button>
            </div>
            <button class="btn" onclick="exitAdmin()">← Назад</button>
        </div>

        <div id="ticketsList"></div>
        <div id="pagination"></div>
    </div>

    <script>
        let currentStep = 1;
        let tickets = [];
        let currentPage = 1;
        const ticketsPerPage = 20;

        // Функция для открытия изображений
        function openImageInNewTab(base64) {
            try {
                const byteString = atob(base64.split(',')[1]);
                const mimeString = base64.split(',')[0].split(':')[1].split(';')[0];
                const ab = new ArrayBuffer(byteString.length);
                const ia = new Uint8Array(ab);
                
                for (let i = 0; i < byteString.length; i++) {
                    ia[i] = byteString.charCodeAt(i);
                }
                
                const blob = new Blob([ab], { type: mimeString });
                const url = URL.createObjectURL(blob);
                const win = window.open(url, '_blank');
                win.onload = () => URL.revokeObjectURL(url);
            } catch (error) {
                console.error('Ошибка открытия изображения:', error);
            }
        }

        // Обновление прогресс-бара
        function updateProgress() {
            document.querySelectorAll('.progress-item').forEach((item, index) => {
                item.classList.toggle('active', index + 1 === currentStep);
            });
        }

        // Переход между шагами
        function nextStep() {
            if (currentStep >= 4) return;
            document.querySelector(`#step${currentStep}`).classList.remove('active');
            currentStep++;
            document.querySelector(`#step${currentStep}`).classList.add('active');
            updateProgress();
        }

        // Загрузка изображений
        document.getElementById('fileInput').addEventListener('change', function(e) {
            const preview = document.getElementById('preview');
            preview.innerHTML = '';
            const files = Array.from(e.target.files).slice(0, 5);
            
            files.forEach(file => {
                const reader = new FileReader();
                reader.onload = (event) => {
                    const img = document.createElement('img');
                    img.src = event.target.result;
                    img.style.maxWidth = '150px';
                    img.onclick = () => openImageInNewTab(event.target.result);
                    preview.appendChild(img);
                };
                reader.readAsDataURL(file);
            });
        });

        // Отправка формы
        async function submitForm() {
            const files = Array.from(document.getElementById('fileInput').files).slice(0, 5);
            const images = await Promise.all(files.map(file => {
                return new Promise((resolve) => {
                    const reader = new FileReader();
                    reader.onload = (e) => resolve(e.target.result);
                    reader.readAsDataURL(file);
                });
            }));

            const formData = {
                phone: document.querySelector('input[name="phone"]').value,
                name: document.querySelector('input[name="name"]').value,
                productLink: document.querySelector('input[name="productLink"]').value,
                comment: document.querySelector('textarea[name="comment"]').value,
                social: document.querySelector('input[name="social"]').value,
                images: images
            };

            try {
                const response = await fetch('http://194.87.226.249:5000/tickets', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(formData)
                });

                if (response.ok) {
                    nextStep();
                    document.getElementById('ticketForm').reset();
                    document.getElementById('preview').innerHTML = '';
                }
            } catch (error) {
                console.error('Ошибка:', error);
            }
        }

        // Админ-панель
        async function showAdminLogin() {
            const password = prompt('Пароль администратора:');
            if (password === 'Tymba') {
                document.getElementById('mainContainer').style.display = 'none';
                document.getElementById('adminPanel').style.display = 'block';
                await updateAdminPanel();
            } else {
                alert('Неверный пароль!');
            }
        }

        // Сортировка по тегам
        function sortTickets() {
            const priority = {'contacting':4, 'rejected':3, 'spam':2, 'clown':1};
            return tickets.sort((a, b) => {
                const aMax = Math.max(...a.tags.map(t => priority[t] || 0));
                const bMax = Math.max(...b.tags.map(t => priority[t] || 0));
                return bMax - aMax || b.id - a.id;
            });
        }

        // Обновление списка тикетов
        async function updateAdminPanel() {
            try {
                const response = await fetch('http://194.87.226.249:5000/tickets');
                tickets = await response.json();
                renderTickets();
            } catch (error) {
                console.error('Ошибка:', error);
            }
        }

        // Рендер тикетов
        function renderTickets() {
            const list = document.getElementById('ticketsList');
            const sortedTickets = sortTickets();
            const start = (currentPage - 1) * ticketsPerPage;
            const paginatedTickets = sortedTickets.slice(start, start + ticketsPerPage);
            
            list.innerHTML = paginatedTickets.map(ticket => `
                <div class="ticket-card">
                    <div class="ticket-header">
                        <h3>${ticket.name}</h3>
                        <p>📱 ${ticket.phone}</p>
                    </div>
                    <div class="ticket-content">
                        <p>🛒 Товар: <a href="${ticket.productLink}" target="_blank">${ticket.productLink}</a></p>
                        <p>💬 Комментарий: ${ticket.comment}</p>
                        ${ticket.social ? `<p>🌐 Соцсеть: <a href="${ticket.social}" target="_blank">${ticket.social}</a></p>` : ''}
                        <div class="images-preview">
                            ${ticket.images.map(img => `
                                <img src="${img}" 
                                    alt="Скриншот" 
                                    onclick="openImageInNewTab('${img}')">
                            `).join('')}
                        </div>
                        <div class="tags-container">
                            <div class="tag ${ticket.tags.includes('contacting') ? 'active' : ''}" 
                                onclick="toggleTag('contacting', ${ticket.id})">📞 Связываюсь...</div>
                            <div class="tag ${ticket.tags.includes('rejected') ? 'active' : ''}" 
                                onclick="toggleTag('rejected', ${ticket.id})">🚫 Отклонено</div>
                            <div class="tag ${ticket.tags.includes('spam') ? 'active' : ''}" 
                                onclick="toggleTag('spam', ${ticket.id})">💣 Спам</div>
                            <div class="tag ${ticket.tags.includes('clown') ? 'active' : ''}" 
                                onclick="toggleTag('clown', ${ticket.id})">🤡 Клоун</div>
                        </div>
                        <button class="btn" onclick="deleteTicket(${ticket.id})">Удалить</button>
                    </div>
                </div>
            `).join('');

            renderPagination();
        }

        // Пагинация
        function renderPagination() {
            const totalPages = Math.ceil(tickets.length / ticketsPerPage);
            const pagination = document.getElementById('pagination');
            pagination.innerHTML = '';
            
            for (let i = 1; i <= totalPages; i++) {
                const btn = document.createElement('button');
                btn.className = `btn ${i === currentPage ? 'active' : ''}`;
                btn.textContent = i;
                btn.onclick = () => {
                    currentPage = i;
                    renderTickets();
                };
                pagination.appendChild(btn);
            }
        }

        // Управление тегами
        async function toggleTag(tag, id) {
            const ticket = tickets.find(t => t.id === id);
            const newTags = ticket.tags.includes(tag) 
                ? ticket.tags.filter(t => t !== tag) 
                : [...ticket.tags, tag];

            try {
                await fetch(`http://194.87.226.249:5000/tickets/${id}`, {
                    method: 'PATCH',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ tags: newTags })
                });
                ticket.tags = newTags;
                renderTickets();
            } catch (error) {
                console.error('Ошибка:', error);
            }
        }

        // Удаление тикета
        async function deleteTicket(id) {
            if (!confirm('Вы уверены, что хотите удалить заявку?')) return;
            await fetch(`http://194.87.226.249:5000/tickets/${id}`, { method: 'DELETE' });
            await updateAdminPanel();
        }

        // Выход из админ-панели
        function exitAdmin() {
            document.getElementById('mainContainer').style.display = 'block';
            document.getElementById('adminPanel').style.display = 'none';
        }

        updateProgress();
    </script>
</body>
</html>
