from unittest.mock import Mock

from game.player import Player


class TestPlayer:
    def test_initial_position(self):
        p = Player(x=200, y=350)
        assert p.x == 200
        assert p.y == 350

    def test_move_left(self):
        p = Player(x=200, y=350)
        p.move_left()
        assert p.x == 195

    def test_move_right(self):
        p = Player(x=200, y=350)
        p.move_right()
        assert p.x == 205

    def test_clamp_left(self):
        p = Player(x=2, y=350)
        p.move_left()
        assert p.x == 0

    def test_clamp_right(self):
        p = Player(x=398, y=350)
        p.move_right()
        assert p.x == 400

    def test_draw_creates_polygon(self):
        p = Player(x=200, y=350)
        canvas = Mock()
        p.draw(canvas)
        assert canvas.create_polygon.call_count >= 1
