import pygame

class Button:
    def __init__(self, x, y, width, height, text, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback
        self.color = (70, 130, 180)
        self.hover_color = (100, 160, 210)
        self.font = pygame.font.SysFont(None, 24)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.callback()

### canvas.py
import pygame
import networkx as nx
import matplotlib.pyplot as plt

class Canvas:
    def __init__(self, screen):
        self.screen = screen
        self.graph = nx.Graph()
        self.pos = {}

    def load_graph(self, graph_data):
        self.graph.clear()
        self.pos.clear()
        self.graph.add_nodes_from(graph_data['nodes'])
        self.graph.add_weighted_edges_from(graph_data['edges'])
        self.pos = nx.spring_layout(self.graph, seed=42)

    def draw_graph(self, path=None, visited=None, start=None, end=None):
        self.screen.fill((25, 25, 25))
        radius = 20

        for edge in self.graph.edges(data=True):
            src, dst, data = edge
            color = (200, 200, 200)
            if path and (src, dst) in zip(path, path[1:]) or (dst, src) in zip(path, path[1:]):
                color = (255, 215, 0)
            elif visited and (src in visited and dst in visited):
                color = (100, 100, 255)
            pygame.draw.line(self.screen, color, self.scale(self.pos[src]), self.scale(self.pos[dst]), 4)

        for node in self.graph.nodes():
            x, y = self.scale(self.pos[node])
            color = (255, 0, 0) if node == start else (0, 255, 0) if node == end else (50, 150, 255)
            pygame.draw.circle(self.screen, color, (x, y), radius)
            font = pygame.font.SysFont(None, 24)
            img = font.render(str(node), True, (255, 255, 255))
            self.screen.blit(img, (x - 8, y - 8))

    def scale(self, pos):
        x, y = pos
        return int(x * 800 + 100), int(y * 500 + 80)