function showPresentText(footerElement){
    const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        let ratio = Math.min(1, Math.max(0, entry.intersectionRatio));
        footerElement.style.setProperty('--opacity-footer-after-before', ratio.toFixed(2));
        if (ratio != 0) {
            footerElement.style.setProperty('--visibility-footer-arter-before', 'visible')
        } else {
            footerElement.style.setProperty('--visibility-footer-arter-before', 'hidden')
        }
    });
    }, {
        threshold: Array.from({ length: 101 }, (_, i) => i / 100)
    });

    observer.observe(footerElement);
};

function editViewTabs(courses, text) {
    for (let course of courses) {
        course.addEventListener('mouseover', (elem) => {
            let parent = elem.target.closest(`.${course.classList[0]}`)
            let courseName = parent.dataset.course
            for (let txt of text) {
                txt.classList.remove('show')
                if (txt.dataset.course === courseName) {
                    txt.classList.add('show')
                }
            };
        })
    }
}

function editViewBurger(burger) {
    console.log(burger)
    burger.addEventListener('click', () => {
        burger.classList.toggle('open')
    })
}

function request(){
    return ['admin', 'employee', 'parent']
}


function editViewLogin(btn) {
    let form = btn.closest('form')
    btn.addEventListener('click', () => {
        //Отправляем данные на сервер, 
        //чтобы получить разрешение, 
        //если сервер возвращает список,
        //формируем список доступных аккаунтов и даем выбор
        let response = request()
        form = new FormData(form)
        console.log(form)
        if (response.length > 1) {
            let accountsContainer = document.querySelector('.choise');
            let authContainer = document.querySelector('.auth');
            let accounts = accountsContainer.querySelectorAll('.choise__item');
            for (let acc of accounts) {
                if (response.includes(acc.dataset.account)) {
                    acc.classList.add('active')
                }
            }
            accountsContainer.classList.add('active')
            authContainer.classList.remove('active')
        } else {
            //если аккаунт 1, то редиректим сразу на него
            console.log('Redirect on profile')
        }
    })
}

function main() {
    // let footer = document.querySelector('.footer');
    // let coursesCard = document.querySelectorAll('.services__course');
    // let coursesText = document.querySelectorAll('.services__text');
    // let burgerParent = document.querySelector('.panel__item_burger');
    // let burgerBtn = burgerParent.querySelector('button');
    // let linksMenu = document.querySelectorAll('.topmenu__link');
    let loginBtn = document.querySelector('.auth__bth_login');


    // showPresentText(footer)
    // editViewTabs(coursesCard, coursesText)
    // editViewBurger(burgerBtn)
    // editViewSubmenu(linksMenu)
    editViewLogin(loginBtn)
}

main()