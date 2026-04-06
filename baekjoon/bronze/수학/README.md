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
- 🛠 사용: `while`문, 정수 덧셈, 누적합, 