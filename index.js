class MovingAverage {
    constructor() {
        // initializing an emplty array as 'elements'
        this.elements = [];
    }
    getElements() {
        // this method will return the elements array
        return this.elements;
    }
    addElement(element) {
        /* this function will check if the element is a number then add to elements array 
        else give error as it is not a number */
        if (typeof element === 'number') {
            this.elements.push(element);
        }
        else {
            throw new Error('element is not a number');
        }
    }
    getMovingAverage(n) {
        // this function calculates the moving average of the 
        if (n > this.elements.length) {
            throw new Error('n is greater than the number of elements');
        }
        let sum = 0;
        for (let i = 0; i < n; i++) {
            sum += this.elements[this.elements.length - 1 - i];
        }
        return sum / n;
    }
}
// here we create a handler 'a' to access the MovingAverage() function and properties by using the 'new' keyword
const a = new MovingAverage();

// push 10 random numbers between 0 to 10
for (let i = 0; i < 10; i++) {
    a.addElement(Math.floor(Math.random() * 10));
}

// we will see the rando elements in the console that were added to elements array
console.log(a.getElements());

// we are setting 3 to get an average of the last 3 elemnets in the array
console.log(a.getMovingAverage(3));