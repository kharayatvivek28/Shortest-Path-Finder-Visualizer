import pygame
import networkx as nx

class Canvas:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.graph = nx.Graph()
        self.pos = {}

        self.offset_x = 0
        self.offset_y = 0
        self.dragging = False
        self.last_mouse_pos = (0, 0)
        self.zoom_level = 1.0

    def load_graph(self, graph_data):
        self.graph.clear()
        self.pos.clear()
        self.graph.add_nodes_from(graph_data['nodes'])
        self.graph.add_weighted_edges_from(graph_data['edges'])
        self.pos = nx.spring_layout(self.graph, seed=42)

    def draw_graph(self, path=None, visited=None, start=None, end=None):
        self.screen.fill((25, 25, 25))
        radius = int(20 * self.zoom_level)

        for edge in self.graph.edges(data=True):
            src, dst, data = edge
            color = (200, 200, 200)
            if path and (src, dst) in zip(path, path[1:]) or (dst, src) in zip(path, path[1:]):
                color = (255, 215, 0)
            elif visited and (src in visited and dst in visited):
                color = (100, 100, 255)
            pygame.draw.line(self.screen, color, self.scale(self.pos[src]), self.scale(self.pos[dst]), max(1, int(4 * self.zoom_level)))

            # Draw edge weights in pink with a larger font size
            mid_x = (self.pos[src][0] + self.pos[dst][0]) / 2
            mid_y = (self.pos[src][1] + self.pos[dst][1]) / 2
            weight_pos = self.scale((mid_x, mid_y))

            # Increase font size for weight label (even more visible)
            font_size = int(50 * self.zoom_level)  # Much larger font size for weight text
            font = pygame.font.SysFont(None, font_size)
            weight_surf = font.render(str(data['weight']), True, (255, 105, 180))  # Pink
            self.screen.blit(weight_surf, weight_pos)

        for node in self.graph.nodes():
            x, y = self.scale(self.pos[node])
            color = (255, 0, 0) if node == start else (0, 255, 0) if node == end else (50, 150, 255)
            pygame.draw.circle(self.screen, color, (x, y), radius)
            font = pygame.font.SysFont(None, int(24 * self.zoom_level))
            img = font.render(str(node), True, (255, 255, 255))
            self.screen.blit(img, (x - radius // 2, y - radius // 2))

    def scale(self, pos):
        x, y = pos
        return (
            int(x * self.zoom_level * 800 + self.offset_x),
            int(y * self.zoom_level * 500 + self.offset_y)
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.dragging = True
                self.last_mouse_pos = pygame.mouse.get_pos()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                last_x, last_y = self.last_mouse_pos
                dx = mouse_x - last_x
                dy = mouse_y - last_y
                self.offset_x += dx
                self.offset_y += dy
                self.last_mouse_pos = (mouse_x, mouse_y)

        elif event.type == pygame.MOUSEWHEEL:
            old_zoom = self.zoom_level
            if event.y > 0:
                self.zoom_level *= 1.1
            elif event.y < 0:
                self.zoom_level /= 1.1
            self.zoom_level = max(0.3, min(self.zoom_level, 5))

            # Zoom to mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            scale_factor = self.zoom_level / old_zoom
            self.offset_x = mouse_x - scale_factor * (mouse_x - self.offset_x)
            self.offset_y = mouse_y - scale_factor * (mouse_y - self.offset_y)
