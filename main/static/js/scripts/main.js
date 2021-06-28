let switchButtons = function(btns, activeClass){
  btns.forEach(function(element, index){
    element.addEventListener('click', function(index){
      btns.forEach(function(element){
        element.classList.remove(activeClass)
      })
      element.classList.add(activeClass)
    })
  })
};


let catalogMain = document.querySelectorAll('#catalogMain button'),
catalogMainMobile = document.querySelectorAll('#catalogMainMobile button');
let buttonsWidget1 = document.querySelectorAll('#buttonsWidget1 button'),
buttonsWidget2 = document.querySelectorAll('#buttonsWidget2 button'),
buttonsWidget3 = document.querySelectorAll('#buttonsWidget3 button'),
buttonsItemsSwitcher = document.querySelectorAll('#ItemCharsSwitcher button');

switchButtons(catalogMain, 'toggle-button-active')
switchButtons(catalogMainMobile, 'toggle-button-active')
switchButtons(buttonsWidget1, 'active')
switchButtons(buttonsWidget2, 'active')
switchButtons(buttonsWidget3, 'active')
switchButtons(buttonsItemsSwitcher, 'act')

let sections = document.querySelectorAll('.section');

let burger = document.getElementById('burger'),
 burgerToggle = document.getElementById('burger-toggle'),
 burgerClose = document.getElementById('burger-close'),
 burgerMenus = document.querySelectorAll('.burger .firstLvl .first');

burgerClose.addEventListener('click', () => {
  burger.classList.add('burger__off');
  burger.classList.remove('burger__on');
  sections.forEach((section) => {
    section.classList.add('d-block');
    section.classList.remove('d-none');
  })
})

burgerToggle.addEventListener('click', () => {
  sections.forEach((section) => {
    setTimeout(()=> {
      section.classList.add('d-none');
      section.classList.remove('d-block');
    }, 400)
    
  })
  burger.classList.add('burger__on');
  burger.classList.remove('burger__off');
})

burgerMenus.forEach(function(elem){
  elem.addEventListener('click', function(e){
    if (elem.classList.contains('on')){
      elem.classList.remove('on')
      elem.classList.add('off')
      elem.children[1].classList.add('secondLvlOff')
      elem.children[1].classList.remove('secondLvlOn')
    } else {
      elem.classList.remove('off')
      elem.classList.add('on')
      elem.children[1].classList.add('secondLvlOn')
      elem.children[1].classList.remove('secondLvlOff')
    }
  })
})


const ItemsCharacters = {
  'Descriptions' : {
    'topHeader' : 'Прекрасен во всех отношениях',
    'firstPar'  : 'Новый дисплей Liquid Retina — наш самый продвинутый ЖК‑дисплей. Ещё более быстрый Face ID. Самый мощный и умный процессор iPhone. И потрясающая камера. iPhone XR — воплощение красоты и интеллекта. Всё внимание на дисплей Liquid Retina. Новый дисплей iPhone XR — самый продвинутый ЖК‑дисплей iPhone. Инновационные технологии подсветки позволили нам создать дисплей, закруглённый по углам и занимающий всю переднюю панель. Теперь реалистичные цвета заполняют её целиком.',
    'bottomHeader' : 'Исключительное качество материалов.',
    'secondPar' : 'Особо прочная передняя панель из стекла. Плотно подогнанная рамка из алюминия, применяющегося в аэрокосмической отрасли. Защита от воды и пыли. И шесть великолепных цветов. Семь слоёв цвета. Передовые технологии позволили добиться невероятно глубокого, насыщенного цвета задней панели из стекла. Алюминиевая рамка аэрокосмического уровня. Анодированная рамка корпуса из особого сплава, разработанного Apple, идеально сочетается с цветом задней панели.'
  },
  'Chars' : {
    '1' : 'Характеристики'
  },
  'Feedbacks' : {
    '1' : 'feedback',
    '2' : 'feedback2',
    '3' : 'feedback3'
  }
}


