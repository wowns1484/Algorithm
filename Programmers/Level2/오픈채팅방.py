def solution(record):
    answer = []
    user = {}
    logs = []

    for rec in record:
        data = rec.split(" ")

        if data[1] not in user:
            user[data[1]] = data[2]

        if len(data) == 3:
            if data[0] == "Enter":
                logs.append((data[1], "님이 들어왔습니다."))

            if user[data[1]] != data[2]:
                user[data[1]] = data[2]
        else:
            logs.append((data[1], "님이 나갔습니다."))

    for log in logs:
        answer.append(user[log[0]] + log[1])    

    return answer