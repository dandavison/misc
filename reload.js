function reloadForever(t) {
  location.reload()
  setTimeout(reloadForever, t);
}

reloadForever(5000)

setInterval(location.reload, 5000)


setInterval(function(){
  try{
    location.reload()
  }
  catch(err){
    console.log(err)
  }
}, 5000)
