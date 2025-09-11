/**
 * @module Form
 * @description Объект Form регистрирует форму, 
 * проводит валидацию при отправке и отправляет результат на сервер
 */


import { NOTIFICATION_TEMPLATES } from '../notifications-templates.js';
import { Notification } from './Notification.js';

export class Form {
    constructor(clsForm) {
        this.cls = `.${clsForm}`;
        this.form = document.querySelector(this.cls);
        this.inputs = this.form.querySelectorAll('input');
        this.submit = this.form.querySelector('button[type=submit]');
        this.notification = new Notification('notifications')

        this.form.addEventListener('submit', this.sendForm.bind(this))
    }

    /**
     * Обработчик отправки формы
     * @param {HTMLElement} form 
     */
    sendForm(form) {
        form.preventDefault();
        this.form = form.target
        
        if (this.validate()) {
            //Тут отправка формы на сервер
        }
    }

    /**
     * Запускает проверку полей из формы
     * @returns {Boolean} true - все поля пошли валидацияю, false - не все
     */
    validate() {
        const form = new FormData(this.form)
        const formData = Object.fromEntries(form.entries())
        let validStatus = true;
        console.log(formData, form);
        for (let input of this.inputs) {
            console.log(input.dataset.validate);
            switch (input.dataset.validate) {
                case 'name': 
                validStatus = this.checkName(input.value)
                break;
                case 'phone': 
                validStatus = this.checkPhone(input.value)
                break;
            }
        }

        return validStatus
    }

    checkName(name) {
        let valid = true;

        name = name.trim();

        if (name.length < 2) {
            valid = false
            this.notification.showMessage(NOTIFICATION_TEMPLATES.forms.nameShort)
        }

        const regex = /^[A-Za-zА-Яа-яЁё\-]+$/;

        if (!regex.test(name)) {
            valid = false
            this.notification.showMessage(NOTIFICATION_TEMPLATES.forms.nameIncorrect)
        }

        return valid;
    }

    checkPhone(phone) {
        let valid = true;
        phone = phone.trim();
        // убираем все символы кроме цифр
        const digits = phone.replace(/\D/g, '');

        // проверяем количество цифр
        if (digits.length < 11 || digits.length > 15) {
            valid = false;
            this.notification.showMessage(NOTIFICATION_TEMPLATES.forms.phoneShort);
        }

        // регулярка: допустимые символы
        const regex = /^\+?[0-9\s\-\(\)]+$/;

        if (!regex.test(phone)) {
            valid = false
            this.notification.showMessage(NOTIFICATION_TEMPLATES.forms.phoneIncorrect)
        }

        return valid;
    }
}