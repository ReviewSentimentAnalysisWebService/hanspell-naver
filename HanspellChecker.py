import requests
import json
import re
import time
from requests.exceptions import HTTPError


class HanspellChecker:

    def __init__(self):
         # we'll use Naver spell checker
        self.base_url = 'https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy'
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
        
        params = {
            'q': text,
            'color_blindness': 0
        }

        # Get response
        success = False
        try_cnt = 0
        while success == False:
            try:
                r = self._agent.get(self.base_url, params=params)
                try_cnt += 1
                res_code = r.status_code
                if res_code != 200:  # response 200 means 'The request has succeeded'
                    if try_cnt >= 3:
                        return text
                    raise HTTPError
            except HTTPError:
                print("[!] An error occurred while sending the request. error code: {}".format(res_code))
                print("[-] Waiting 5 seconds before resending the request...")
                time.sleep(5)
            else:
                success = True
                
        r = r.text  # change bytestring to string
        data = json.loads(r)
        html = data['message']['result']['html']

        # Remove html tag in the response
        result = self.remove_tag(html)
        
        return result


if __name__ == '__main__':
    
    checker = HanspellChecker()
    print(checker.correct("안녕하세여. 자연어처리는 넘 어려워용."))
