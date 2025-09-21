export class Tabs {
    constructor({ btnsName, detailsName }) {
        this.btns = document.querySelectorAll(btnsName);
        this.details = document.querySelectorAll(detailsName);
        this.activeBtn = document.querySelector(`${btnsName}.active`);
        this.activeDetail = document.querySelector(`${detailsName}.open`);
        
        this.setEvents();
    }

    setEvents() {
        for (let btn of this.btns) {
            btn.addEventListener('click', this.btnClick.bind(this))
        }
    }

    btnClick(btn) {
        this.activeBtn.classList.remove('active')
        this.activeDetail.classList.remove('open')

        this.activeBtn = btn.target
        this.activeBtn.classList.add('active')

        this.activeDetail = [...this.details].find(
            el => el.dataset.info === btn.target.dataset.btn
        )
        this.activeDetail.classList.add('open')
    }
}