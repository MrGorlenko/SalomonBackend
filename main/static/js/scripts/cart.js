let modalBase = document.querySelector('#modal_base'),
callCartModal = document.querySelector('.header__basket'),
toggleCart = false,
closeModal = document.querySelector('#close')

let BasketCounter = document.querySelector('#basketCounter');

let callCart = () => {
  if (toggleCart) {
    modalBase.classList.add('d-flex')
    modalBase.classList.remove('d-none')
  } else {
    modalBase.classList.remove('d-flex')
    modalBase.classList.add('d-none')
  }
}

let bigArr = []

function removeItemOnce(arr, value) {
  var index = arr.indexOf(value);
  if (index > -1) {
    arr.splice(index, 1);
  }
  return arr;
}

let removingIndex , newArr;
callCartModal.onclick = () => {
  toggleCart = !toggleCart
  callCart()
  removingItem()

}

let removingItem = () => {
  let ItemsInBasket = document.querySelectorAll('#basketItems .basketItem .removeIcon')


  ItemsInBasket.forEach((button, index) => {
    button.onclick = () => {
      removingIndex = index
      console.log(removingIndex)
      cleanCart()
      overalPrice -= ~~bigArr[index][1]
      if (bigArr[index][5]>0){
        oldPriceVal -= ~~bigArr[index][5]
      } else {
        oldPriceVal -= ~~bigArr[index][1]
      }
      discount = ~~overalPrice - ~~oldPriceVal
      let newArr = bigArr.splice(removingIndex, 1)
      basketDrawing(bigArr)
      removingItem()

      
      overalPriceCurrent.innerHTML = overalPrice + ' руб.'
      overallPriceOld.innerHTML = oldPriceVal + ' руб.'
      discountPrice.innerHTML = discount + ' pуб.'
    }
  }) 

  //overalPrice 

}

closeModal.onclick = () => {
  toggleCart = !toggleCart
  callCart()
}


let buyButtons = document.querySelectorAll('.one-click-button')

let picSearch = document.querySelectorAll('.SaleGood__price');

let cleanCart = () => {
  basketItems.innerHTML = ''
}

let basketDrawing = (drawArr) => {
  for (let i = 0; i < drawArr.length; i++){
    let basketItem = document.createElement('div')
    basketItem.className = 'basketItem';

    let title = document.createElement('div'),
    span = document.createElement('span'),
    p = document.createElement('p');

    let pic = document.createElement('img');
    pic.setAttribute('src', drawArr[i][2])

    let counter = document.createElement('div'),
    minus = document.createElement('span'),
    number = document.createElement('span'),
    plus = document.createElement('span');

    minus.className = 'minus'
    number.className = 'number'
    plus.className = 'plus'

    minus.innerHTML = '-'
    number.innerHTML = '1'
    plus.innerHTML = '+'

    counter.classList.add('counter')
    counter.classList.add('counter_gold')
    counter.appendChild(minus)
    counter.appendChild(number)
    counter.appendChild(plus)


    title.className = 'title'
    span.innerText = drawArr[i][3]
    p.innerText = drawArr[i][0]
    title.appendChild(span)
    title.appendChild(p)

    let price = document.createElement('div')
    price.className = 'price'
    price.innerHTML = drawArr[i][1] + 'руб.'

    let removeIcon = document.createElement('img');
    removeIcon.className = 'removeIcon'
    removeIcon.setAttribute('src', drawArr[i][4])



    // FINISH
    basketItem.appendChild(pic)
    basketItem.appendChild(title)
    basketItem.appendChild(counter)
    basketItem.appendChild(price)
    basketItem.appendChild(removeIcon)

    basketItems.appendChild(basketItem)

   }
}

let overalPrice = 0,
oldPriceVal = 0,
discount = 0;
let basketItems = document.querySelector('#basketItems');
let overalPriceCurrent = document.querySelector('.overall .price .current'),
overallPriceOld = document.querySelector('.overall .price .old'),
discountPrice = document.querySelector('.overall .price .discount');

buyButtons.forEach((button) => {
  button.onclick = () =>{
    let arr = []

    alert('Товар добавлен в корзину')

    //console.log(event.target.parentNode.parentNode.querySelector('.SaleGood__about .SaleGood__base .buttonsWidget .active'))

    let title = event.target.parentNode.querySelector('.ttl').innerText,
    price = event.target.parentNode.querySelector('.pr').innerText,
    pic = event.target.parentNode.querySelector('.pic').innerText,
    cat = event.target.parentNode.querySelector('.cat').innerText,
    rem = event.target.parentNode.querySelector('.rem').innerText,
    oldPrice = event.target.parentNode.querySelector('.oldPr').innerText,
    height = event.target.parentNode.parentNode.querySelector('.SaleGood__about .SaleGood__base .buttonsWidget .active').innerHTML,
    size = event.target.parentNode.parentNode.querySelector('.SaleGood__about .SaleGood__base .selectWidget span').innerHTML;

    //console.log(size)

    arr.push(title)
    arr.push(price)
    arr.push(pic)
    arr.push(cat)
    arr.push(rem)
    arr.push(oldPrice)
    arr.push(height)
    arr.push(size)

   bigArr.push(arr)

   //console.log(bigArr)


   basketItems.innerHTML = ''
   basketDrawing(bigArr)


    overalPrice += ~~price
    if (oldPrice > 0){
      oldPriceVal += ~~oldPrice
    } else {
      oldPriceVal += ~~price
    }

    discount = ~~overalPrice - ~~oldPriceVal

   overalPriceCurrent.innerHTML = overalPrice + ' руб.'
   overallPriceOld.innerHTML = oldPriceVal + ' руб.'
   discountPrice.innerHTML = discount + ' pуб.'

   BasketCounter.innerHTML = bigArr.length
  }
})



