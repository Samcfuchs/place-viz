let keypoints = document.getElementById("keypoints").innerHTML += "<div><svg></svg></div>"
keypoints.innerHTML += "<div><svg></svg></div>"

function addKeypoint(title, divname, svgname, paragraph1, paragraph2){
    let html = document.getElementById("keypoints")
    html.innerHTML += "<div class='case' id='"+divname+"'></div>"
    let div = document.getElementById(divname)
    div.innerHTML += "<h3>"+title+"</h3>"
    div.innerHTML += "<p>"+paragraph1+"</p>"
    div.innerHTML += "<svg id='"+svgname+"' width='500' height='500' ></svg>"
    div.innerHTML += "<p>"+paragraph2+"</p>"
}