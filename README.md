# Rotating Maze Game

A **Python + Pygame** project developed as part of **Laboratory Work #6** for the *Odesa National Polytechnic University*.

## 🎓 Educational Purpose

This game was created as a practical assignment to practice:

* Sprite management
* Movement and collision detection
* Game state control
* Pygame event handling
* Object-oriented programming
* Using lists and tuples for data management

## 🎮 Game Description

Navigate through a randomly generated maze that rotates over time. The objective is to reach the green exit before the timer runs out.

### Features

* Random maze generation on every start
* Maze rotation based on selected difficulty
* Four difficulty levels: Beginner, Medium, Hard, Impossible
* Best time records saved per difficulty in `records.json`

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/rotating-maze-game.git
   cd rotating-maze-game
   ```
2. Install dependencies:

   ```bash
   pip install pygame
   ```

## 🚀 How to Run

```bash
python run.py
```

## 🕹️ Controls

* **Arrow Keys** — Move the player
* **Reach the green exit** before time runs out

## 📋 Project Structure
* `run.py` — Main file to start game
* `main.py` — Main game loop and entry point
* `menu.py` — Menu and end screen management
* `player.py` — Player behavior and movement
* `maze.py` — Maze generation, drawing, and rotation
* `rnd_cell.py` — Random cell selection
* `config.py` — Game settings and configurations
* `files.py` — Record saving and loading

## 🖼️ Screenshots

*To be added after publishing the repository*

## 📝 License

MIT License

---

This project was developed as **Laboratory Work #6** by a student of **Odesa National Polytechnic University**.

---

Feel free to star ⭐ the repository if you find it useful!