let baseChars = document.getElementById('baseChars');
let buttonIndex = null;
let showDescr = () => {
  baseChars.appendChild(document.createElement('h1'))
  baseChars.appendChild(document.createElement('p'))
  baseChars.appendChild(document.createElement('h1'))
  baseChars.appendChild(document.createElement('p'))
  baseChars.children[0].innerHTML = ItemsCharacters.Descriptions.topHeader
  baseChars.children[1].innerHTML = ItemsCharacters.Descriptions.firstPar
  baseChars.children[2].innerHTML = ItemsCharacters.Descriptions.bottomHeader
  baseChars.children[3].innerHTML = ItemsCharacters.Descriptions.secondPar
}, 
showChars = () => {
  baseChars.appendChild(document.createElement('p'))
  baseChars.children[0].innerHTML = ItemsCharacters.Chars[1]
}, 
showFeedbacks = () => {
  baseChars.appendChild(document.createElement('h1'))
  baseChars.appendChild(document.createElement('p'))
  baseChars.appendChild(document.createElement('h1'))
  baseChars.appendChild(document.createElement('p'))
  baseChars.appendChild(document.createElement('h1'))
  baseChars.appendChild(document.createElement('p'))
  baseChars.children[0].innerHTML = ItemsCharacters.Feedbacks[1]
  baseChars.children[1].innerHTML = ItemsCharacters.Feedbacks[1]
  baseChars.children[2].innerHTML = ItemsCharacters.Feedbacks[2]
  baseChars.children[3].innerHTML = ItemsCharacters.Feedbacks[2]
  baseChars.children[4].innerHTML = ItemsCharacters.Feedbacks[3]
  baseChars.children[5].innerHTML = ItemsCharacters.Feedbacks[3]
};

let cleanInfo = () => {
  while (baseChars.children[0]){
    baseChars.children[0].parentNode.removeChild(baseChars.children[0])
  }
},
charactersMinHeight = () => {
  document.getElementById('ItemCharacters').style.minHeight = baseChars.offsetHeight + document.getElementById('btnDescr').offsetHeight + document.getElementById('btnChar').offsetHeight + document.getElementById('btnFeedbacks').offsetHeight + 40 + 'px'
},
descrUp = () => {
  baseChars.style.top = document.getElementById('btnDescr').offsetHeight - 2 + 'px'
  document.getElementById('btnChar').style.top = baseChars.offsetHeight + document.getElementById('btnDescr').offsetHeight + 10 + 'px'
  document.getElementById('btnFeedbacks').style.top = baseChars.offsetHeight + document.getElementById('btnDescr').offsetHeight + document.getElementById('btnChar').offsetHeight + 20 + 'px'
},
charsUp = () => {
  baseChars.style.top = document.getElementById('btnDescr').offsetHeight + document.getElementById('btnChar').offsetHeight + 8 + 'px'
  document.getElementById('btnChar').style.top = document.getElementById('btnDescr').offsetHeight + 10 + 'px';
  document.getElementById('btnFeedbacks').style.top =  document.getElementById('btnDescr').offsetHeight + document.getElementById('btnChar').offsetHeight + baseChars.offsetHeight + 20 + 'px'
},
feedbacksUp = () => {
  document.getElementById('btnChar').style.top = (document.getElementById('btnDescr').offsetHeight * 1) + 10 + 'px'
  document.getElementById('btnFeedbacks').style.top = (document.getElementById('btnDescr').offsetHeight * 2) + 20 + 'px'
  baseChars.style.top = (document.getElementById('btnDescr').offsetHeight * 3) + 18 + 'px'
  
}
;

showDescr();

if (window.screen.width <= 992){
  descrUp()
  charactersMinHeight()
}

buttonsItemsSwitcher.forEach((element, index) => {
  element.addEventListener('click', (elem, i) => {
    cleanInfo();
    buttonIndex = index;
    console.log(buttonIndex)
    if (buttonIndex == 0) {
      showDescr()
      descrUp()
      charactersMinHeight()
    } else if (buttonIndex == 1) {
      showChars()
      charsUp()
      charactersMinHeight()
    } else if (buttonIndex == 2) {
      showFeedbacks()
      feedbacksUp()
      charactersMinHeight()
    }
  })

})

// const baseChars = document.getElementById('baseChars')
console.log(baseChars.offsetHeight)

setTimeout(1000, console.log(baseChars.offsetHeight))