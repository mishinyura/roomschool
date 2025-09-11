export class Notification {
    constructor(clsContainer) {
        this.cls = clsContainer;
        this.container = document.querySelector(`.${this.cls}`)
    }

    create(message) {
        const notification = document.createElement('div')
        const btn = document.createElement('button')
        const decription = document.createElement('p')
        

        notification.className = `${this.cls}__message`;
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

    showMessage(message = "No message", timeout = 6000) {
        const obj = this.create(message);
        requestAnimationFrame(() => {
            obj.notification.classList.add('show');
        });
        setTimeout(() => this.delete(obj.notification), timeout);
    }
}