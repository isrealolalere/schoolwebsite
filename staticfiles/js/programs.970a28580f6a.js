const slides = document.querySelectorAll('.slide')

var counter = 0;
slides.forEach(
    (slide, index) => {
        slide.style.left = `${index * 100}%`
    }
)

const goPrev = () => {
    //loop back to the last slide at the first slide
    if (counter === 0){
        counter = slides.length - 1;
    } else {
        counter--;
    }
    slideImage()
}

const goNext = () => {
    counter++;

    //loop back to the first slide at the last slide
    if (counter === slides.length){
        counter = 0;
    }
    slideImage();
}


// slide images with 6 seconds interval
setInterval(() => {
    goNext();
}, 6000);



const slideImage = () => {
    slides.forEach(
        (slide) => {
            slide.style.transform = `translateX(-${counter * 100}%)`
        }
    )
}