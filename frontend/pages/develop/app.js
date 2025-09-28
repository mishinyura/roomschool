import { Select } from '../../assets/scripts/components/Select.js'
import { Header } from '../../assets/scripts/modules/Header.js'

function main() {
    const header = new Header('.header')

    const sortedSelect = new Select({
        obj: '.filters__select',
        input: '.filters__wrapper',
        options: '.filters__sort'
    })
}

document.addEventListener("DOMContentLoaded", () => {
    main()
})