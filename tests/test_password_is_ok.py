import pytest

from password_checker import password_is_ok

def test_password_is_ok():

    assert password_is_ok("") == False

    assert password_is_ok("All1!") == False

    assert password_is_ok("ALLENALL!1") == True

    assert password_is_ok("allenall1!") == True

    assert password_is_ok("AllenAll!") == True

    assert password_is_ok("AllenAll1") == True