from collections import deque

def refine_timetable(timetable, last_bus):
    refined = deque()
    timetable.sort()
    for time_i in timetable:
        t = int(time_i.split(":")[0]) * 60 + int(time_i.split(":")[1])
        if last_bus < t:
            break
        refined.append(t)
    return refined

def solution(n, t, m, timetable):
    bus_table = deque([540 + i * t for i in range(n)])
    user_table = refine_timetable(timetable, bus_table[-1])
    sheets, last_user = 0, None
    while bus_table and user_table:
        sheets = m
        while sheets and user_table and user_table[0] <= bus_table[0]:
            last_user = user_table.popleft()
            sheets -= 1
        bus_table.popleft()

    if bus_table:
        return '%02d:%02d' % (bus_table[-1] // 60, bus_table[-1] % 60)
    else:
        return '%02d:%02d' % (last_user // 60, last_user % 60 - 1)


if __name__ == '__main__':
    print(solution(
        2, 10, 2, ["09:10", "09:09", "08:00"]
    ))