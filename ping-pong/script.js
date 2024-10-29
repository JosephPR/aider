class PongGame {
    constructor() {
        this.paddle1 = document.getElementById('paddle1');
        this.paddle2 = document.getElementById('paddle2');
        this.ball = document.getElementById('ball');
        this.score1Element = document.getElementById('score1');
        this.score2Element = document.getElementById('score2');
        this.games1Element = document.getElementById('games1');
        this.games2Element = document.getElementById('games2');
        this.startBtn = document.getElementById('start-btn');
        this.resetBtn = document.getElementById('reset-btn');

        this.gameBoard = document.getElementById('game-board');
        this.boardHeight = this.gameBoard.offsetHeight;
        this.boardWidth = this.gameBoard.offsetWidth;

        this.paddle1Pos = 160;
        this.paddle2Pos = 160;
        this.ballX = this.boardWidth / 2;
        this.ballY = this.boardHeight / 2;
        this.ballSpeedX = 5;
        this.ballSpeedY = 5;
        this.paddleSpeed = 8;

        this.score1 = 0;
        this.score2 = 0;
        this.games1 = 0;
        this.games2 = 0;
        this.isGameRunning = false;

        this.keys = {
            w: false,
            s: false,
            ArrowUp: false,
            ArrowDown: false
        };

        this.init();
    }

    init() {
        this.setupEventListeners();
        this.startBtn.addEventListener('click', () => this.startGame());
        this.resetBtn.addEventListener('click', () => this.resetAll());
        this.gameLoop = this.gameLoop.bind(this);
    }

    setupEventListeners() {
        document.addEventListener('keydown', (e) => {
            if (this.keys.hasOwnProperty(e.key)) {
                this.keys[e.key] = true;
            }
        });

        document.addEventListener('keyup', (e) => {
            if (this.keys.hasOwnProperty(e.key)) {
                this.keys[e.key] = false;
            }
        });
    }

    startGame() {
        if (!this.isGameRunning) {
            this.isGameRunning = true;
            this.gameLoop();
            this.startBtn.textContent = 'Pause';
        } else {
            this.isGameRunning = false;
            this.startBtn.textContent = 'Resume';
        }
    }

    resetAll() {
        this.score1 = 0;
        this.score2 = 0;
        this.games1 = 0;
        this.games2 = 0;
        this.updateScore();
        this.resetBall();
        this.isGameRunning = false;
        this.startBtn.textContent = 'Start Game';
    }

    resetBall() {
        this.ballX = this.boardWidth / 2;
        this.ballY = this.boardHeight / 2;
        this.ballSpeedX = 5 * (Math.random() > 0.5 ? 1 : -1);
        this.ballSpeedY = 5 * (Math.random() > 0.5 ? 1 : -1);
    }

    updateScore() {
        this.score1Element.textContent = this.score1;
        this.score2Element.textContent = this.score2;
        this.games1Element.textContent = this.games1;
        this.games2Element.textContent = this.games2;
    }

    checkGameWin() {
        if (this.score1 >= 11 && this.score1 - this.score2 >= 2) {
            this.games1++;
            this.score1 = 0;
            this.score2 = 0;
            this.updateScore();
            return true;
        } else if (this.score2 >= 11 && this.score2 - this.score1 >= 2) {
            this.games2++;
            this.score1 = 0;
            this.score2 = 0;
            this.updateScore();
            return true;
        }
        return false;
    }

    movePaddles() {
        if (this.keys.w && this.paddle1Pos > 0) {
            this.paddle1Pos -= this.paddleSpeed;
        }
        if (this.keys.s && this.paddle1Pos < this.boardHeight - 80) {
            this.paddle1Pos += this.paddleSpeed;
        }
        if (this.keys.ArrowUp && this.paddle2Pos > 0) {
            this.paddle2Pos -= this.paddleSpeed;
        }
        if (this.keys.ArrowDown && this.paddle2Pos < this.boardHeight - 80) {
            this.paddle2Pos += this.paddleSpeed;
        }

        this.paddle1.style.top = `${this.paddle1Pos}px`;
        this.paddle2.style.top = `${this.paddle2Pos}px`;
    }

    moveBall() {
        this.ballX += this.ballSpeedX;
        this.ballY += this.ballSpeedY;

        // Wall collisions
        if (this.ballY <= 0 || this.ballY >= this.boardHeight - 10) {
            this.ballSpeedY = -this.ballSpeedY;
        }

        // Paddle collisions
        if (this.ballX <= 20 && this.ballY >= this.paddle1Pos && this.ballY <= this.paddle1Pos + 80) {
            this.ballSpeedX = -this.ballSpeedX;
            this.ballSpeedX *= 1.1;
            this.ballSpeedY *= 1.1;
        }
        if (this.ballX >= this.boardWidth - 30 && this.ballY >= this.paddle2Pos && this.ballY <= this.paddle2Pos + 80) {
            this.ballSpeedX = -this.ballSpeedX;
            this.ballSpeedX *= 1.1;
            this.ballSpeedY *= 1.1;
        }

        // Scoring
        if (this.ballX <= 0) {
            this.score2++;
            this.updateScore();
            if (this.checkGameWin()) {
                this.resetBall();
                return;
            }
            this.resetBall();
        }
        if (this.ballX >= this.boardWidth - 10) {
            this.score1++;
            this.updateScore();
            if (this.checkGameWin()) {
                this.resetBall();
                return;
            }
            this.resetBall();
        }

        this.ball.style.left = `${this.ballX}px`;
        this.ball.style.top = `${this.ballY}px`;
    }

    gameLoop() {
        if (!this.isGameRunning) return;

        this.movePaddles();
        this.moveBall();

        requestAnimationFrame(this.gameLoop);
    }
}

// Initialize the game when the window loads
window.onload = () => {
    new PongGame();
};
