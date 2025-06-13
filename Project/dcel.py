from shapely.geometry import Point, Polygon
import numpy as np

class Vertex:
    def __init__(self, x, y):
        self.point = Point(x, y)
        self.incident_edge: tuple[Point, Point] = [self.point, None] 

class HalfEdge:
    def __init__(self, next_edge=None, prev_edge=None):
        self.origin: Point = None         # Vertex at the origin of this half-edge
        self.twin: tuple[Point, Point] = None
        self.incident_face = None  
        self.next = next_edge
        self.prev = prev_edge

    

class Face:
    def __init__(self, boundary_points=None):
        self.outer_component: tuple[Point, Point] = None
        self.inner_component: tuple[Point, Point] = None

        if boundary_points:
            self.polygon: Polygon = Polygon(boundary_points)
        else:
            self.polygon: Polygon = None


class DCEL:
    def __init__(self):
        self.vertices: list[Vertex] = []
        self.half_edges: list[HalfEdge] = []
        self.faces: list[Face] = []

    def add_vertex(self, x, y):
        vertex = Vertex(x, y)
        self.vertices.append(vertex)
        return vertex
    
    def add_half_edge(self):
        half_edge = HalfEdge()
        self.half_edges.append(half_edge)
        return half_edge
    
    def add_face(self, boundary_points=None):
        face = Face(boundary_points)
        self.faces.append(face)
        return face


