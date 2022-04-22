import numpy as np
from scipy.spatial import ConvexHull


def make_hull(points):
    hull = ConvexHull(points)
    vertices = hull.points[hull.simplices]
    normals = np.cross(vertices[:, 0] - vertices[:, 1], vertices[:, 0] - vertices[:, 2])
    sign = np.sign(np.sum(vertices[:, 0] * normals, axis=1))
    flipped = np.where(sign < 0.0)
    vertices[flipped] = vertices[flipped, ::-1]
    normals = (normals.T / np.sqrt(np.sum(normals * normals, axis=1)) * sign).T
    vertices = vertices.reshape(-1, 3)
    normals = np.repeat(normals, 3, axis=0)
    return vertices, normals
