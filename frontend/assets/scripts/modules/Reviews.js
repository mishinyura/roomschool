export class Reviews {
    constructor(obj) {
        this.author = this._createAuthor(obj.author);
        this.comment = this._createComment(obj.comment);
        this.rating = this._createRating(obj.rating);
        this.date = this._createDate(obj.created_at);
        this.evaluated = this._createEval(obj.evaluated);
        this.element = this._createContainer();
    }

    _createElement(tagName, className) {
        let elem = document.createElement(tagName)
        elem.className = className

        return elem
    }

    _createContainer() {
        let element = this._createElement('div', 'reviews__item')
        
        return element
    }

    _createDate(date) {
        let element = this._createElement('span', 'reviews__date')
        element.innerText = date

        return element
    }

    _createAuthor(author) {
        let element = this._createElement('h4', 'reviews__author')
        element.innerText = author

        return element
    }

    _createComment(comment) {
        let element = this._createElement('p', 'reviews__comment')
        element.innerText = comment

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

    _createEval(evaluated) {
        let element = this._createElement('h5', 'reviews__eval')
        element.innerText = evaluated

        return element
    }

    buildReview() {
        const list = document.querySelector('.reviews__list')
        this.element.append(
            this.date,
            this.author,
            this.evaluated,
            this.rating,
            this.comment
        )
        list.appendChild(this.element)
    }
}