showModal = (name,desc,url,loc,cat) => {
    console.log(name,desc,url)
    $("#label").text(name)
    $("#myModal").modal("show")
    $(".mod-img").attr("src",url)
    $("#img-desc").text(desc)
    $("#url-to-copy").val(window.location.origin + url)
    $("#img-location").text("Location: " + loc)
    $("#img-category").text("Category: " + cat)
}
copyUrl = () => {
    $("#url-to-copy").select()
    document.execCommand('copy');
    alert("Link copied")
}