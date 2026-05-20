from game.shoot import Bullet, BulletManager, bullet_hits, player_hits
from game.obstacle import Obstacle
from game.player import Player
from game.log import clear, events


class TestShoot:
    def test_bullet_moves_up(self):
        b = Bullet(x=200.0, y=340.0)
        b.y -= 8
        assert b.y == 332.0

    def test_bullet_culled_at_top(self):
        clear()
        mgr = BulletManager()
        mgr.fire(200.0, -20.0)
        mgr.update()
        mgr.cull()
        culled = [e for e in events() if e["type"] == "bullet_culled"]
        assert len(culled) == 1

    def test_bullet_hits_obstacle(self):
        bul = Bullet(x=100.0, y=50.0)
        obs = Obstacle(x=100.0, y=50.0, radius=10, speed=1)
        assert bullet_hits(bul, obs) is True

    def test_bullet_misses_obstacle(self):
        bul = Bullet(x=0.0, y=0.0)
        obs = Obstacle(x=200.0, y=200.0, radius=10, speed=1)
        assert bullet_hits(bul, obs) is False

    def test_player_hits_obstacle(self):
        p = Player(x=200.0, y=370.0)
        obs = Obstacle(x=200.0, y=370.0, radius=30, speed=1)
        assert player_hits(p, obs) is True

    def test_player_not_hit_by_far_obstacle(self):
        p = Player(x=200.0, y=370.0)
        obs = Obstacle(x=0.0, y=0.0, radius=10, speed=1)
        assert player_hits(p, obs) is False
