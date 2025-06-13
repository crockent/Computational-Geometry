from dcel import DCEL, Vertex, HalfEdge, Face

def build_irregular_decagon_dcel():
    dcel = DCEL()

    # Irregular decagon (10 vertices, non-symmetric)
    points = [
        (0, 0), (2, 0.5), (3, 1.5), (3.2, 3), (2.5, 4.2),
        (1.5, 5), (0.2, 4.5), (-0.5, 3.2), (-0.2, 1.8), (0.5, 0.8)
    ]
    vertices = [Vertex(x, y) for x, y in points]
    dcel.vertices.extend(vertices)

    # Create half-edges (10 edges + 10 twins)
    half_edges = [HalfEdge() for _ in range(10)]
    twins = [HalfEdge() for _ in range(10)]
    dcel.half_edges.extend(half_edges + twins)

    # Set origins for half-edges and twins
    for i in range(10):
        half_edges[i].origin = vertices[i]
        twins[i].origin = vertices[(i + 1) % 10]

    # Set twins
    for i in range(10):
        half_edges[i].twin = twins[i]
        twins[i].twin = half_edges[i]

    # Set next and prev for the face
    for i in range(10):
        half_edges[i].next = half_edges[(i + 1) % 10]
        half_edges[i].prev = half_edges[(i - 1) % 10]

    # Set next and prev for the twins (outside face)
    for i in range(10):
        twins[i].next = twins[(i - 1) % 10]
        twins[i].prev = twins[(i + 1) % 10]

    # Create face for the decagon
    face = Face(boundary_points=points)
    dcel.faces.append(face)

    # Assign incident face and outer component
    for e in half_edges:
        e.incident_face = face
    face.outer_component = half_edges[0]

    # Optionally, assign incident_face for twins (usually the "outside" face, can be None)
    for t in twins:
        t.incident_face = None

    # Set incident_edge for vertices
    for i, v in enumerate(vertices):
        v.incident_edge = half_edges[i]

    return dcel

def test_irregular_decagon_dcel():
    dcel = build_irregular_decagon_dcel()

    # Expected values
    expected_vertices = 10
    expected_half_edges = 20  # 10 edges + 10 twins
    expected_faces = 1

    assert len(dcel.vertices) == expected_vertices, "Vertex count mismatch"
    assert len(dcel.half_edges) == expected_half_edges, "Half-edge count mismatch"
    assert len(dcel.faces) == expected_faces, "Face count mismatch"

    # Check vertex coordinates
    coords = sorted([(v.point.x, v.point.y) for v in dcel.vertices])
    expected_coords = sorted([
        (0, 0), (2, 0.5), (3, 1.5), (3.2, 3), (2.5, 4.2),
        (1.5, 5), (0.2, 4.5), (-0.5, 3.2), (-0.2, 1.8), (0.5, 0.8)
    ])
    assert coords == expected_coords, "Vertex coordinates mismatch"

    # Check face polygon
    face = dcel.faces[0]
    assert face.polygon.is_valid, "Face polygon is invalid"
    # Area is not a round number, but should be positive
    assert face.polygon.area > 0, "Face area should be positive for a valid decagon"

    print("All DCEL irregular decagon tests passed.")

    



if __name__ == "__main__":
    test_irregular_decagon_dcel()