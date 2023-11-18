/*
 * Click on a reading in the Perusall web interface,
 * and run this script in the developer console.
 * Copy-and-paste the console.info output to data.py.
 */
var len = 0; 
var times = 0;
var i = setInterval(() => { 
  var img = document.querySelectorAll("img.chunk"); img[img.length-1].scrollIntoView(); 
  if (len < img.length) {
    len = img.length;
  } else if (times > 3) {
    var urls = [];
    img.forEach((e) => urls.push(e.src));
    var spl = location.pathname.split('/');
    console.info('urls = """\n'+urls.join('\n')+'\n"""\n\ntitle="'+spl[spl.length-1]+'"\n');
    clearInterval(i);
  } else {
      times++;
  }
}, 2000);