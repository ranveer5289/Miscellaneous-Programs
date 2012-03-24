var res = document.evaluate("//title/text()",document,null,XPathResult.ANY_TYPE,null);
var theTitle = res.iterateNext();
while (theTitle){
alert(theTitle.textContent);
theTitle = res.iterateNext();
}

//----------------------################_______________###############################_____________________
//-------TORRENTZ.ME---------------------------------------------------------------------------------------

var res = document.evaluate("html/body/div[3]/dl[4]/dt/a/@href",document,null,XPathResult.ANY_TYPE,null);
var link;
var theLink = res.iterateNext();
while (theLink){
link = (theLink.textContent);
theLink = res.iterateNext();
}
window.name = link

var tracker_link = document.evaluate("html/body/div[3]/dl[2]/dt/a/@href",document,null,XPathResult.ANY_TYPE,null);
var theTracker = tracker_link.iterateNext();
while (theTracker){
tracker = (theTracker.textContent);
theTracker = Tracker_link.iterateNext();
}
tracker

var torrent_link = document.evaluate(".//*[@id='details']/div[2]/a[1]/@href",document,null,XPathResult.ANY_TYPE,null);
var theTorrent = torrent_link.iterateNext();
while (theTorrent){
torrent = (theTorrent.textContent);
theTorrent = torrent_link.iterateNext();
}
torrent




