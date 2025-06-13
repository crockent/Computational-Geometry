from shapely.geometry import Point, Polygon
import numpy as np

class Vertex:
    def __init__(self, x, y):
        self.point = Point(x, y)
        self.incident_edge = None  # One of the half-edges emanating from the vertex

class HalfEdge:
    def __init__(self):
        self.origin = None         # Vertex at the origin of this half-edge
        self.twin = None           # Twin half-edge (opposite direction)
        self.incident_face = None  # Face to the left of the half-edge
        self.next = None           # Next half-edge around the face
        self.prev = None           # Previous half-edge around the face

class Face:
    def __init__(self, boundary_points=None):
        self.outer_component = []    
        self.inner_component = []
        if boundary_points:
            self.polygon: Optional[Polygon] = Polygon(boundary_points)
        else:
            self.polygon: Optional[Polygon] = None


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


