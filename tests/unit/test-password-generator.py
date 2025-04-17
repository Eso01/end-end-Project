from src.main import generate_password

def test_password_length():
    """Test that generated password has correct length"""
    length = 12
    special = 2
    numbers = 2
    password = generate_password(length, special, numbers)
    assert len(password) == length

def test_password_contains_special_chars():
    """Test password contains required special characters"""
    from string import punctuation
    password = generate_password(12, 3, 0)
    assert any(char in punctuation for char in password)

def test_password_contains_numbers():
    """Test password contains required numbers"""
    from string import digits
    password = generate_password(12, 0, 3)
    assert any(char in digits for char in password)
