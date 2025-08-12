
carousel_items = document.getElementsByClassName("carousel-item")
function add_class(){
      if(carousel_items.length > 0){
        carousel_items[0].classList.add('active');
      }
 }
 add_class()