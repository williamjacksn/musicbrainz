import lxml.html
import requests
import types


def get_session(username: str, password: str) -> requests.Session:
    s = requests.session()

    # get login page
    login_url = 'https://musicbrainz.org/login'
    resp = s.get(login_url)
    resp.raise_for_status()
    doc = lxml.html.document_fromstring(resp.content)

    el = doc.cssselect('input[name=csrf_session_key]')[0]
    csrf_session_key = el.get('value')

    el = doc.cssselect('input[name=csrf_token]')[0]
    csrf_token = el.get('value')

    # send login
    login_payload = {
        'csrf_session_key': csrf_session_key,
        'csrf_token': csrf_token,
        'password': password,
        'remember_me': 1,
        'username': username,
    }
    resp = s.post(login_url, data=login_payload)
    resp.raise_for_status()
    return s
