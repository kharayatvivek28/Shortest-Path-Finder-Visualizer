import pygame
from canvas import Canvas
from buttons import Button
from graph_engine import dijkstra
from graphs.graph_data import get_random_graph

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1400, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shortest Path Finder - Dijkstra Visualizer")

# Set up the reduced graph area (85% for the graph)
GRAPH_WIDTH = int(WIDTH * 0.85)
UI_WIDTH = WIDTH - GRAPH_WIDTH  # Remaining space for UI/buttons

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Create canvas for graph drawing (only the graph area will be used)
canvas = Canvas(screen, GRAPH_WIDTH, HEIGHT)

# Initialize graph data and load it
graph_data = get_random_graph()
canvas.load_graph(graph_data)

# Pathfinding variables
path = []
visited = []

# Dijkstra function to run the algorithm and update visualization
def run_dijkstra():
    global path, visited
    path, visited_set = dijkstra(
        canvas.graph,
        graph_data['start'],
        graph_data['end'],
        lambda visited=[]: canvas.draw_graph(path=path, visited=visited,
                                             start=graph_data['start'], end=graph_data['end']) or pygame.display.update(),
        delay=0.3
    )
    visited = list(visited_set)

# Reset graph function
def reset_graph():
    global path, visited, graph_data
    path = []
    visited = []
    graph_data = get_random_graph()  # Get new random graph
    canvas.load_graph(graph_data)  # Load the new graph

# Font for button labels
font = pygame.font.SysFont(None, 30)

# Buttons for running Dijkstra and resetting the graph, with margin to the right
buttons = [
    Button(20, 620, 160, 50, "Find Shortest Path", run_dijkstra),
    Button(200, 620, 120, 50, "Reset Graph", reset_graph)
]

# Main loop
running = True
while running:
    # Fill background with a dark color
    screen.fill((25, 25, 25))

    # Draw the graph (path, visited nodes, start, and end)
    canvas.draw_graph(path=path, visited=visited, start=graph_data['start'], end=graph_data['end'])

    # Draw buttons in the UI area (right side)
    for button in buttons:
        button.draw(screen)

    # Event handling loop
    for event in pygame.event.get():
        canvas.handle_event(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for button in buttons:
                button.check_click(pos)

    # Update the screen
    pygame.display.update()

    # Frame rate control (60 frames per second)
    clock.tick(60)

# Quit Pygame
pygame.quit()
