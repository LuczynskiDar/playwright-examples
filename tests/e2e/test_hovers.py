
import pytest


@pytest.mark.parametrize("user_index, expected_username", [
    (0, "name: user1"),
    (1, "name: user2"),
    (2, "name: user3"),
])
def test_hover_shows_username(hovers_page, user_index, expected_username):
    hovers_page.navigate("https://the-internet.herokuapp.com/hovers")
    hovers_page.hover_over(user_index)
    username = hovers_page.get_caption(user_index)
    assert username == expected_username