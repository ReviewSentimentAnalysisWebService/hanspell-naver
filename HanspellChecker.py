import requests
import json
import re


class HanspellChecker:

    def __init__(self):
         # we'll use Naver spell checker
        self.base_url = 'https://m.search.naver.com/p/csearch/ocontent/spellchecker.nhn'
        self.headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'referer': 'https://search.naver.com/'
        }

        self._agent = requests.Session()


    def remove_tag(self, text):
        text = re.sub('<.+?>', '', text, 0, re.I|re.S)
        return text


    def correct(self, text):
        """
        This function checks the spelling and grammer of korean text,
        and corrects it.
        """

        if isinstance(text, list):
            result = []
            for item in text:
                corrected = self.correct(item)
                result.append(corrected)
            return result

        # Max length of text is 500
        if len(text) > 500:
            return text
        
        payload = {
            '_callback': 'window.__jindo2_callback._spellingCheck_0',
            'q': text
        }

        # Get response
        r = self._agent.get(self.base_url, params=payload, headers = self.headers)
        r = r.text[len(payload['_callback'])+1:-2]

        data = json.loads(r)
        html = data['message']['result']['html']

        # Remove <span> tag in the response
        result = self.remove_tag(html)
        
        return result


if __name__ == '__main__':
    
    checker = HanspellChecker()

    print(checker.correct("안녕하세여. 자연어처리는 넘 어려워용"))
