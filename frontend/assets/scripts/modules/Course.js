class CourseBuilder {
    createCard() {

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
        this.lessons = obj.lessons
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