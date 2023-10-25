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


known_artists = types.SimpleNamespace()
known_artists.chris_tucci = types.SimpleNamespace(name='Chris Tucci', artist_id=1878272)
known_artists.dave_edson = types.SimpleNamespace(name='Dave Edson', artist_id=2625984)
known_artists.feodor_chin = types.SimpleNamespace(name='Feodor Chin', artist_id=2027455)
known_artists.jessica_rau = types.SimpleNamespace(name='Jessica Rau', artist_id=1874204)
known_artists.joshua_johnson = types.SimpleNamespace(name='Joshua Johnson', artist_id=1875608)
known_artists.kym_miller = types.SimpleNamespace(name='Kym Miller', artist_id=2625985)
known_artists.marion_toro = types.SimpleNamespace(name='Marion Toro', artist_id=2362948)
