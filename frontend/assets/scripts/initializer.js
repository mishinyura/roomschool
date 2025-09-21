/**
 * @module initializer
 * @description Модуль хранит в себе функции с инициализацией
 * страниц. Каждая функция относится к одной странице и вызывается
 * при загрузке DOM.
 */

import { InputMask } from '../../assets/scripts/components/InputMask.js'
import { Form } from '../../assets/scripts/components/Form.js'
import { Select } from '../../assets/scripts/components/Select.js'
import { Header } from '../../assets/scripts/components/Header.js'

/**
 * Инциализация основной страницы
 */
export function indexInit() {
    new InputMask('#inputPhoneNumber')
    const formCallback = new Form('callback__form')
    const selectCallback = new Select({
        obj: '.callback__select',
        input: '.callback__wrapper',
        options: '.callback__item'
    })
    const header = new Header('.header')

    const coursesSlider = new Swiper('.tickets', {
        direction: 'horizontal',
        loop: true,
        freeMode: true,
        slidesPerView: 3,
        spaceBetween:  40,
        wrapperClass: 'tickets__wrapper',
        slideClass: 'tickets__item',
        autoplay: {
            delay: 2500,
            disableOnInteraction: true,
        }
    })
}



export function courseDetailInit() {
    
}