var http = require("http");
var session = require('client-sessions');
var helloworld = require("./helloworld.js");

app.use(session({
  cookieName: 'session',
  secret: 'random_string_goes_here',
  duration: 30 * 60 * 1000,
  activeDuration: 5 * 60 * 1000,
}));

http.createServer(function (request, response) {
  var get_data = require('url').parse(request.url);

  console.log(get_data);
  console.log(get_data['pathname']);

  if(get_data['pathname'] == "/hello"){
    helloworld.sayhello(response);
  }

  switch(get_data['pathname']) {
    case "/hello":
      helloworld.sayhello(response);
      break;
    case "/":
      response.writeHead(200, {'Content-Type': 'text/plain'});
      response.end("Nothing here yet");
      break;

  }
}).listen(8081);

// Console will print the message
console.log('Server running at http://localhost:8081/');
