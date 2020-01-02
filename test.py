import os
os.environ['PYTEST_RUNNING'] = 'true'
import hug
import putongwords

#
# Test if file parsing is correct


def test_parse_simple():
    result = hug.test.get(putongwords, '/a')
    assert result.headers_dict['location'] == 'https://a.com'


def test_parse_leading_slash():
    result = hug.test.get(putongwords, '/b')
    assert result.headers_dict['location'] == 'https://b.com'


def test_parse_trailing_slash():
    result = hug.test.get(putongwords, '/c')
    assert result.headers_dict['location'] == 'https://c.com'


def test_parse_slash_on_both_ends():
    result = hug.test.get(putongwords, '/d')
    assert result.headers_dict['location'] == 'https://d.com'


def test_parse_leading_double_slash():
    result = hug.test.get(putongwords, '/e')
    assert result.headers_dict['location'] == 'https://e.com'


def test_parse_trailing_double_slash():
    result = hug.test.get(putongwords, '/f')
    assert result.headers_dict['location'] == 'https://f.com'


def test_parse_double_slash_on_both_ends():
    result = hug.test.get(putongwords, '/g')
    assert result.headers_dict['location'] == 'https://g.com'


#
# Test if user-input parsing is correct


def test_userinput_simple():
    result = hug.test.get(putongwords, '/a')
    assert result.headers_dict['location'] == 'https://a.com'


def test_userinput_double_leading_slash():
    result = hug.test.get(putongwords, '//a')
    assert result.headers_dict['location'] == 'https://a.com'


def test_userinput_many_leading_slash():
    result = hug.test.get(putongwords, '/////a')
    assert result.headers_dict['location'] == 'https://a.com'


def test_userinput_trailing_slash():
    result = hug.test.get(putongwords, '/a/')
    assert result.headers_dict['location'] == 'https://a.com'


def test_userinput_double_trailing_slash():
    result = hug.test.get(putongwords, '/a//')
    assert result.headers_dict['location'] == 'https://a.com'


def test_userinput_many_trailing_slash():
    result = hug.test.get(putongwords, '/a////')
    assert result.headers_dict['location'] == 'https://a.com'


#
# Test for input with params


def test_param_simple():
    result = hug.test.get(putongwords, '/a/b')
    assert result.headers_dict['location'] == 'https://a.com/b'


def test_param_multiple():
    result = hug.test.get(putongwords, '/a/b/c')
    assert result.headers_dict['location'] == 'https://a.com/b/c'


def test_param_multiple_fixed():
    result = hug.test.get(putongwords, '/a/b/d')
    assert result.headers_dict['location'] == 'https://a.com/b/fixed/d'
