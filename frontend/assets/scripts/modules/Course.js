import { marked } from '../../libs/marked.esm.js'

import { timeFormatDuration } from '../utils.js';
import { Accordion } from '../components/Accordeon.js';
import { Reviews } from './Reviews.js';

export class CourseCard {
    _render() {

    }
}

export class CourseDetail {
    constructor(obj) {
        this.title = obj.name;
        this.slug = obj.slug;
        this.shortDescription = obj.description.short
        this.mainDescription = obj.description.main
        this.fullDescription = obj.description.full
        this.image = obj.image
        this.price = obj.price
        this.discount = obj.discount
        this.amountLessons = obj.amount_video
        this.duration = obj.duration
        this.rating = obj.rating
        this.modules = obj.modules
        this.teachers = obj.teachers
        this.reviews = obj.reviews
        this.prerequisite_sub = obj.prerequisite_subjects
    }

    _createElement(tagName, className=null, text=null, ...attrs) {
        let element = document.createElement(tagName)

        if (className) {
            element.className = className
        }

        if (text) {
            element.innerText = text
        }

        if (attrs) {
            for (let attr of attrs) {
                console.log(attr)
            }
        }

        return element
    }

    renderHead(parentName='.courses__wrapper') {
        const parent = document.querySelector(parentName)
        const textBlock = this._createElement('div', 'courses__content')
        const title = this._createElement('h1', 'courses__title', this.title)
        const descr = this._createElement('p', 'courses__description', this.mainDescription)
        const videos = this._createElement('span', 'courses__videos videos-course', this.amountLessons)
        const hours = this._createElement('span', 'courses__hours hours-course', timeFormatDuration(this.duration))
        const rating = this._createElement('span', 'courses__rating rating-course', this.rating)
        const image = this._createElement('div', 'courses__image')
        const img = this._createElement('img')
        img.setAttribute('src', `../../assets/media/images${this.image}`)

        textBlock.append(title, descr, videos, hours, rating)
        image.appendChild(img)
        parent.append(textBlock, image)
    }

    renderDescription(parentName='.description_md') {
        const parent = document.querySelector(parentName)
        const html = marked.parse(this.fullDescription);
        parent.innerHTML = html
    }

    renderTeachers(parentName='.teachers') {
        const parent = document.querySelector(parentName)
        let container, image, info;
        let img, name, role, post, rating, description;

        for (let teacher of this.teachers) {
            ({ name, role, post, rating, description } = teacher)
            container = this._createElement('div', 'teachers__item')
            image = this._createElement('div', 'teachers__image')
            info = this._createElement('div', 'teachers__info')

            img = this._createElement('img')
            role = this._createElement('span', 'teachers__role', role)
            name = this._createElement('h3', 'teachers__name', name)
            post = this._createElement('p', 'teachers__post', post)
            description = this._createElement('p', 'teachers__description', description)
            rating = this._createElement('span', 'teachers__rating rating-course', rating)

            image.appendChild(img)
            info.append(role, name, post, description, rating)
            container.append(image, info)
            parent.appendChild(container)
        }
    }

    renderPlan(parentName='.plan') {
        const parent = document.querySelector(parentName)
        let module, topic, title, descr, videos, testes;
        let detail, item, name, type, time
        let amountVideo, amountTests;

        for (let mod of this.modules) {
            module = this._createElement('div', 'plan__module')
            topic = this._createElement('div', 'plan__topic')
            title = this._createElement('h4', 'plan__title', mod.title)
            descr = this._createElement('p', 'plan__description', mod.description)
            detail = this._createElement('ul', 'plan__detail')
            amountVideo = 0
            amountTests = 0

            for (let less of mod.lessons) {
                item = this._createElement('li', 'plan__item')
                name = this._createElement('span', 'plan__name', less.title)
                type = this._createElement('span', 'plan__type', less.type)
                time = this._createElement('span', 'plan__time hours-course', timeFormatDuration(less.duration))

                if (less.type == 'video') {
                    amountVideo++
                    item.classList.add('plan__item_video')
                } else if (less.type == 'test') {
                    amountTests++
                    item.classList.add('plan__item_work')
                }

                item.append(name, type, time)
                detail.appendChild(item)
            }

            topic.append(title, descr)

            if (amountVideo) {
                videos = this._createElement('span', 'plan__counter videos-course', amountVideo)
                topic.appendChild(videos)
            }
            if (amountTests) {
                testes = this._createElement('span', 'plan__counter testes-course', amountTests)
                topic.appendChild(testes)
            }

            module.append(topic, detail)

            parent.appendChild(module)

        }

        const planAccordeon = new Accordion({
            name: '.plan',
            btns: '.plan__topic',
            collapse: false
        })
    }

