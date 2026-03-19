# sys module

## 1. Overview
`sys`는 파이썬 인터프리터와 실행 환경에 접근하기 위한 표준 모듈이다.  
입출력 제어, 프로그램 종료, 명령줄 인자 확인, 재귀 제한 설정 등 실행 환경과 가까운 기능을 제공한다.

---

## 2. Why it matters
알고리즘 문제 풀이에서는 빠른 입력과 재귀 제한 설정 때문에 자주 사용된다.  
또한 프로그램을 조기에 종료하거나 실행 환경 정보를 확인할 때도 유용하다.

---

## 3. Key APIs

### 3.1 `sys.stdin.readline()`

- **역할**: 빠른 입력 처리
- **왜 사용하나**: `input()`은 내부적으로 추가 처리(공백 제거, 변환 등)를 수행하지만,
  `sys.stdin.readline()`은 단순히 문자열을 읽기 때문에 더 빠름
- **특징**
  - 입력 끝에 `\n`이 포함됨
  - 보통 `strip()`과 함께 사용
- **주의점**
  - 문자열 그대로 들어오므로 필요하면 형변환 필요

#### Code
```python
import sys
input = sys.stdin.readline

name = input().strip()
print(name)
```

#### Output
```text
(입력값에 따라 달라짐)
```

---

### 3.2 `sys.stdout.write()`

- **역할**: 표준 출력에 문자열 직접 쓰기
- **왜 사용하나**: 
    - 출력 형식을 직접 제어하거나 출력 횟수가 많을 때 성능을 개선하기 위해 사용
- **특징**
  - 자동 줄바꿈 없음
  - 문자열만 출력 가능
- **주의점**
  - 숫자를 출력하려면 `str()`로 변환해야 함

#### Code
```python
import sys

sys.stdout.write("Hello")
sys.stdout.write("World")
```

#### Output
```text
HelloWorld
```

#### Code
```python
import sys

sys.stdout.write("Hello\n")
sys.stdout.write("World")
```

#### Output
```text
Hello
World
```

---

### 3.3 `sys.exit()`

- **역할**: 프로그램 종료
- **왜 사용하나**
    - 특정 조건에서 더 이상 실행할 필요가 없거나
    - 중첩된 반복문 등 복잡한 흐름에서 즉시 프로그램을 종료하기 위해 사용
- **특징**
  - 이후 코드는 실행되지 않음
  - 내부적으로 `SystemExit` 예외를 발생시킴
  - 종료 코드를 전달할 수 있음
- **주의점**
  - 남용하면 코드 흐름이 복잡해질 수 있음

#### Code
```python
import sys

number = int(input())

if number < 0:
    print("잘못된 입력")
    sys.exit()

print("정상 실행")
```

#### Code
```python
import sys

try:
    sys.exit()
except SystemExit:
    print("SystemExit caught")
```

#### Output
```text
SystemExit caught
```

---

### 3.4 `sys.argv`

- **역할**: 명령줄 인자 확인
- **왜 사용하나**: 파일 실행 시 전달한 값들을 프로그램 안에서 사용하기 위해
- **특징**
  - 첫 번째 원소는 보통 파일명
- **주의점**
  - 입력값 검증이 필요할 수 있음

#### Code
```python
import sys

print(sys.argv)
```

#### Output
```text
예 : ['test.py', 'arg1']
```

---

### 3.5 `sys.setrecursionlimit()`

- **역할**: 재귀 호출 가능 깊이 조정
- **왜 사용하나**: DFS, 트리 탐색 등 재귀가 깊어질 수 있는 문제에서 `RecursionError`를 방지하기 위해
- **주의점**
  - 너무 크게 설정하면 메모리 사용량이 커질 수 있음

#### Code
```python
import sys

sys.setrecursionlimit(10**6)
```

---

## 4. Comparison

### `print()` vs `sys.stdout.write()`

| 항목 | `print()` | `sys.stdout.write()` |
|---|---|---|
| 속도 | 보통 | 더 빠름 |
| 줄바꿈 | 자동 | 직접 추가 |
| 출력 타입 | 여러 타입 가능 | 문자열만 가능 |
| 내부 동작 | 포맷팅 포함 | 단순 문자열 출력 |
| 사용 편의성 | 높음 | 낮음 |
| 출력 제어 | 비교적 단순 | 더 직접적 |

### `break` vs `sys.exit()`

| 항목 | `break` | `sys.exit()` |
|---|---|---|
| 반복문 탈출 | O | 가능 |
| 프로그램 전체 종료 | X | O |

---

## 5. When to use

- 입력 데이터가 많고 성능이 중요한 경우 → `sys.stdin.readline()`
- 출력 형식을 직접 제어하거나 출력이 많은 경우 → `sys.stdout.write()`
- 특정 조건에서 즉시 프로그램을 종료해야 하는 경우 → `sys.exit()`
- 실행 시 전달된 인자를 처리해야 하는 경우 → `sys.argv`
- 재귀 깊이가 깊은 문제(DFS 등)를 해결할 때 → `sys.setrecursionlimit()`

---

## 6. Summary
`sys`는 파이썬 실행 환경과 직접 연결되는 표준 모듈이다.  
특히 코딩테스트에서는 빠른 입력 처리, 재귀 깊이 설정, 조건 기반 조기 종료를 위해 필수적으로 사용된다.