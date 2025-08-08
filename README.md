# 💡 알고리즘 코딩테스트 풀이, 코테 통과 드가자~

**comhappy**의 알고리즘 코딩테스트 문제 풀이 기록을 관리하는 공간. 백준, 프로그래머스, SWEA등 다양한 플랫폼의 문제 풀이

---

### 📂 디렉토리 구조

각 코딩테스트 플랫폼의 이름으로 디렉토리를 분류하여 문제 소스 코드를 관리합니다.

- **Baekjoon**
  - Gold
  - Silver
    - `1000.cpp`
  - Bronze
- **Programmers**
  - Level_1
    - `완주하지 못한 선수.cpp`
  - Level_2
- **SWEA**
  - D1
    - `2072.cpp`


- **Baekjoon**: 백준 온라인 저지(BOJ) 문제 풀이 코드
- **Programmers**: 프로그래머스 문제 풀이 코드
- **SWEA**: 삼성 SW Expert Academy 문제 풀이 코드

각 플랫폼 디렉토리 내부는 문제의 난이도나 유형에 따라 하위 디렉토리로 추가 분류될 수 있습니다.

---

### 푼 문제 목록 (Progress)

> ✨ 꾸준히 업데이트될 예정입니다.

####  Baekjoon Online Judge

| 문제 번호 | 문제 이름 | 난이도 | 풀이 언어 | 링크 |
| :--- | :--- | :---: | :---: | :---: |
| 1000 | A+B | Bronze V | C++ | [Link](https://www.acmicpc.net/problem/1000) |
| ... | ... | ... | ... | ... |

#### Programmers

| 레벨 | 문제 이름 | 풀이 언어 | 링크 |
| :---: | :--- | :---: | :---: |
| 1 | 완주하지 못한 선수 | C++ | [Link](https://school.programmers.co.kr/learn/courses/30/lessons/42576) |
| ... | ... | ... | ... |

#### SW Expert Academy

| 난이도 | 문제 번호 | 문제 이름 | 풀이 언어 | 링크 |
| :---: | :--- | :--- | :---: | :---: |
| D1 | 2072 | 홀수만 더하기 | C++ | [Link](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq) |
| ... | ... | ... | ... | ... |

---

### 🎯 목표

- **꾸준한 커밋**: 매일 최소 1시간이상 풀고 커밋하는 것을 목표로 합니다.
- **다양한 유형 정복**: 특정 유형에만 치우치지 않고, 다양한 알고리즘과 자료구조 문제를 해결합니다.
- **코드 리뷰 및 개선**: 단순히 문제를 푸는 것에서 그치지 않고, 더 효율적이고 가독성 좋은 코드를 작성하기 위해 꾸준히 리팩토링합니다.

---

### 💬 Commit Message Convention

커밋 메시지는 다음과 같은 형식을 따릅니다.

[플랫폼] 문제이름(문제번호) / 난이도


**예시)**

[Baekjoon] A+B(1000) / Bronze V
[Programmers] 완주하지 못한 선수 / Level 1


---

### 💻 사용 언어

- ** 주력 언어: `Java`, Python **
- 필요에 따라 `Python`, `Java` 등 다른 언어를 사용할 수 있습니다.





🤖 Notion 과제 자동화 스크립트
매일 쌓이는 과제와 실습 목록, 더 이상 손으로 정리하지 마세요! 이 스크립트는 텍스트 파일에 정리된 과제 목록을 AI를 이용해 자동으로 분석하고, 여러분의 Notion 데이터베이스에 깔끔하게 추가해주는 자동화 도구입니다.

📂 프로젝트 파일 구성
이 프로젝트는 3개의 핵심 파일로 구성되어 있습니다.

notion_automation.py: 메인 Python 스크립트

input.txt: 과제 내용을 입력하는 텍스트 파일

requirements.txt: 실행에 필요한 라이브러리 목록

✨ 주요 기능 및 특징
⚙️ 단순 반복 작업을 자동화하여 학습에 더 집중할 수 있도록 돕습니다.

AI 기반 자동 분석: Google의 Gemini API를 통해 input.txt에 있는 텍스트를 분석하여 제목, 과목, 날짜 등의 정보를 자동으로 추출합니다.

자동 데이터베이스 입력: 추출된 정보를 Notion API를 통해 지정된 데이터베이스에 자동으로 추가합니다.

간편한 입력 방식: 사용자는 복잡한 코드 수정 없이, 그날의 과제 내용을 input.txt 파일에 붙여넣기만 하면 됩니다.

⚙️ 설정 및 실행 순서
💡 처음 한 번만 설정하면 이후에는 5단계만 반복하면 됩니다.

1. 사전 준비
PC에 Python 3 버전이 설치되어 있어야 합니다. (python.org에서 다운로드)

2. 라이브러리 설치
터미널(또는 명령 프롬프트)을 열어 이 프로젝트 폴더로 이동한 뒤, 아래 명령어를 실행합니다.

Bash

pip install -r requirements.txt
3. API 키 및 데이터베이스 설정
Notion 설정

API 키 발급: Notion 통합 페이지에서 새 통합을 만들고 **내부 통합 토큰**을 복사합니다.

데이터베이스 생성: Notion에 새 페이지를 만들고 아래 표와 똑같은 속성으로 데이터베이스를 생성합니다.
| 속성 이름 | 속성 유형 |
| :--- | :--- |
| 제목 | 제목 (Title) |
| 과목 | 선택 (Select) |
| 구분 | 선택 (Select) |
| 날짜 | 날짜 (Date) |
| 사이트 | 선택 (Select) |
| 풀이여부 | 체크박스 (Checkbox) |
| 링크 | URL |

데이터베이스 연결: 생성한 데이터베이스의 ••• 메뉴 > + 연결 추가에서 1번에서 만든 통합(봇)을 초대합니다.

데이터베이스 ID 확인: 데이터베이스 URL(.../xxxxxxxx?v=...)에서 32자리의 데이터베이스 ID를 복사합니다.

Gemini API 키 생성

Google AI Studio에서 **Get API key**를 클릭하여 새로운 API 키를 생성하고 복사합니다.

4. 스크립트 정보 입력
notion_automation.py 파일을 열어 상단 설정 부분에 3단계에서 얻은 키와 ID를 붙여넣습니다.

Python

# --- 1. 설정: 이곳에 여러분의 정보를 입력하세요! ---
NOTION_API_KEY = "복사한 Notion API 키"
DATABASE_ID = "복사한 Notion 데이터베이스 ID"
GEMINI_API_KEY = "복사한 Gemini API 키"
5. 실행
input.txt 파일에 그날의 과제 내용을 붙여넣고 저장합니다.

터미널에서 아래 명령어를 실행합니다.

Bash

python notion_automation.py
🛠️ 사용 기술
Language: Python

APIs: Notion API, Google Gemini API


