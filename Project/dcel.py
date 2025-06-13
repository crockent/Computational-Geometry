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
        self.outer_component = []    # One of the half-edges bordering the face
        if boundary_points:
            self.polygon = Polygon(boundary_points)
        else:
            self.polygon = None

class DCEL:
    def __init__(self):
        self.vertices = []
        self.half_edges = []
        self.faces = []


