const http = require("http");
//Criando o servidor
const server = http.createServer((req, res) => {
  console.log(req.method);
  console.log(req.url);
  res.statusCode = 201;
  res.end("<h1>Olá Everson</h1>");
});
//O servidor irá ficar ouvindo a porta 3000, ou seja, qualquer coisa que acontecer nessa porta será notificada no nosso servidor
server.listen(3000, () => {
  console.log("Servidor Ativo!");
});
