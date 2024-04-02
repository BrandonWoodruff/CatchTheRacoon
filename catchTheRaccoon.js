const { createCanvas, loadImage } = require("canvas");
const fs = require("fs");
const readline = require("readline");

const WIDTH = 1000;
const HEIGHT = 800;
const BLACK = "#000000";
const WHITE = "#FFFFFF";

class DisplayGame {
  constructor() {
    this.canvas = createCanvas(WIDTH, HEIGHT);
    this.ctx = this.canvas.getContext("2d");
  }

  async background() {
    const background = await loadImage("background.jpg");
    this.ctx.drawImage(background, 0, 0);
  }

  async title() {
    const icon = await loadImage("dabr.jpg");
    // Set icon - not supported in node-canvas
    // Set caption - not supported in node-canvas
  }

  score(score) {
    this.ctx.fillStyle = WHITE;
    this.ctx.font = "36px Arial";
    this.ctx.fillText(`Score: ${score}`, 10, 10);
  }

  countdown(start) {
    this.ctx.fillStyle = WHITE;
    this.ctx.font = "36px Arial";
    this.ctx.fillText(`Countdown: ${Math.ceil(start / 1000)}`, 700, 10);
  }

  start_game() {
    this.ctx.fillStyle = BLACK;
    this.ctx.fillRect(0, 0, WIDTH, HEIGHT);

    this.ctx.fillStyle = WHITE;
    this.ctx.font = "72px Arial";
    this.ctx.fillText("Catch the Raccoon", WIDTH / 2 - 250, HEIGHT / 2 - 50);
    this.ctx.font = "36px Arial";
    this.ctx.fillText(
      "Press Space to start the game",
      WIDTH / 2 - 240,
      HEIGHT / 2
    );
  }

  game_over(score) {
    this.ctx.fillStyle = BLACK;
    this.ctx.fillRect(0, 0, WIDTH, HEIGHT);

    this.ctx.fillStyle = WHITE;
    this.ctx.font = "64px Arial";
    this.ctx.fillText("Game Over", WIDTH / 2 - 200, HEIGHT / 2 - 50);
    this.ctx.fillText(`Score: ${score}`, WIDTH / 2 - 150, HEIGHT / 2);
  }

  async saveToFile(fileName) {
    const out = fs.createWriteStream(fileName);
    const stream = this.canvas.createPNGStream();
    stream.pipe(out);
    out.on("finish", () => console.log("The PNG file was created."));
  }
}

class Racket {
  constructor() {
    this.image = "racket.png";
    this.x = WIDTH / 2;
    this.y = HEIGHT / 2;
  }

  async racket_display(ctx) {
    const image = await loadImage(this.image);
    ctx.drawImage(image, this.x, this.y);
  }

  async racket_movement() {
    // Handle keyboard input - not supported in node.js directly
    // You can use readline or similar libraries for user input
  }
}

class Raccoon {
  constructor() {
    this.image = "racoon.png";
    this.x = WIDTH / 2;
    this.y = HEIGHT / 2;
  }

  async raccoon_display(ctx) {
    const image = await loadImage(this.image);
    ctx.drawImage(image, this.x, this.y);
  }
}

async function main() {
  const game = new DisplayGame();
  await game.background();
  await game.title();
  game.start_game();

  const racket = new Racket();
  const raccoon = new Raccoon();
  let score = 0;
  let start = 30000;

  while (true) {
    // Game logic and event handling
    // Implement your game loop here
    // You may need to use readline or similar libraries for input handling

    // Render the game
    game.ctx.clearRect(0, 0, WIDTH, HEIGHT);
    await racket.racket_display(game.ctx);
    await raccoon.raccoon_display(game.ctx);
    game.score(score);
    game.countdown(start);
    // You may need to periodically call await game.saveToFile(fileName) to save the game state as an image
  }

  // Game over logic
  game.game_over(score);
  // You may need to call await game.saveToFile(fileName) to save the game over screen as an image
}

// Call the main function
main();
