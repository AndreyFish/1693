import idx as idx

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [src[num] for  num in  range(1, len(src)) if src[num] > src[num - 1]] # работаем от 1 до длины списка len
# result = [val for  idx, val in enumerate(src) if src[idx - 1] < src[idx] and idx > 0]

print(result)