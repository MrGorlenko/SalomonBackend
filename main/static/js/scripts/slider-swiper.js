const swiper = new Swiper('.swiper-container', {
  loop: true,

  pagination : {
    el : '.custom-pagination',
    bulletClass: 'pagination-regular',
    bulletActiveClass: 'pagination-active',
    clickable: true,
    type: 'bullets',

  },

  navigation: {
    nextEl: '.slider__arrows .next',
    prevEl: '.slider__arrows .prev',
  },

});

const swiper2 = new Swiper('.swiper-container2', {
  centeredSlides: true,
  pagination: {
    el : '.custom-pagination2',
    bulletClass: 'pagination-regular2',
    bulletActiveClass: 'pagination-active2',
    type: 'bullets',
    clickable: true,
  },
  initialSlide: 1
})

const swiper3 = new Swiper('.swiper-container3', {
  effect: 'fade',
  fadeEffect: {
    crossFade: true
  },
  navigation: {
    nextEl: '.custom-arrow3 .next',
    prevEl: '.custom-arrow3 .prev'
  },
  pagination: {
    el : '.custom-pagination3',
    bulletClass: 'pagination-regular3',
    bulletActiveClass: 'pagination-active2',
  }
})

const swiper4 = new Swiper('.swiper-container4', {
  centeredSlides: true,
  pagination: {
    el : '.custom-pagination4',
    bulletClass: 'pagination-regular2',
    bulletActiveClass: 'pagination-active2',
    type: 'bullets',
    clickable: true,
  },
  initialSlide: 1
})

const swiper5 = new Swiper('.swiper-container5', {
  slidesPerView: 1,
  slidesOffsetAfter: 2,
  spaceBetween: 31,
  navigation: {
    nextEl: '.custom-arrow3 .next',
    prevEl: '.custom-arrow3 .prev'
  },

  breakpoints: {
    992 : {
      slidesPerView: 4
    }
  }

})

const swiper6 = new Swiper('.swiper-container6', {
  slidesPerView: 1,
  spaceBetween: 32,
  navigation: {
    nextEl: '.custom-arrow3 .next',
    prevEl: '.custom-arrow3 .prev'
  },
  breakpoints : {
    992 : {
      slidesPerView: 3
    }
  }
})

const swiper7 = new Swiper('.swiper-container7', {
  slidesPerView: 1,
  spaceBetween: 30,
  width: 171,
  navigation: {
    nextEl: '.custom-arrow3 .next',
    prevEl: '.custom-arrow3 .prev'
  },
})

const swiper8 = new Swiper('.swiper-container8', {
  pagination : {
    el : '.custom-pagination',
    bulletClass: 'pagination-regular',
    bulletActiveClass: 'pagination-active',
    clickable: true,
    type: 'bullets',
  },
  navigation: {
    nextEl: '.slider__arrow .next',
    prevEl: '.slider__arrow .prev'
  }
})

const swiper9 = new Swiper('.swiper-container9', {
  navigation: {
    nextEl: '.slider__arrow .next',
    prevEl: '.slider__arrow .prev'
  },
  slidesPerView: 1,
  pagination: {
    el : '.custom-pagination',
    bulletClass: 'pagination-regular',
    bulletActiveClass: 'pagination-active',
    clickable: true,
    type: 'bullets',
  }
})