# map()

## 1. Overview
여러 iterable의 요소에 함수를 적용하여 새로운 iterator를 반환하는 함수

---

## 2. Syntax
```python
map(function, iterable, ...)
```

---

## 3. Parameters

| 파라미터 | 설명 |
|---|---|
| function | 각 요소에 적용할 함수 |
| iterable | 순회 가능한 객체 (list, tuple 등) |

---

## 4. Return Value

| 타입 | 설명 |
|---|---|
| map object (iterator) | 결과를 바로 반환하지 않고 iterator 형태로 반환 |

---

## 5. Example

#### Code
```python
arr = [1, 2, 3]
result = map(lambda x: x * 2, arr)

print(list(result))
```

#### Output
```text
[2, 4, 6]
```

---

## 6. Key Points

- 결과는 iterator이므로 `list()` 또는 `tuple()`로 변환해야 확인 가능
- 여러 iterable을 동시에 처리 가능
- lambda와 함께 자주 사용됨

---

## 7. Time Complexity

- O(n)

---

## 8. Pitfalls (주의할 점)

- `map` 객체는 한 번 순회하면 재사용 불가능
- 출력하려면 반드시 `list()`로 감싸야 함

---

## 9. When to use

- 리스트의 모든 요소에 동일한 연산을 적용할 때
- 입력값을 빠르게 변환할 때 (`map(int, input().split())`)

---

## 10. Related

- lambda
- list comprehension