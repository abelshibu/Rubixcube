from utils import create_solved_cube, print_cube, dummy_solver

def scramble_cube(cube):
    cube['U'][0][0] = 'B'  # mock scramble
    return cube

def write_output(scrambled, moves):
    with open("output.txt", "w") as f:
        f.write("Rubik’s Cube Solver Output\n\n")
        f.write("Scrambled Cube:\n")
        for face in ['U', 'D', 'L', 'R', 'F', 'B']:
            f.write(f"{face} Face:\n")
            for row in scrambled[face]:
                f.write(" ".join(row) + "\n")
            f.write("\n")
        f.write("Solution Moves:\n")
        f.write(" ".join(moves) + "\n")
        f.write(f"\nTotal Moves: {len(moves)}\n")

if __name__ == "__main__":
    cube = create_solved_cube()
    scrambled = scramble_cube(cube)

    print("Scrambled Cube:")
    print_cube(scrambled)

    solution_moves = dummy_solver(scrambled)
    print("Solution:")
    print(" ".join(solution_moves))

    write_output(scrambled, solution_moves)
