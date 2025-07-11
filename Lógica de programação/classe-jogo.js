// Classe genérica que representa um herói de uma aventura
class Heroi {
  constructor(nome, idade, tipo) {
    this.nome = nome;
    this.idade = idade;
    this.tipo = tipo;
  }

  atacar() {
    let ataque = "";

    // Estrutura de decisão para definir o tipo de ataque
    switch (this.tipo.toLowerCase()) {
      case "mago":
        ataque = "magia";
        break;
      case "guerreiro":
        ataque = "espada";
        break;
      case "monge":
        ataque = "artes marciais";
        break;
      case "ninja":
        ataque = "shuriken";
        break;
      default:
        ataque = "um ataque desconhecido";
    }

    console.log(`O ${this.tipo} atacou usando ${ataque}!`);
  }
}

// Exemplo de uso:

// Criação de alguns heróis
const heroi1 = new Heroi("Merlin", 150, "mago");
const heroi2 = new Heroi("Arthas", 30, "guerreiro");
const heroi3 = new Heroi("Lee", 25, "monge");
const heroi4 = new Heroi("Hanzo", 28, "ninja");

// Cada herói realiza um ataque
heroi1.atacar(); // O mago atacou usando magia
heroi2.atacar(); // O guerreiro atacou usando espada
heroi3.atacar(); // O monge atacou usando artes marciais
heroi4.atacar(); // O ninja atacou usando shuriken

