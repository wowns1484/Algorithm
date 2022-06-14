def solution(arr1, arr2):
    answer = []

    for a, b in zip(arr1, arr2):
        cols = []
        for x, y in zip(a, b):
            cols.append(x + y)
        answer.append(cols)

    return answer