// dom 속성
const li = document.querySelector('li')
// html 태그를 모델링하여 js로 갖고 왔고 
// li.만 하면 사용할 수 있는 속성들이 한가득 나타남

const search = document.querySelector('park')
search.classList.add('zero')
search.classList.remove('zero')
search.classList.contains('zero') //true/false
search.innerHTML='<h3>zerobase</h3>'
