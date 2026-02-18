## 📌 Linear Search in Python
### 🔎 Linear Search kya hota hai?

Linear Search ek **simple searching algorithm** hai jisme hum list ke elements ko **start se end tak ek-ek karke check** karte hain.

👉 Jab tak required element mil na jaye ya list khatam na ho jaye.

---

## 🧠 Algorithm (Step by Step)

1. Start
2. List aur target element input lo
3. i = 0 se n-1 tak loop chalao
4. Agar `arr[i] == target`
   → Position return karo
5. Agar loop khatam ho jaye aur element na mile
   → "Not Found" print karo
6. End

---

## 🧾 Python Program – Linear Search

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # element mil gaya

    return -1   # element nahi mila


# Example
numbers = [10, 25, 30, 45, 50]
key = 30

result = linear_search(numbers, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
```

---

## 🧩 Line by Line Explanation

```python
for i in range(len(arr)):
```

➡ List ke har element par loop chalega

```python
if arr[i] == target:
```

➡ Har element ko target se compare karega

```python
return i
```

➡ Match milte hi index return karega

```python
return -1
```

➡ Agar element na mile to -1 return karega

---

## ⏱ Time Complexity

* Best Case → **O(1)** (agar first position par mil jaye)
* Worst Case → **O(n)** (agar last me ho ya na mile)

---

## 📊 Example Diagram

List: `[10, 25, 30, 45, 50]`
Target = `30`

```
Step 1: 10 ≠ 30
Step 2: 25 ≠ 30
Step 3: 30 = 30 ✅ (Found)
```
---
