const dJSON = require('dirty-json');
const getStdin = require('get-stdin');

getStdin().then(function(s) {
  dJSON.parse(s).then(function (r) {
	console.log(JSON.stringify(r));
  })
});
