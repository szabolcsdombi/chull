chull
-----

convex hull from points

.. code::

    pip install chull

- `Documentation <https://chull.readthedocs.io/>`_
- `chull on Github <https://github.com/szabolcsdombi/chull/>`_
- `chull on PyPI <https://pypi.org/project/chull/>`_

.. py:method:: chull.make_hull(points: Vertices[N, 3]) -> Tuple[Vertices[N, 3], Normals[N, 3]]

Returns vertices and normals suitable for rendering.

.. code-block::

    points = np.array([
        ...
    ])

    vertices, normals = chull.make_hull(points)
