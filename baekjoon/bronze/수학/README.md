# ✅ Solved Problems

---

### 1. <수학> BOJ 2745 - 진법 변환  
- 🔗 문제: https://www.acmicpc.net/problem/2745  
- 📂 풀이: [README](./2745/README.md)  
- 💻 코드: [solution.py](./2745/solution.py)  
- 💡 핵심: 진법 수를 왼쪽부터 읽으며 누적 계산  
- 🛠 사용: 문자열 순회, `isdigit()`, `ord()`, 진법 변환

---

### 2. <수학> BOJ 11005 - 진법 변환 2  
- 🔗 문제: https://www.acmicpc.net/problem/11005  
- 📂 풀이: [README](./11005/README.md)  
- 💻 코드: [solution.py](./11005/solution.py)  
- 💡 핵심: 10진수를 `B`로 계속 나누며 나머지를 구해 `B`진수로 변환  
- 🛠 사용: `%`, `//`, `reversed()`, `join()`, `chr()`, `ord()`

---

### 3. <수학> BOJ 2720 - 세탁소 사장 동혁  
- 🔗 문제: https://www.acmicpc.net/problem/2720  
- 📂 풀이: [README](./2720/README.md)  
- 💻 코드: [solution.py](./2720/solution.py)  
- 💡 핵심: 큰 단위 동전부터 차례대로 개수를 구해 거스름돈을 계산 (그리디 알고리즘)  
- 🛠 사용: 정수 단위 계산, `divmod()`, 튜플 반환, 언패킹

---

### 4. <수학> BOJ 2903 - 중앙 이동 알고리즘  
- 🔗 문제: https://www.acmicpc.net/problem/2903  
- 📂 풀이: [README](./2903/README.md)  
- 💻 코드: [solution.py](./2903/solution.py)  
- 💡 핵심: 한 변의 점 개수 규칙을 찾아 전체 점 개수를 계산  
- 🛠 사용: 거듭제곱, 정수 계산, 점화식 아이디어

---

### 5. <수학> BOJ 2292 - 벌집  
- 🔗 문제: https://www.acmicpc.net/problem/2292  
- 📂 풀이: [README](./2292/README.md)  
- 💻 코드: [solution.py](./2292/solution.py)  
- 💡 핵심: 벌집의 각 층 마지막 번호를 누적해서 N이 속한 층 찾기  
- 🛠 사용: `while`문, 정수 덧셈, 누적합

---

### 6. <수학> BOJ 2869 - 달팽이는 올라가고 싶다  
- 🔗 문제: https://www.acmicpc.net/problem/2869  
- 📂 풀이: [README](./2869/README.md)  
- 💻 코드: [solution.py](./2869/solution.py)  
- 💡 핵심: 마지막 날은 미끄러지지 않는다는 점을 이용해 날짜를 수식으로 계산  
- 🛠 사용: 정수 나눗셈, 올림 계산, 수식 변환

---

### 7. <수학> BOJ 2501 - 약수 구하기  
- 🔗 문제: https://www.acmicpc.net/problem/2501  
- 📂 풀이: [README](./2501/README.md)  
- 💻 코드: [solution.py](./2501/solution.py)  
- 💡 핵심: 약수를 작은 수부터 차례대로 찾으면서 'K'번째 약수를 판별
- 🛠 사용: `for`문, 나머지 연산, 조건문, 카운트

---

### 8. <수학> BOJ 9506 - 약수들의 합  
- 🔗 문제: https://www.acmicpc.net/problem/9506  
- 📂 풀이: [README](./9506/README.md)  
- 💻 코드: [solution.py](./9506/solution.py)  
- 💡 핵심: 자기 자신을 제외한 약수들을 구해 합을 비교하고, 완전수이면 주어진 출력 형식에 맞게 표현
- 🛠 사용: 반복문, 나머지 연산, 리스트, 누적합, 조건문, 문자열 출력 처리