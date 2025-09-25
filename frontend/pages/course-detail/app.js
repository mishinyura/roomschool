import { marked } from '../../assets/libs/marked.esm.js'

import { timeFormatDuration, pluralize, loadData } from '../../assets/scripts/utils.js'
import { Header } from '../../assets/scripts/modules/Header.js'
import { Accordion } from '../../assets/scripts/components/Accordeon.js'
import { Tabs } from '../../assets/scripts/components/Tabs.js'
import { Reviews } from '../../assets/scripts/modules/Reviews.js'
import { CourseDetail } from '../../assets/scripts/modules/Course.js'

async function main() {
    const courseData = await loadData('../../data/course.json')
    console.log(courseData)

    const namePage = document.querySelector('meta[name="page"]').content

    const header = new Header('.header')

    const coursesSlider = new Swiper('.tabs__content', {
        direction: 'horizontal',
        loop: false,
        effect: 'coverflow',
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

    const course = new CourseDetail(courseData)
    course.build()
}

document.addEventListener("DOMContentLoaded", () => {
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