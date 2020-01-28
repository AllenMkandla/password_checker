import pytest

from password_checker import password_is_valid
#password is valid
def test_password_exists():
    with pytest.raises(Exception) as e:
        password_checker.password_is_valid("")
    str(e.value) == 'password does not exist'
def test_password_length():
    with pytest.raises(Exception) as e:
        password_checker.password_is_valid("All1!")
    str(e.value) == 'password does not exist'

def test_password_lowercase():
    with pytest.raises(Exception) as e:
        password_checker.password_is_valid("ALLENALL!1")
    str(e.value) == 'password should have at least one lowercase letter'
def test_password_uppercase():
    with pytest.raises(Exception,) as e:
        password_checker.password_is_valid("allenall1!")
    str(e.value) == 'password should have at least one uppercase letter'
def test_password_digit():
    with pytest.raises(Exception) as e: 
        password_checker.password_is_valid("AllenAll!")
    str(e.value) == 'password should at least have one digit'
def test_password_character():
    with pytest.raises(Exception) as e:
        password_checker.password_is_valid("AllenAll1")
    str(e.value) == 'password should have at least one special character'
