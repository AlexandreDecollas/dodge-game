from game.obstacle import Obstacle, ObstacleManager
from game.log import clear, events


class TestObstacle:
    def test_small_size(self):
        o = Obstacle(x=100.0, y=0.0, radius=10, speed=3)
        assert o.radius == 10
        assert o.speed == 3

    def test_medium_size(self):
        o = Obstacle(x=100.0, y=0.0, radius=20, speed=2)
        assert o.radius == 20
        assert o.speed == 2

    def test_large_size(self):
        o = Obstacle(x=100.0, y=0.0, radius=30, speed=1)
        assert o.radius == 30
        assert o.speed == 1

    def test_fall_speed(self):
        o = Obstacle(x=100.0, y=0.0, radius=10, speed=3)
        o.y += o.speed
        assert o.y == 3.0

    def test_manager_spawn_adds_obstacle(self):
        clear()
        mgr = ObstacleManager(seed=42)
        mgr.spawn(canvas_width=400)
        spawned = [e for e in events() if e["type"] == "obstacle_spawned"]
        assert len(spawned) == 1
        assert spawned[0]["radius"] in (10, 20, 30)

    def test_seed_reproducibility(self):
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

    def test_off_screen_culled(self):
        clear()
        mgr = ObstacleManager(seed=42, canvas_height=400)
        mgr.spawn(canvas_width=400)
        mgr.obstacles[0].y = 430.0
        mgr.update()
        culled = [e for e in events() if e["type"] == "obstacle_culled"]
        assert len(culled) == 1
