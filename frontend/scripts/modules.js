import { NOTIFICATION_TEMPLATES } from './notifications-templates.js';

class Notification {
    constructor(clsName, templates = NOTIFICATION_TEMPLATES) {
        this.container = document.querySelector(`.${clsName}`);
        this.description = this.container.querySelector(`.${clsName}__descr`);
        this.title = this.container.querySelector(`.${clsName}__title`);
        this.templates = templates;

    }

    setNotification({ type, code, params = {} }) {
        const typeError = this.templates[type];
        if (!typeError) throw new Error('Unknown notification type');
        const title = interpolate(typeError.title, params);
        const descTemplate = typeError.descriptions[code];
        const description = interpolate(descTemplate, params);

        this.title.innerText = title;
        this.description.innerText = description;
    }

    showMessage() {
        this.container.classList.add('show');
        setTimeout(() => {
            this.container.classList.remove('show');
        }, 6000);
    }
}

class Forms {
    constructor(nameForm){
        this.authForm = document.forms[nameForm]
        if (!this.authForm) throw new Error('Форма не найдена!');
        this.fields = Array.from(this.authForm.elements).filter(
            field => field.tagName === 'INPUT' || 
            field.tagName === 'TEXTAREA'
        )
        
        this.formValidate = this.formValidate.bind(this)

        for (let filed of this.fields) {
            filed.addEventListener('blur', this.formValidate)
        }
        console.log(this.fields)
    }

    async editViewLogin(btn) {
        let form = btn.closest('form')
        btn.addEventListener('click', async () => {
            //Отправляем данные на сервер, 
            //чтобы получить разрешение, 
            //если сервер возвращает список,
            //формируем список доступных аккаунтов и даем выбор
            let response = await request()
            form = new FormData(form)
            console.log(form)
            if (response.length > 1) {
                let accountsContainer = document.querySelector('.choise');
                let authContainer = document.querySelector('.auth');
                let accounts = accountsContainer.querySelectorAll('.choise__item');
                for (let acc of accounts) {
                    if (response.includes(acc.dataset.account)) {
                        acc.classList.add('active')
                    }
                }
                accountsContainer.classList.add('active')
                authContainer.classList.remove('active')
            } else {
                //если аккаунт 1, то редиректим сразу на него
                console.log('Redirect on profile')
            }
        })
    }

    passwordValidate(value){
        console.log(value)
    }

    loginValidate(){

    }

    formValidate(elem){
        switch (elem.currentTarget.name) {
            case 'login':
                this.loginValidate()
                break;
            case 'password':
                this.passwordValidate(elem.currentTarget.value)
                break;
        }
    }

    

}


class Slider {
    constructor(config){
        if (this.configValidate(config)) {
            this.container = document.querySelector(config.container)
            this.slider = this.container.querySelector('ul')
            this.cards = this.slider.querySelectorAll('li')

            this.prevBtn = this.container.querySelector(config.prev)
            this.nextBtn = this.container.querySelector(config.next)

            this.showNextSlide = this.showNextSlide.bind(this)
            this.showPrevSlide = this.showPrevSlide.bind(this)

            this.prevBtn.addEventListener('click', this.showPrevSlide)
            this.nextBtn.addEventListener('click', this.showNextSlide)
        }

        this.getSliderParams()
    }

    configValidate(data){
        if (!data.container) {
            throw new Error('Укажите клас или идентификатор общего контейнера с вашим слайдером')
        }

        return true
    }

    getSliderParams(){
        this.widthContainer = this.container.getBoundingClientRect().width;
        this.heightContainer = this.container.getBoundingClientRect().height;
        this.widthSlider = this.slider.getBoundingClientRect().width;
        this.heightSlider = this.slider.getBoundingClientRect().height;
        this.widthCard = this.cards[0].getBoundingClientRect().width;
        this.heightCard = this.cards[0].getBoundingClientRect().height;

        console.log(this.widthSlider)
    }

    showNextSlide(){
        console.log('next')
    }

    showPrevSlide(){
        console.log('prev')
    }
}


class Header{
    constructor(clsName) {
        this.header = document.querySelector(`.${clsName}`)
        this.editStyle = this.editStyle.bind(this)
        window.addEventListener('scroll', this.editStyle)
    }

    editStyle(el) {
        if (window.scrollY > 0) {
            this.header.classList.add('scrolled');
        } else {
            this.header.classList.remove('scrolled');
        }
    }
}

// let acc = new Forms('authorizationForm');
// let header = new Header('header')

const slider = new Slider({
    container: '.slider',
    prev: '.prev',
    next: '.next'
})