/**
 * @module initializer
 * @description Модуль хранит в себе функции с инициализацией
 * страниц. Каждая функция относится к одной странице и вызывается
 * при загрузке DOM.
 */

import { InputMask } from './components/InputMask.js'
import { Form } from './components/Form.js'
import { Select } from './components/Select.js'

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
}