import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import random
import kociemba
import time
import sys

colors_rgb = {
    'W': (1, 1, 1),    # White
    'Y': (1, 1, 0),    # Yellow
    'G': (0, 1, 0),    # Green
    'B': (0, 0, 1),    # Blue
    'O': (1, 0.5, 0),  # Orange
    'R': (1, 0, 0)     # Red
}

faces = ['U', 'D', 'F', 'B', 'L', 'R']
face_colors = dict(zip(faces, ['W', 'Y', 'G', 'B', 'O', 'R']))

# Create cube structure
class RubiksCube:
    def __init__(self):
        self.reset_cube()
        self.rotation_queue = []

    def reset_cube(self):
        self.cube = {face: [[face_colors[face]] * 3 for _ in range(3)] for face in faces}
        self.rotation_queue = []

    def rotate_face_clockwise(self, face):
        self.cube[face] = [list(row) for row in zip(*self.cube[face][::-1])]

    def move(self, move):
        base = move[0]
        if move.endswith("2"):
            self._apply_single_move(base)
            self._apply_single_move(base)
        elif move.endswith("'"):
            for _ in range(3): self._apply_single_move(base)
        else:
            self._apply_single_move(base)

    def _apply_single_move(self, move):
        self.rotate_face_clockwise(move)
        f = self.cube
        if move == 'U':
            f['F'][0], f['R'][0], f['B'][0], f['L'][0] = f['R'][0], f['B'][0], f['L'][0], f['F'][0]
        elif move == 'D':
            f['F'][2], f['L'][2], f['B'][2], f['R'][2] = f['L'][2], f['B'][2], f['R'][2], f['F'][2]
        elif move == 'F':
            tmp = [f['U'][2][i] for i in range(3)]
            for i in range(3): f['U'][2][i] = f['L'][2 - i][2]
            for i in range(3): f['L'][i][2] = f['D'][0][i]
            for i in range(3): f['D'][0][i] = f['R'][2 - i][0]
            for i in range(3): f['R'][i][0] = tmp[i]
        elif move == 'B':
            tmp = [f['U'][0][i] for i in range(3)]
            for i in range(3): f['U'][0][i] = f['R'][i][2]
            for i in range(3): f['R'][i][2] = f['D'][2][2 - i]
            for i in range(3): f['D'][2][i] = f['L'][i][0]
            for i in range(3): f['L'][i][0] = tmp[2 - i]
        elif move == 'L':
            tmp = [f['U'][i][0] for i in range(3)]
            for i in range(3): f['U'][i][0] = f['B'][2 - i][2]
            for i in range(3): f['B'][i][2] = f['D'][2 - i][0]
            for i in range(3): f['D'][i][0] = f['F'][i][0]
            for i in range(3): f['F'][i][0] = tmp[i]
        elif move == 'R':
            tmp = [f['U'][i][2] for i in range(3)]
            for i in range(3): f['U'][i][2] = f['F'][i][2]
            for i in range(3): f['F'][i][2] = f['D'][i][2]
            for i in range(3): f['D'][i][2] = f['B'][2 - i][0]
            for i in range(3): f['B'][i][0] = tmp[2 - i]

    def scramble(self):
        self.scramble_moves = [random.choice(['U', "U'", 'D', "D'", 'L', "L'", 'R', "R'", 'F', "F'", 'B', "B'"]) for _ in range(20)]
        for move in self.scramble_moves:
            self.move(move)
        self.rotation_queue = []

    def to_kociemba_string(self):
        face_order = ['U', 'R', 'F', 'D', 'L', 'B']
        color_map = {}
        for face in face_order:
            center_color = self.cube[face][1][1]
            color_map[center_color] = face

        facelets = ''
        for face in face_order:
            for row in self.cube[face]:
                for color in row:
                    facelets += color_map[color]
        return facelets

    def solve(self):
        try:
            facelets = self.to_kociemba_string()
            solution = kociemba.solve(facelets)
            self.rotation_queue = solution.split()
        except Exception as e:
            print("Solver Error:", e)
            self.rotation_queue = []

# Draw a single cubie
def draw_cubie(x, y, z, colors_faces):
    glPushMatrix()
    glTranslatef(x, y, z)
    for face, color in colors_faces.items():
        glColor3fv(colors_rgb[color])
        glBegin(GL_QUADS)
        if face == 'F':
            glVertex3f(-0.5, -0.5, 0.5)
            glVertex3f(0.5, -0.5, 0.5)
            glVertex3f(0.5, 0.5, 0.5)
            glVertex3f(-0.5, 0.5, 0.5)
        elif face == 'B':
            glVertex3f(0.5, -0.5, -0.5)
            glVertex3f(-0.5, -0.5, -0.5)
            glVertex3f(-0.5, 0.5, -0.5)
            glVertex3f(0.5, 0.5, -0.5)
        elif face == 'U':
            glVertex3f(-0.5, 0.5, -0.5)
            glVertex3f(0.5, 0.5, -0.5)
            glVertex3f(0.5, 0.5, 0.5)
            glVertex3f(-0.5, 0.5, 0.5)
        elif face == 'D':
            glVertex3f(-0.5, -0.5, 0.5)
            glVertex3f(0.5, -0.5, 0.5)
            glVertex3f(0.5, -0.5, -0.5)
            glVertex3f(-0.5, -0.5, -0.5)
        elif face == 'L':
            glVertex3f(-0.5, -0.5, -0.5)
            glVertex3f(-0.5, -0.5, 0.5)
            glVertex3f(-0.5, 0.5, 0.5)
            glVertex3f(-0.5, 0.5, -0.5)
        elif face == 'R':
            glVertex3f(0.5, -0.5, 0.5)
            glVertex3f(0.5, -0.5, -0.5)
            glVertex3f(0.5, 0.5, -0.5)
            glVertex3f(0.5, 0.5, 0.5)
        glEnd()
    glPopMatrix()

# Draw the entire cube
def draw_cube(cube: RubiksCube):
    spacing = 1.05
    for x in range(3):
        for y in range(3):
            for z in range(3):
                colors_faces = {}
                if y == 2: colors_faces['U'] = cube.cube['U'][2 - z][x]
                if y == 0: colors_faces['D'] = cube.cube['D'][z][x]
                if z == 2: colors_faces['F'] = cube.cube['F'][2 - y][x]
                if z == 0: colors_faces['B'] = cube.cube['B'][y][2 - x]
                if x == 0: colors_faces['L'] = cube.cube['L'][2 - y][z]
                if x == 2: colors_faces['R'] = cube.cube['R'][2 - y][2 - z]
                draw_cubie((x - 1) * spacing, (y - 1) * spacing, (z - 1) * spacing, colors_faces)

def main():
    pygame.init()
    display = (900, 700)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("3D Rubik's Cube")

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)
    glEnable(GL_DEPTH_TEST)

    cube = RubiksCube()
    angle = 0

    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(angle, 1, 1, 0)
        draw_cube(cube)
        glPopMatrix()

        angle += 0.3

        if cube.rotation_queue:
            move = cube.rotation_queue.pop(0)
            cube.move(move)
            time.sleep(0.2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_r:
                    cube.reset_cube()
                elif event.key == K_s:
                    cube.scramble()
                elif event.key == K_RETURN:
                    cube.solve()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
