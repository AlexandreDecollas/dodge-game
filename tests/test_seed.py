from game.obstacle import ObstacleManager
from game.log import clear, events


class TestSeed:
    def test_same_seed_same_obstacles(self):
        clear()
        mgr1 = ObstacleManager(seed=42)
        for _ in range(10):
            mgr1.spawn(canvas_width=400)
        positions1 = [(e["x"], e["radius"]) for e in events() if e["type"] == "obstacle_spawned"]

        clear()
        mgr2 = ObstacleManager(seed=42)
        for _ in range(10):
            mgr2.spawn(canvas_width=400)
        positions2 = [(e["x"], e["radius"]) for e in events() if e["type"] == "obstacle_spawned"]

        assert positions1 == positions2

    def test_different_seed_different_obstacles(self):
        clear()
        mgr1 = ObstacleManager(seed=42)
        for _ in range(5):
            mgr1.spawn(canvas_width=400)
        positions1 = [(e["x"], e["radius"]) for e in events() if e["type"] == "obstacle_spawned"]

        clear()
        mgr2 = ObstacleManager(seed=99)
        for _ in range(5):
            mgr2.spawn(canvas_width=400)
        positions2 = [(e["x"], e["radius"]) for e in events() if e["type"] == "obstacle_spawned"]

        assert positions1 != positions2
