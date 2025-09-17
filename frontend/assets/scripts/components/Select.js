/**
 * @module Select
 * @description Объект Select создает кастомный раскрывающийся
 * список, регулирует показ списка и управляет выбором
 */

export class Select{
    constructor(settings) {
        this.container = document.querySelector(settings.obj)
        this.wrapper = this.container.querySelector(settings.input)
        
        this.selected = this.wrapper.querySelector('input')
        this.choices = this.container.querySelectorAll(settings.options)
        this.list = this.choices[0].parentElement
        
        this.handlerShowList = this.showList.bind(this)
        this.handlerHideList = this.hideList.bind(this)

        this.wrapper.addEventListener('click', this.handlerShowList)

        for (let item of this.choices) {
            item.addEventListener('click', this.handlerHideList)
        }
    }

    setChoice(elem) {
        let data = elem.dataset.way
        let value = elem.innerText
        this.selected.dataset.way = data
        this.selected.value = value

        for (let item of this.choices) {
            item.classList.remove('selected')
        }
        elem.classList.add('selected')
    }

    showList() {
        if (!this.list.classList.contains('active')){
            this.list.classList.add('active')
        }
        this.handleOutside = (e) => this.closeIfOutside(e);
        document.addEventListener('click', this.handleOutside);
    }

    closeIfOutside(e) {
        if (this.container.contains(e.target)) return;

        this.list.classList.remove('active');
        document.removeEventListener('click', this.handleOutside);
    }

    hideList(elem) {
        this.list.classList.remove('active')
        this.setChoice(elem.target)
    }
}