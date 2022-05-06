function addKeypoint(title, divname, heatmapname, imglist, paragraph1, paragraph2) {
    let html = document.getElementById("keypoints")
    html.innerHTML += "<div class='case' id='" + divname + "'></div>"
    let div = document.getElementById(divname)
    div.innerHTML += "<h3>" + title + "</h3>"
    div.innerHTML += "<p>" + paragraph1 + "</p>"
    div.innerHTML += "<div class='heatmap' id='" + heatmapname + "'></div>"
    div.innerHTML += "<p>" + paragraph2 + "</p>"
    if(imglist.length>0){
        num_imgs = imglist.length
        img_counter = 1
        console.log(imglist)
        imglist.forEach(img => {
            div.innerHTML += "<div class='imgandtext' id='" + divname + img_counter + "img'></div>"
            let imgdiv = document.getElementById(divname + img_counter+'img')
            imgdiv.innerHTML += "<img src='images/"+img[0]+"'>"
            imgdiv.innerHTML += "<p>" + img[1] + "</p>"
            if(img_counter%2 == 0){
                document.getElementById(divname + img_counter+'img').classList.add("reverse")
            }
            img_counter+=1
        });
    }
}