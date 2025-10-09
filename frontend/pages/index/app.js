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

    // const selectCallback = new Select({
    //     obj: '.callback__select',
    // })

    // const header = new Header('.header')

    const header = new Header({
        elements: {
            header: ".header",
            burger: "#burger",
            searchBtn: ".panel__btn_search",
            searchInput: ".panel__form",
            chatBtn: ".header__chat-btn",
        },

        handlers: {
            header: {
                target: 'window',
                event: "scroll",
                callback() {
                    this.onScroll();
                }
            },
            burger: {
                event: "click",
                callback() {
                    this.toggleMenu();
                },
            },
            searchBtn: {
                event: "click",
                callback() {
                    this.toggleSearch();
                },
            },
            searchInput: {
                event: "input",
                callback(e) {
                    this.searchData();
                },
            },
            chatBtn: {
                event: "click",
                callback() {
                    this.handleChat();
                },
            },
        },
    });

    const coursesSlider = new Swiper('.reviews__slider', {
        direction: 'horizontal',
        loop: true,
        speed: 400,
        spaceBetween: 40,
        slidesPerView: 1,
        effect: 'cube',
        // centeredSlides: true,

        wrapperClass: 'reviews__wrapper',
        slideClass: 'reviews__slide',
        pagination: {
            el: '.swiper-pagination',
        },

        // Navigation arrows
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        }
        // autoplay: {
        //     delay: 2500,
        //     disableOnInteraction: true,
        // },
    })

    // particlesJS.load('particles-js', '../../assets/libs/particles/particles.json', function () {
    //     console.log('callback - particles.js config loaded');
    // });

}

document.addEventListener("DOMContentLoaded", () => {
    main()
})