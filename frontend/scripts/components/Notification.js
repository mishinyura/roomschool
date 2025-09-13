/**
 * @module Notification
 * @description Объект Notification создает сообщение на странице,
 * управляет показом и удаляет после демонстрации
 */

export class Notification {
    constructor(clsContainer) {
        this.cls = clsContainer;
        this.container = document.querySelector(`.${this.cls}`)
    }

    create(message, success=false) {
        const notification = document.createElement('div')
        const btn = document.createElement('button')
        const decription = document.createElement('p')
        
        if (success) {
            notification.className = `${this.cls}__message ${this.cls}__message_ok`;
        } else {
            notification.className = `${this.cls}__message ${this.cls}__message_error`;
        }
        notification.setAttribute('role', 'alert');
        notification.setAttribute('aria-live', 'assertive');
        btn.className = `${this.cls}__btn`
        decription.className = `${this.cls}__descr`
        decription.innerText = message

        notification.append(btn, decription)
        this.container.appendChild(notification)

        notification.querySelector(`.${this.cls}__btn`).addEventListener('click', () => {
            this.delete(notification);
        });

        return {notification, decription}
    }

    delete(notification) {
        notification.classList.remove('show');
        notification.addEventListener('transitionend', () => {
            notification.remove();
        }, { once: true });
    }

    showMessage(message = "No message", success=false, timeout = 6000) {
        const obj = this.create(message, success);
        requestAnimationFrame(() => {
            obj.notification.classList.add('show');
        });
        setTimeout(() => this.delete(obj.notification), timeout);
    }
}