# hanspell-naver
네이버 맞춤법 검사기를 이용한 문장 교정 라이브러리입니다.

### 필요 라이브러리
- `requests`
- `json`

### 사용법
HanspellChecker의 `correct('교정할 문장')` 메서드로 문장을 교정할 수 있습니다. correct()의 인자로 리스트 타입도 지원합니다.

```python
from HanspellChecker import HanspellChecker


checker = HanspellChecker()

print(checker.correct("안녕하세여. 자연어처리는 넘 어려워용."))

# list 형태의 입력도 가능합니다.
text_list = [
    "솔직히 쟤보다 내가 더 낟다",
    "그러면 안돼지!",
    "맛춤뻡좀지킵시당",
]
print(checker.correct(text_list))
```
