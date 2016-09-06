var page = require('webpage').create(),
	system = require('system'),
	address = 'http://www.baidu.com';

page.onResourceRequested = function(req) {
	var url = req.url;
	// Declare a new Dicts!
	var theRequest = new Object();

	if (url.indexOf("?") != -1 ) {
		var str = url.substr(1);
		strs = str.split("&");
		for (var i =0; i < strs.length; i++) {
			// Fill the Dicts with param name & param value!
			theRequest[strs[i].split("=")[0]] = unescape(strs[i].split("=")[1]);
		}
	}
	if (theRequest) {
		// if the dict have fill with some data ...
		if (theRequest.hasOwnProperty("sid") && theRequest.hasOwnProperty("cb")){
			var cookies = page.cookies
			theRequest.cookies = cookies
			console.log(JSON.stringify(theRequest, undefined, 4));
		}
	}
};
	
page.open(address, function(status) {
		if (status !== 'success') {
			console.log('Fail to load the address');
		}
		phantom.exit();
});

