document.addEventListener('DOMContentLoaded', function() {
    const jsonField = document.querySelector('#id_contacts');
    if (jsonField) {
        jsonField.addEventListener('blur', function() {
            try {
                JSON.parse(this.value);
                this.classList.remove('is-invalid');
            } catch (e) {
                this.classList.add('is-invalid');
                const errorDiv = this.nextElementSibling;
                if (errorDiv && errorDiv.classList.contains('form-help-text')) {
                    errorDiv.innerHTML = 'Ошибка в JSON: ' + e.message + '<br>' + errorDiv.textContent;
                    errorDiv.style.color = 'red';
                }
            }
        });
    }
});