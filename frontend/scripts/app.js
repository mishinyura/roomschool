import { indexInit } from './initializer.js';

// function showPresentText(footerElement){
//     const observer = new IntersectionObserver(entries => {
//     entries.forEach(entry => {
//         let ratio = Math.min(1, Math.max(0, entry.intersectionRatio));
//         footerElement.style.setProperty('--opacity-footer-after-before', ratio.toFixed(2));
//         if (ratio != 0) {
//             footerElement.style.setProperty('--visibility-footer-arter-before', 'visible')
//         } else {
//             footerElement.style.setProperty('--visibility-footer-arter-before', 'hidden')
//         }
//     });
//     }, {
//         threshold: Array.from({ length: 101 }, (_, i) => i / 100)
//     });

//     observer.observe(footerElement);
// };

// function editViewTabs(courses, text) {
//     for (let course of courses) {
//         course.addEventListener('mouseover', (elem) => {
//             let parent = elem.target.closest(`.${course.classList[0]}`)
//             let courseName = parent.dataset.course
//             for (let txt of text) {
//                 txt.classList.remove('show')
//                 if (txt.dataset.course === courseName) {
//                     txt.classList.add('show')
//                 }
//             };
//         })
//     }
// }

// function editViewBurger(burger) {
//     console.log(burger)
//     burger.addEventListener('click', () => {
//         burger.classList.toggle('open')
//     })
// }





function main() {
    // let footer = document.querySelector('.footer');
    // let coursesCard = document.querySelectorAll('.services__course');
    // let coursesText = document.querySelectorAll('.services__text');
    // let burgerParent = document.querySelector('.panel__item_burger');
    // let burgerBtn = burgerParent.querySelector('button');
    // let linksMenu = document.querySelectorAll('.topmenu__link');
    // let loginBtn = document.querySelector('.auth__bth_login');


    // showPresentText(footer)
    // editViewTabs(coursesCard, coursesText)
    // editViewBurger(burgerBtn)
    // editViewLogin(loginBtn)


    const namePage = document.querySelector('meta[name="page"]').content

    switch (namePage) {
        case 'index':
            indexInit()
            break;
    }
}

document.addEventListener("DOMContentLoaded", () => {
    main()
})