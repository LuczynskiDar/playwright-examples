
import pytest


def test_alert_accepted(alerts_page):
    alerts_page.navigate("https://the-internet.herokuapp.com/javascript_alerts")
    alerts_page.trigger_alert()
    assert alerts_page.get_result_text() == "You successfully clicked an alert"
    
@pytest.mark.parametrize("action, expected_result", [
    ("accept", "You clicked: Ok"),
    ("dismiss", "You clicked: Cancel"),])
def test_confirm(alerts_page, action, expected_result):
    alerts_page.navigate("https://the-internet.herokuapp.com/javascript_alerts")
    alerts_page.trigger_confirm(action)
    assert alerts_page.get_result_text() == expected_result
    
def test_prompt(alerts_page):
    input_test = "Test Prompt Input"
    alerts_page.navigate("https://the-internet.herokuapp.com/javascript_alerts")
    alerts_page.trigger_prompt(input_test)
    assert alerts_page.get_result_text() == f"You entered: {input_test}"