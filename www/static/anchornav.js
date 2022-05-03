// Code referenced from : https://codepen.io/malsu/pen/VwKzoPG

function navHighlighter() {
  
  // Get current scroll position
  let scrollY = window.pageYOffset;

  // loop thru sections to get height, top and id vals
  sections.forEach(current => {
    const sectionHeight = current.offsetHeight;
    const sectionTop = current.offsetTop - 50;
    sectionId = current.getAttribute("id");

    if (
      scrollY > sectionTop &&
      scrollY <= sectionTop + sectionHeight
    ){
      document.querySelector(".nav a[href*=" + sectionId + "]").classList.add("active");
    } else {
      document.querySelector(".nav a[href*=" + sectionId + "]").classList.remove("active");
    }
  });
}
