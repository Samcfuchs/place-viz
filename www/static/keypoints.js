function addKeypoint(title, divname, heatmapname, paragraph1, paragraph2) {
    let html = document.getElementById("keypoints")
    html.innerHTML += "<div class='case' id='" + divname + "'></div>"
    let div = document.getElementById(divname)
    div.innerHTML += "<h3>" + title + "</h3>"
    div.innerHTML += "<p>" + paragraph1 + "</p>"
    div.innerHTML += "<div class='heatmap' id='" + heatmapname + "'></div>"
    div.innerHTML += "<p>" + paragraph2 + "</p>"
}