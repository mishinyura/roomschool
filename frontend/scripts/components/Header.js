export class Header {
    constructor(objName) {
        this.header = document.querySelector(objName);
        this.burger = this.header.querySelector('#burger');
        this.menu = this.header.querySelector(`${objName}__menu`)
        this.setEvents();
    }

    setEvents() {
        this.burger.addEventListener("click", this.toggleMenu.bind(this));
        window.addEventListener("scroll", this.onScroll.bind(this));
    }

    toggleMenu() {
        this.menu.classList.toggle("active");
        this.burger.classList.toggle("open");
        document.body.classList.toggle("lock"); // чтобы не скроллился фон
    }

    onScroll() {
        if (window.scrollY > 50) {
        this.header.classList.add("scrolled");
        } else {
        this.header.classList.remove("scrolled");
        }
    }
}