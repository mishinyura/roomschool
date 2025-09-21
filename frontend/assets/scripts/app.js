import { indexInit, courseDetailInit } from './initializer.js';

function main() {
    const namePage = document.querySelector('meta[name="page"]').content

    switch (namePage) {
        case 'index':
            indexInit()
            break;
        case 'course-detail':
            courseDetailInit()
            break;
    }
}

document.addEventListener("DOMContentLoaded", () => {
    main()
})