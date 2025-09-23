// export class Accordion{
//     /**
//      * 
//      * @param {String} name Селектор контейнера, в котором список элементов
//      * @param {String} btns Селектор кнопок, под которыми детальное описание
//      * @param {Boolean} collapse True - при открытии одного, открытый ранее соваричается
//      */
//     constructor({name, btns, items, collapse}){
//         this.accordion = document.querySelector(name)
//         this.btns = this.accordion.querySelectorAll(btns)
//         this.collapse = collapse

//         this.handlerClickBtn = this.clickBtn.bind(this)


//         for (let btn of this.btns) {
//             btn.addEventListener('click', this.handlerClickBtn)
//         }
//     }

//     open(btn){
//         let detail = btn.nextElementSibling
//         detail.classList.add('open')
//         detail.style.height = `${detail.scrollHeight + 25}px`
//         btn.classList.add('open')
//     }

//     close(btn){
//         btn.classList.remove('open')
//         let detail = btn.nextElementSibling
//         detail.classList.remove('open')
//         detail.style.height = 0;
//     }

//     closeAll() {
//         let detail;
//         for (let btn of this.btns) {
//             btn.classList.remove('open')
//             detail = btn.nextElementSibling
//             detail.classList.remove('open')
//             detail.style.height = 0;
//         }
//     }

//     clickBtn(btn) {
//         if (this.collapse) {
//             this.closeAll()
//             this.open(btn.currentTarget)
//         } else {
//             if (btn.currentTarget.classList.contains('open')) {
//                 this.close(btn.currentTarget)
//             } else {
//                 this.open(btn.currentTarget)
//             }
//         }

//     }
// }




export class Accordion {
    /**
     * @param {Object} options
     * @param {String} options.name  - селектор контейнера
     * @param {String} options.btns  - селектор кнопок
     * @param {Boolean} options.collapse - при открытии одного закрывать остальные
     */
    constructor({ name, btns, collapse = true }) {
        this.container = document.querySelector(name);
        if (!this.container) throw new Error('Accordion: container not found ' + name);

        this.btns = Array.from(this.container.querySelectorAll(btns));
        this.collapse = collapse;
        this._onClick = this._onClick.bind(this);

        this.btns.forEach(btn => btn.addEventListener('click', this._onClick));
    }

    // обработчик клика
    _onClick(e) {
        const btn = e.currentTarget;
        const detail = btn.nextElementSibling;
        if (!detail) return;

        if (btn.classList.contains('open')) {
            this._close(detail, btn);
        } else {
            if (this.collapse) this.closeAll();
            this._open(detail, btn);
        }
    }

    _open(detail, btn) {
        // защита от повторного открытия
        if (detail.classList.contains('open')) return;

        // Гарантируем начальное состояние для анимации
        detail.style.height = '0px';

        // Добавляем класс, который может задать padding/borders и т.д.
        detail.classList.add('open');
        btn.classList.add('open');

        // Получаем итоговую высоту (включая padding)
        const targetHeight = detail.scrollHeight;

        // Форсируем reflow чтобы браузер увидел начальное значение height = 0
        // затем устанавливаем конечную высоту — произойдёт плавная анимация
        detail.getBoundingClientRect(); // force reflow
        detail.style.height = targetHeight + 'px';
    }

    _close(detail, btn) {
        if (!detail.classList.contains('open')) return;

        // Устанавливаем текущую реальную высоту (если сейчас height:auto)
        const currentHeight = detail.scrollHeight;
        detail.style.height = currentHeight + 'px';

        // Форсируем reflow, затем анимируем до нуля
        detail.getBoundingClientRect();
        detail.style.height = '0px';

        // По окончании анимации — убираем класс и inline-height
        detail.addEventListener('transitionend', () => {
            detail.classList.remove('open');
            btn.classList.remove('open');
            detail.removeAttribute('style')
        }, { once: true });
    }

    closeAll() {
        for (const btn of this.btns) {
            if (btn.classList.contains('open')) {
                const detail = btn.nextElementSibling;
                if (detail) this._close(detail, btn);
            }
        }
    }

    // Убрать обработчики (если нужно)
    destroy() {
        for (const btn of this.btns) {
            btn.removeEventListener('click', this._onClick);
        }
    }
}