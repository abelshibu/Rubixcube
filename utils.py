# utils.py

def create_solved_cube():
    faces = ['W', 'Y', 'O', 'R', 'G', 'B']  # U, D, L, R, F, B
    return {
        'U': [[faces[0]] * 3 for _ in range(3)],
        'D': [[faces[1]] * 3 for _ in range(3)],
        'L': [[faces[2]] * 3 for _ in range(3)],
        'R': [[faces[3]] * 3 for _ in range(3)],
        'F': [[faces[4]] * 3 for _ in range(3)],
        'B': [[faces[5]] * 3 for _ in range(3)],
    }

def print_cube(cube):
    for face in ['U', 'D', 'L', 'R', 'F', 'B']:
        print(f"{face} Face:")
        for row in cube[face]:
            print(" ".join(row))
        print()

def dummy_solver(cube):
    return ["F'", "R", "U", "R'", "U'", "F"]
