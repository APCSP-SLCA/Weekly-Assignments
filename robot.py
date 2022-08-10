# Tell Python we want to use the pyglet module
import pyglet

# Create a window for our application to run on!
# Notice we use dot notation to access the Window class

TITLE = "robot.py"
WIDTH = 600
HEIGHT = 600
GRID_DIM = 2
CELL_SIZE = WIDTH // GRID_DIM
batch = pyglet.graphics.Batch()

grid = []
for i in range(GRID_DIM):
    row = []
    for j in range(GRID_DIM):
        x = j*CELL_SIZE
        y = i*CELL_SIZE
        row.append(pyglet.shapes.BorderedRectangle(x, y, CELL_SIZE, CELL_SIZE,
                                           color=(255, 255, 255), border=2,
                                           batch=batch))

    grid.append(row)





window = pyglet.window.Window(width=WIDTH, height=HEIGHT)
window.set_caption(TITLE)


# Runs on_draw at a certain frame rate
@window.event
def on_draw():
    window.clear()  # clears the screen
    batch.draw()

pyglet.app.run()