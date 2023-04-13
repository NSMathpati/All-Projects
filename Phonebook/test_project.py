from phonebook import checknumber

def test_check_number():
    assert checknumber("+14155552656") == True
    assert checknumber("+917901568900") == True
    assert checknumber("123") == False
    assert checknumber("") == False


