const playerSymbol = "O";
const aiSymbol = "X";
let currentPlayer = playerSymbol;
let gameBoard = Array(9).fill(null);
const cells = document.querySelectorAll(".cell");
const messageElement = document.getElementById("message");
const resetBtn = document.getElementById("resetBtn");

/**
 * @param {MouseEvent} event
 * @returns {Promise<void>}
 */
async function handleClick(event) {
  const index = event.target.getAttribute("data-cell");
  console.log(index, gameBoard[index]);

  if (gameBoard[index] || messageElement.textContent.includes("wins")) return;

  gameBoard[index] = currentPlayer;
  event.target.textContent = currentPlayer;
  event.target.classList.add("taken");

  try {
    const response = await fetch("http://127.0.0.1:5000/player_turn", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ row: Math.floor(index / 3), col: index % 3 }),
    });
    /**
     * @type {import("./types").trunResponse}
     */
    const data = await response.json();

    if (data.winner) {
      messageElement.textContent = `${data.winner} wins!`;
      document.getElementById(
        "score"
      ).textContent = `X = ${data.score.X}, O = ${data.score.O}`;

      return;
    } else if (data.message === "It's a draw!") {
      messageElement.textContent = data.message;
      return;
    } else {
      currentPlayer = aiSymbol;
      messageElement.textContent = `${currentPlayer}'s turn`;
      await sendAITurn();
    }
  } catch (error) {
    console.error("Error handling player move:", error);
  }
}

/**
 * @returns {Promise<void>}
 */

async function sendAITurn() {
  try {
    const response = await fetch("http://127.0.0.1:5000/ai_turn");
    if (!response.ok) {
      throw new Error("Failed to send AI turn");
    }
    /**
     * @type {import("./types").trunResponse}
     */
    const data = await response.json();

    if (data.winner) {
      const aiIndex = data.cell[0] * 3 + data.cell[1];
      cells[aiIndex].textContent = aiSymbol;
      cells[aiIndex].classList.add("taken");
      messageElement.textContent = `${data.winner} wins!`;
      document.getElementById(
        "score"
      ).textContent = `X = ${data.score.X}, O = ${data.score.O}`;
    } else if (data.message === "It's a draw!") {
      messageElement.textContent = data.message;
    } else {
      const aiIndex = data.cell[0] * 3 + data.cell[1];
      gameBoard[aiIndex] = aiSymbol;
      cells[aiIndex].textContent = aiSymbol;
      cells[aiIndex].classList.add("taken");

      currentPlayer = playerSymbol;
      messageElement.textContent = `${currentPlayer}'s turn`;
    }
  } catch (error) {
    console.error("Error handling AI move:", error);
  }
}

async function resetGame() {
  try {
    const response = await fetch("http://127.0.0.1:5000/reset", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();

    if (data.message === "Game reset successful") {
      gameBoard = Array(9).fill(null);
      cells.forEach((cell) => {
        cell.textContent = "";
        cell.classList.remove("taken");
      });

      currentPlayer = playerSymbol;
      messageElement.textContent = "Player's turn (X)";
      console.log("Game has been reset on the server.");
    } else {
      console.log("Error resetting game:", data.message);
    }
  } catch (error) {
    console.error("Error resetting game:", error);
  }
}

cells.forEach((cell) => cell.addEventListener("click", handleClick));
resetBtn.addEventListener("click", resetGame);