// // // // // // 
let goodModalClose = document.querySelector('.goodModal_close'),
goodModal = document.querySelector('.goodModalWrapper'),
goodModalSlider = document.querySelector('.swiper-container8 .swiper-wrapper');

goodModalSlider.innerHTML = ''

document.querySelectorAll('.buttonBuy').forEach((button) => {
  button.onclick = () => {
    goodModal.classList.add('goodModalWrapper_on')
    goodModal.classList.remove('goodModalWrapper_off')
    goodModalSlider.innerHTML = ''

    let pics = event.target.parentNode.querySelectorAll('.pic'),
    cat = event.target.parentNode.querySelector('.cat').innerHTML,
    title = event.target.parentNode.querySelector('.ttl').innerHTML,
    price = event.target.parentNode.querySelector('.pr').innerHTML,
    rem = event.target.parentNode.querySelector('.rem').innerText,
    oldPrice = event.target.parentNode.querySelector('.oldPr').innerHTML,
    description = event.target.parentNode.querySelector('.description'),
    characters = event.target.parentNode.querySelector('.characters'),
    feedbacks = event.target.parentNode.querySelector('.feedbacks');

    console.log(description)

    document.querySelector('#GoodModalCat').innerHTML = cat
    document.querySelector('#GoodModalTitle').innerHTML = title

    document.querySelector('.ModalGoodPrice .current').innerHTML = price + ' руб.'
    document.querySelector('.ModalGoodPrice .old').innerHTML = oldPrice + ' руб.'

    document.querySelector('#baseChars').innerHTML = description.innerHTML

    for (let i = 0; i<pics.length; i++){
      let SwiperSlide = document.createElement('div');
      SwiperSlide.className = 'swiper-slide'
      SwiperSlide.style.backgroundImage = `url(${pics[i].innerHTML}) `
      goodModalSlider.appendChild(SwiperSlide)
    }

    let swiper8 = new Swiper('.swiper-container8', {
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

    buttonsItemsSwitcher = document.querySelectorAll('#ItemCharsSwitcher button');
    switchButtons(buttonsItemsSwitcher, 'act')

    buttonsItemsSwitcher.forEach((button, index) => {
      button.onclick = () => {
        console.log(index)
        switch (index) {
          case 0: {
            document.querySelector('#baseChars').innerHTML = description.innerHTML
            break
          } 
          case 1: {
            document.querySelector('#baseChars').innerHTML = characters.innerHTML
            break
          }
          case 2: {
            document.querySelector('#baseChars').innerHTML = feedbacks.innerHTML
            break
          }
        }
      }
    })

    document.querySelector('#ModalGoodBuy').onclick = () => {

      let arr = []

      alert('Товар добавлен в корзину')
      arr.push(title)
      arr.push(price)
      arr.push(pics[0].innerHTML)
      arr.push(cat)
      arr.push(rem)
      arr.push(oldPrice)

      bigArr.push(arr)
      basketItems.innerHTML = ''
      basketDrawing(bigArr)

      console.log(bigArr)

      overalPrice += ~~price
      if (oldPrice > 0){
        oldPriceVal += ~~oldPrice
      } else {
        oldPriceVal += ~~price
      }
  
      discount = ~~overalPrice - ~~oldPriceVal
  
     overalPriceCurrent.innerHTML = overalPrice + ' руб.'
     overallPriceOld.innerHTML = oldPriceVal + ' руб.'
     discountPrice.innerHTML = discount + ' pуб.'

     BasketCounter.innerHTML = bigArr.length
     document.querySelector('.goodModalWrapper').classList.remove('goodModalWrapper_on')
     document.querySelector('.goodModalWrapper').classList.add('goodModalWrapper_off')
    }

  }
})


goodModalClose.onclick = () => {
  document.querySelector('.goodModalWrapper').classList.remove('goodModalWrapper_on')
  document.querySelector('.goodModalWrapper').classList.add('goodModalWrapper_off')
}

let switchButtons = function(btns, activeClass){
  btns.forEach(function(element, index){
    element.addEventListener('click', function(index){
      btns.forEach(function(element, i){
        element.classList.remove(activeClass)
      })
      element.classList.add(activeClass)
    })
  })
};

let heightButtons = document.querySelectorAll('.buttonsWidget')



heightButtons.forEach((btns, index) => {
    btns.children[0].className = 'active'
    btns.onclick = () => {
      for (let i = 0; i<btns.children.length; i++) {
        if (btns.children[i].className == 'active'){
          btns.children[i].className = ''
        } else {
          btns.children[i].className = 'active'
        }
      }
    }
})