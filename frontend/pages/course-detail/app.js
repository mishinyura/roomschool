import { marked } from '../../assets/scripts/modules/marked.esm.js'

import { timeFormatDuration, pluralize } from '../../assets/scripts/utils.js'
import { Header } from '../../assets/scripts/components/Header.js'
import { Accordion } from '../../assets/scripts/components/Accordeon.js'
import { Tabs } from '../../assets/scripts/components/Tabs.js'

function main() {
    const namePage = document.querySelector('meta[name="page"]').content

    const header = new Header('.header')

    const planAccordeon = new Accordion({
        name: '.plan',
        btns: '.plan__topic',
        collapse: false
    })

    // const detailCourseTabs = new Tabs({
    //     btnsName: '.tabs__btn',
    //     detailsName: '.tabs__data'
    // })

    const coursesSlider = new Swiper('.tabs__content', {
        direction: 'horizontal',
        loop: false,
        effect: 'cube',
        resistanceRatio: 0,
        slidesPerView: 1,
        spaceBetween: 40,
        wrapperClass: 'tabs__wrapper',
        slideClass: 'tabs__data',
        allowTouchMove: false,
        cubeEffect: {
            shadow: false
        },
        pagination: {
            el: '.tabs__btns',
            clickable: true,
            renderBullet: function (index, className) {
                const labels = ['Описание', 'Преподаватель', 'План', 'Отзывы'];
                return `<button class="${className} tabs__btn">${labels[index]}</button>`;
            },
        }
    })

    
}

document.addEventListener("DOMContentLoaded", () => {
    let text = `### О курсе \nРазвитие эмоционального интеллекта (ЭИ) у&nbsp;детей&nbsp;&mdash; важная часть их&nbsp;общей компетентности. 
    Наша программа опирается на&nbsp;проверенные подходы SEL (социально-эмоциональное обучение) и&nbsp;ЭИ по&nbsp;Гоулману, 
    а&nbsp;также на&nbsp;методику RULER (Йельский университет). Курс разбит на&nbsp;короткие видеоролики (5&ndash;15&nbsp;минут) 
    с&nbsp;активными упражнениями и&nbsp;ролевыми играми. Как показывают исследования, театральные и&nbsp;игровые методы помогают 
    детям лучше осознавать и&nbsp;выражать чувства.\nНапример, Edutopia отмечает, что при театральной игре 
    (&laquo;Pass the Hello&raquo;), где ученики передают друг другу &laquo;привет&raquo; с&nbsp;разными эмоциями, дети быстрее 
    учатся вербализовать свои чувства.\n ### Что вы изучите? \nНаша программа базируется на&nbsp;пяти ключевых компетенциях SEL: самосознание, 
    самоуправление, социальное осознание, ответственное принятие решений и&nbsp;навыки общения, которые соответствуют пяти 
    компонентам&nbsp;ЭИ по&nbsp;Гоулману: самопознание, саморегуляция, мотивация, эмпатия и&nbsp;социальные навыки. Особое внимание 
    уделяется развитию эмпатии и&nbsp;коммуникации. Занятия включают ролевые и&nbsp;группово&#769;ые упражнения, позволяющие ученикам 
    практиковаться в&nbsp;выражении эмоций и&nbsp;понимании других. Такие интерактивные методы делают абстрактные навыки осязаемыми 
    и&nbsp;улучшают эмоциональное взаимодействие между сверстниками.\n ### Для кого курс? \nПрограмма делится на&nbsp;два уровня: начальный 
    (10&ndash;13&nbsp;лет) и&nbsp;продвинутый (14&ndash;17&nbsp;лет), чтобы постепенно усложнять материалы и&nbsp;задачи. Используются 
    и&nbsp;доказанные образовательные методики. Например, метод RULER (Йель) учит школьников распознавать, называть и&nbsp;управлять 
    эмоциями. Для этого применяются инструменты вроде &laquo;колеса эмоций&raquo; или &laquo;компаса настроения&raquo;, расширяющие 
    словарь чувств. Во&nbsp;всех уроках даются простые определения, разбор примеров и&nbsp;практические рекомендации.`
    let descr = document.querySelector('.description_md')
    const html = marked.parse(text);
    descr.innerHTML = html

    let hours = document.querySelectorAll('.hours-course')
    let testes = document.querySelectorAll('.testes-course')

    for (let hour of hours) {
        hour.innerText = timeFormatDuration(hour.innerText)
    }

    for (let test of testes) {
        test.innerText = pluralize(test.innerText, 'урок', 'урока', 'уроков')
    }

    

    main()
})