import time
import pytest
from game_info import GameInfo


@pytest.fixture
def game_info():
    return GameInfo()


def test_init(game_info):
    assert game_info.level == 1
    assert not game_info.started
    assert game_info.level_start_time == 0


def test_next_level(game_info):
    game_info.next_level()
    assert game_info.level == 2
    assert not game_info.started
    assert game_info.level_start_time == 0


def test_reset(game_info):
    game_info.level = 5
    game_info.started = True
    game_info.level_start_time = time.time()

    game_info.reset()
    assert game_info.level == 1
    assert not game_info.started
    assert game_info.level_start_time == 0


def test_game_finished(game_info):
    game_info.level = GameInfo.LEVELS + 1
    assert game_info.game_finished() == True

    game_info.level = GameInfo.LEVELS
    assert game_info.game_finished() == False


def test_start_level(game_info):
    game_info.start_level()
    assert game_info.started == True
    assert game_info.level_start_time > 0


def test_get_level_time(game_info):
    game_info.start_level()
    time.sleep(1)
    assert game_info.get_level_time() == 1
