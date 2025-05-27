document.addEventListener('DOMContentLoaded', function() {
    // Обработка модального окна контактов
    var contactsModal = document.getElementById('contactsModal');
    
    if (contactsModal) {
        contactsModal.addEventListener('show.bs.modal', function(event) {
            var button = event.relatedTarget;
            
            document.getElementById('modalWebsite').innerHTML = '';
            document.getElementById('modalEmail').innerHTML = '';
            document.getElementById('modalAdditional').innerHTML = '';
            
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
                var additionalHtml = '<div class="mt-3"><strong>Дополнительные сведения:</strong><ul class="list-unstyled">';
                
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

    // Обработка формы фильтров в модальном окне
    const filterForm = document.getElementById('filterForm');
    if (filterForm) {
        filterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const params = new URLSearchParams();
            
            for (const [key, value] of formData.entries()) {
                if (value) {
                    if (key === 'activity') {
                        formData.getAll(key).forEach(val => params.append(key, val));
                    } else {
                        params.append(key, value);
                    }
                }
            }
            
            const modal = bootstrap.Modal.getInstance(document.getElementById('filterModal'));
            modal.hide();
            
            window.location.href = `${window.location.pathname}?${params.toString()}`;
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