    renderReviews(parentName='.reviews') {
        const parent = document.querySelector(parentName)

        for (let rev of this.reviews) {
            new Reviews(rev).buildReview()
        }
    }

    renderControl(parentName='.course') {
        const parent = document.querySelector(parentName)
        const btns = document.querySelector('.course__control')
        const conditions = document.querySelector('.course__conditions')
        const info = this._createElement('div', 'course__info')
        let tempPrice;
        
        if (this.discount != 0) {
            tempPrice = this.price - this.price * this.discount / 100
            const discount = this._createElement('span', 'course__discount', this.discount)
            const oldPrice = this._createElement('span', 'course__price course__price_old', this.price)
            const newPrice = this._createElement('span', 'course__price course__price_new', tempPrice)
            info.append(oldPrice, newPrice, discount)

        } else {
            newPrice = this._createElement('span', 'course__price course__price_new', this.price)
        }

        parent.insertBefore(info, btns)

        if (this.prerequisite_sub.length != 0) {
            const recommendation = this._createElement('div', 'course__recommendations')
            const rec_title = this._createElement('span', 'course__title', 'Рекомендуем пройти до начала курса:')
            const list = this._createElement('ul', 'course__list')
            let item, link;

            for (let obj of this.prerequisite_sub) {
                item = this._createElement('li', 'course__recommendation')
                link = this._createElement('a', 'course__link', obj.name)
                link.setAttribute('href', `/courses/${obj.slug}`)
                item.appendChild(link)
                list.appendChild(item)
            }

            recommendation.append(rec_title, list)
            parent.insertBefore(recommendation, conditions)
        }

    }

    build() {
        this.renderHead()
        this.renderDescription()
        this.renderTeachers()
        this.renderPlan()
        this.renderReviews()
        this.renderControl()
    }
}

export class Courses{
    constructor(obj){
        this.course = this._createElement('article', 'course__item')
        this.title = this._createTitle(obj.title);
        this.slug = obj.slug;
        this.shortDescription = obj.descriptions.short
        this.mainDescription = obj.descriptions.main
        this.fullDescription = obj.descriptions.full
        this.price = obj.price
        this.discount = obj.discount
        this.modules = obj.modules
    }

    generateCard(parentName) {
        let parent = document.querySelector(parentName)

        
    }

    generateDetail() {

    }

    _createElement(tagName, className) {
        let element = document.createElement(tagName)
        element.className = className

        return element
    }

    _createTitle(title){
        let element = this._createElement('h3', 'course__title')
        let link = this._createElement('a', 'course__link')
        link.href = `/courses/${this.slug}`
        link.innerText = title
        element.appendChild(link)

        return element
    }

    _createDescription(description) {
        let element = this._createElement('p', 'course__description')
        element.innerText = description

        return element
    }

    _createTeacher(name) {
        let element = this._createElement('span', 'course__teacher')
        element.innerText = name

        return element
    }

    _createRating(rating) {
        let element = this._createElement('div', 'reviews__rating')
        let star;
        for (let i = 0; 5 > i; ++i) {
            if (i <= rating) {
                star = this._createElement('span', 'reviews__star reviews__star_yellow')
            } else {
                star = this._createElement('span', 'reviews__star reviews__star_white')
            }
            
            element.appendChild(star)
        }

        return element
    }


}