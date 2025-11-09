// Script para o Carrossel da Página de Produto
var elemsCarrosselBotao = document.querySelectorAll(
  ".s-produto__carrossel-botao"
);
var elemCarrosselImagens = document.querySelector(
  ".s-produto__carrossel-itens"
);

elemsCarrosselBotao.forEach(function (elem, i) {
  elem.addEventListener("click", function () {
    elemCarrosselImagens.style = "transform: translateX(-" + i * 100 + "%)";

    elemsCarrosselBotao.forEach(function (ele) {
      if (ele != elem) {
        ele.classList.remove("s-produto__carrossel-botao--selecionado");
      } else {
        ele.classList.add("s-produto__carrossel-botao--selecionado");
      }
    });
  });
});
