import { InputMask } from '../../assets/scripts/components/InputMask.js'
import { Form } from '../../assets/scripts/components/Form.js'
import { Select } from '../../assets/scripts/components/Select.js'
import { Header } from '../../assets/scripts/modules/Header.js'

function main() {
    const namePage = document.querySelector('meta[name="page"]').content

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
        spaceBetween:  40,
        wrapperClass: 'tickets__wrapper',
        slideClass: 'tickets__item',
        autoplay: {
            delay: 2500,
            disableOnInteraction: true,
        },
        breakpoints: {
            320: {
                slidesPerView: 1
            },
            992: {
                slidesPerView: 2
    
            },
            1200: {
                slidesPerView: 3
            }
        }
    })
}

document.addEventListener("DOMContentLoaded", () => {
    main()
})