document.addEventListener('DOMContentLoaded', function() {
    // Добавление контакта
    const addContactBtn = document.getElementById('add-contact');
    if (addContactBtn) {
        addContactBtn.addEventListener('click', function() {
            const contactType = document.getElementById('id_new_contact_type');
            const contactValue = document.getElementById('id_new_contact_value');
            
            if (!contactType.value.trim() || !contactValue.value.trim()) {
                alert('Заполните оба поля контакта!');
                return;
            }
            
            // В реальном проекте здесь может быть AJAX-запрос
            document.getElementById('company-form').submit();
        });
    }

    // Удаление контакта
    document.querySelectorAll('.remove-contact').forEach(btn => {
        btn.addEventListener('click', function() {
            const contactType = this.dataset.contactType;
            const companyId = this.closest('form').dataset.companyId;
            
            if (confirm(`Удалить контакт ${contactType}?`)) {
                fetch(`/api/${companyId}/delete-contact/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken'),
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: `contact_type=${encodeURIComponent(contactType)}`
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        this.closest('.list-group-item').remove();
                    } else {
                        alert('Ошибка: ' + (data.error || 'Неизвестная ошибка'));
                    }
                });
            }
        });
    });

    // Валидация видов деятельности
    const activitiesField = document.getElementById('id_activity_themes');
    if (activitiesField) {
        activitiesField.addEventListener('blur', function() {
            const lines = this.value.split('\n').filter(line => line.trim());
            if (lines.length === 0) {
                this.classList.add('is-invalid');
            } else {
                this.classList.remove('is-invalid');
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