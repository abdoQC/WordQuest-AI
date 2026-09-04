# WordQuest AI

An interactive Python word-search game that visualizes how three classic search algorithms solve a word path on a 10 x 10 letter grid.

![Python](https://img.shields.io/badge/Python-Tkinter-3776AB?logo=python&logoColor=white)

## What it does

Enter a word that appears in the grid, then choose an algorithm:

- **DFS** explores the available path depth-first.
- **BFS** explores candidate paths breadth-first.
- **A\*** uses a distance-based heuristic to guide the search.

The interface animates the algorithm's exploration and highlights the final word path in gold when a solution is found. You can also click cells to mark them manually and right-click to reset their color.

## Built with

- Python
- Tkinter
- `heapq` for the A* priority queue

## Run locally

Python 3 is the only requirement; Tkinter is bundled with most standard Python installations.

```bash
python wordquest.py
```

On Windows, if `python` is not available on your PATH, install Python 3 from [python.org](https://www.python.org/downloads/) and select **Add Python to PATH** during installation.

## How to play

1. Run the program.
2. Enter a word from the displayed word list, such as `CAT`, `WORDQUEST`, or `MANSOURA`.
3. Click **DFS**, **BFS**, or **A\***.
4. Watch the algorithm explore adjacent horizontal, vertical, and diagonal cells.
5. When found, the successful path is highlighted in gold.

## Screenshots to add

Add screenshots here after running the game:

- Main screen showing the 10 x 10 letter board and word list.
- A search in progress, showing the exploration colors for DFS, BFS, or A*.
- A completed search with the gold solution path.

## Authors

Abdelrahman Ehab, Bishoy Nabil, and Emad Shokry
