import requests
import json
import re

# we'll use Naver spell checker
base_url = 'https://m.search.naver.com/p/csearch/ocontent/spellchecker.nhn'
_agent = requests.Session()


def remove_tag(text):
    text = re.sub('<.+?>', '', text, 0, re.I|re.S)
    return text


def proofread(text):
    """
    This function checks the spelling and grammer of korean text,
    and proofreads it.
    """

    # Max length of text is 500
    if len(text) > 500:
        return text
    
    payload = {
        '_callback': 'window.__jindo2_callback._spellingCheck_0',
        'q': text
    }
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'referer': 'https://search.naver.com/'
    }

    # Get response
    r = _agent.get(base_url, params=payload, headers = headers)
    r = r.text[len(payload['_callback'])+1:-2]

    data = json.loads(r)
    html = data['message']['result']['html']

    # Remove <span> tag
    result = remove_tag(html)
    
    return result


if __name__ == '__main__':
    
    print(proofread("크기도너무작지도 크지도않아서그립감도좋고 작동도 너무잘되네용 ㅎㅎ"))