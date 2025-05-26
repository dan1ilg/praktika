document.addEventListener('DOMContentLoaded', function() {
    // Обработка модального окна контактов
    var contactsModal = document.getElementById('contactsModal');
    
    if (contactsModal) {
        contactsModal.addEventListener('show.bs.modal', function(event) {
            var button = event.relatedTarget;
            
            // Очищаем предыдущие данные
            document.getElementById('modalWebsite').innerHTML = '';
            document.getElementById('modalEmail').innerHTML = '';
            document.getElementById('modalAdditional').innerHTML = '';
            
            // Заполняем данные
            if (button.getAttribute('data-website')) {
                document.getElementById('modalWebsite').innerHTML = 
                    '<p><i class="bi bi-globe me-2"></i><strong>Сайт:</strong> ' + 
                    '<a href="' + button.getAttribute('data-website') + '" target="_blank">' + 
                    button.getAttribute('data-website') + '</a></p>';
            }
            
            if (button.getAttribute('data-email')) {
                document.getElementById('modalEmail').innerHTML = 
                    '<p><i class="bi bi-envelope me-2"></i><strong>Email:</strong> ' + 
                    button.getAttribute('data-email') + '</p>';
            }
            
            if (button.getAttribute('data-additional')) {
                var additionalContacts = button.getAttribute('data-additional').split('\n');
                var additionalHtml = '<div class="mt-3"><strong>Дополнительные контакты:</strong><ul class="list-unstyled">';
                
                additionalContacts.forEach(function(contact) {
                    if (contact.trim()) {
                        additionalHtml += '<li><i class="bi bi-info-circle me-2"></i>' + contact + '</li>';
                    }
                });
                
                additionalHtml += '</ul></div>';
                document.getElementById('modalAdditional').innerHTML = additionalHtml;
            }
        });
    }

    // Валидация приоритета
    const prioritySelect = document.querySelector('select[name="priority"]');
    if (prioritySelect) {
        prioritySelect.addEventListener('change', function() {
            const value = this.value;
            if (value && !/^(10|[1-9])$/.test(value)) {
                this.value = '';
                alert('Приоритет должен быть числом от 1 до 10');
            }
        });
    }

    // Сохраняем фильтры при отправке формы поиска
    const searchForm = document.querySelector('.search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            const priorityFilter = document.querySelector('select[name="priority"]').value;
            const regionFilter = document.querySelector('select[name="region"]').value;
            
            if (priorityFilter) {
                const input = document.createElement('input');
                input.type = 'hidden';
                input.name = 'priority';
                input.value = priorityFilter;
                this.appendChild(input);
            }
            
            if (regionFilter) {
                const input = document.createElement('input');
                input.type = 'hidden';
                input.name = 'region';
                input.value = regionFilter;
                this.appendChild(input);
            }
        });
    }

    // Функция для получения CSRF-токена
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});