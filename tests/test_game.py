from unittest.mock import Mock
from game.obstacle import Obstacle
from game.log import clear, events
import main as game_module


def make_game():
    return game_module.Game(root=Mock(), canvas=Mock())


class TestGame:
    def test_game_initializes(self):
        clear()
        game = make_game()
        assert any(e["type"] == "game_init" for e in events())

    def test_game_over_on_player_hit(self):
        clear()
        game = make_game()
        game.obstacle_manager.obstacles.append(
            Obstacle(x=200, y=350, radius=30, speed=1)
        )
        game.tick()
        assert any(e["type"] == "game_over" for e in events())

    def test_restart_resets_game(self):
        clear()
        game = make_game()
        game.game_over()
        game.restart()
        assert any(e["type"] == "game_restart" for e in events())

    def test_score_tracks_seconds(self):
        clear()
        game = make_game()
        for _ in range(32):
            game.tick()
        tick_events = [e for e in events() if e["type"] == "tick"]
        assert tick_events[-1]["tick_count"] // 16 >= 2
