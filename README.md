
# 🧊 3D Rubik’s Cube Visualizer & Solver

A realistic, interactive **3D Rubik’s Cube** built using `Pygame`, `OpenGL`, and `kociemba`. Supports scrambling, solving, and cube rotations with visual animation.



---

### 🚀 Features

- ✅ Fully rendered 3D Rubik’s Cube using OpenGL
- 🎨 Realistic face colors and 3D cubies
- 🔁 Rotation animation
- 🔄 Scramble the cube randomly
- 🤖 Solve using the [Kociemba two-phase algorithm](https://github.com/muodov/kociemba)
- ⌨️ Keyboard controls (`R`, `S`, `Enter`)

---

### 🎮 Controls

| Key         | Action               |
|-------------|----------------------|
| `S`         | Scramble the cube    |
| `R`         | Reset to solved state |
| `Enter`     | Solve using Kociemba |
| `X` (close) | Quit the app         |

---

### 📦 Requirements

Install dependencies using `pip`:

```bash
pip install pygame PyOpenGL numpy kociemba
```

> Python 3.8+ recommended

---

### ▶️ Run the App

Make sure your working directory contains the script, then run:

```bash
python cube.py
```

---

### 🧠 How It Works

- **Cube Representation**: A `RubiksCube` class holds the cube state using 6 face matrices.
- **Rotation Logic**: Simulates realistic face rotations, including clockwise, counter-clockwise, and double turns.
- **Kociemba Solver**: Converts cube state to string, passes to `kociemba.solve()` for optimal solving.
- **OpenGL Rendering**: Draws 27 cubies with correct face colors, rendered in real-time with animation.

---

### 📸 Example

**Scrambled Cube**:

![Scrambled]([example_scramble.png](https://res.cloudinary.com/ddnlumst5/image/upload/v1754164156/Screenshot_2025-08-02_203425_ddsa2o.png))

**Solving...**

![Solving]([example_solving.png](https://res.cloudinary.com/ddnlumst5/image/upload/v1754164156/Screenshot_2025-08-02_203411_utyt2u.png))

---

### 🛠️ Troubleshooting

- **Black screen**? Check your GPU or OpenGL support.
- **`ModuleNotFoundError`**? Ensure all dependencies are installed.
- **Solver not working?** Cube state may be invalid or unsolvable.

---

### ✨ To-Do / Future Ideas

- Add mouse-based face rotation
- Add solving animation by face
- Support different solving methods (CFOP, Beginner’s, etc.)
- GUI buttons (scramble/solve/reset)

---

### 📄 License

MIT License © YourName
