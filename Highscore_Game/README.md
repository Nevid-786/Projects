# 🏆 Highscore Game

This is a fun little Python project that simulates scoring in a game and tracks your **highest score**. Each time you play, the game generates a random score between 1 and 1000. If your new score is higher than the previous one, it's saved as the new high score.

The score is saved to a local file named `hiscore.txt`.

## 🚀 Features

- Random score generation
- Persistent high score tracking using a text file
- Option to play again or reset the high score

## 🧠 How it works

1. At the start, it checks if the `hiscore.txt` file exists.
2. When the game runs:
   - A random score is generated.
   - The score is compared to the previous high score.
   - If it's higher, the file is updated.
   - You can play again or reset the high score.

## ▶️ How to Run

Make sure you have Python installed. Then run:

```bash
python Highscore_game.py
