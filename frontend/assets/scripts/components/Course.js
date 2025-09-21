export class Course{
    constructor(obj){
        this.title = obj.title;
        this.shortDescription = obj.descriptions.short
        this.mainDescription = obj.descriptions.main
        this.fullDescription = obj.descriptions.full
        this.oldPrice = obj.price.old
        this.newPrice = obj.price.new
        this.plan = obj.plan
    }
}