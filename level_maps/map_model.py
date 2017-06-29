import os


class MapTemplate(object):
    MAP_COORDINATES = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
                       (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1),
                       (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
                       (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3),
                       (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4),
                       (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)]


class Maps(MapTemplate):


    MAP_LEVEL_00 = {'nav_map': [(1), (1), (1), (1), (7), (1),
                                (1), (0), (0), (0), (0), (1),
                                (1), (0), (0), (1), (1), (1),
                                (1), (0), (0), (1), (1), (0),
                                (1), (0), (0), (0), (0), (0),
                                (1), (9), (1), (1), (2), (2)],
                    'items_map': [(1), (1), (1), (1), (9), (1),
                                  (1), (0), (0), (0), (0), (1),
                                  (1), (0), (0), (1), (1), (1),
                                  (10), (0), (0), (1), (1), (0),
                                  (10), (0), (0), (8), (0), (0),
                                  (1), (9), (1), (1), (2), (2)]}

    MAP_LEVEL_01 = [(1), (1), (1), (7), (1), (1),
                    (0), (0), (0), (0), (1), (1),
                    (0), (1), (1), (0), (0), (0),
                    (0), (1), (1), (0), (0), (0),
                    (0), (0), (1), (0), (1), (1),
                    (0), (0), (1), (7), (1), (1)]
