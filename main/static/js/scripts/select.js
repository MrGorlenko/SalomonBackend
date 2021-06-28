
class Select {
  constructor( element, state ) {
    this.element = element;
    this.state = state;
  }

  changeState() {
    this.state = !this.state
    if (this.state) {
      this.element.classList.add('selected')
      this.element.children[1].className = 'active'
    } else {
      this.element.classList.remove('selected')
      this.element.children[1].className = 'unactive'
    }
  }

  selectOption(option) {
    this.option = option
    this.element.children[0].innerHTML = option
  }
}

class CharacterSwitcher {
  constructor(element){
    this.element = element
  }
}


select1 = new Select(document.querySelector('.select1'), false)
select2 = new Select(document.querySelector('.select2'), false)
select3 = new Select(document.querySelector('.select3'), false)
select4 = new Select(document.querySelector('.select4'), false)
select5 = new Select(document.querySelector('.select5'), false)
select6 = new Select(document.querySelector('.select6'), false)
select7 = new Select(document.querySelector('.select7'), false)
select8 = new Select(document.querySelector('.select8'), false)
select9 = new Select(document.querySelector('.select9'), false)
select10 = new Select(document.querySelector('.select10'), false)


