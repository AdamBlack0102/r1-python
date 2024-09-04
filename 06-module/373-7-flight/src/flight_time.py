def flight_calculation():
    depart_time_1 = input()
    arrive_time_1 = input()

    depart_time_1_parts = depart_time_1.replace(' ', '').split(':')
    depart_hour_1, depart_minute_1, depart_second_1 = map(int, depart_time_1_parts[:3])

    arrive_time_1_parts = arrive_time_1.replace(' ', '').split(':')
    arrive_hour_1, arrive_minute_1, arrive_second_1 = map(int, arrive_time_1_parts[:3])

    if len(arrive_time_1_parts) > 3:
        if '(+1)' in arrive_time_1_parts[3]:
            arrive_hour_1 += 24
        elif '(+2)' in arrive_time_1_parts[3]:
            arrive_hour_1 += 48

    depart_time_2 = input()
    arrive_time_2 = input()

    depart_time_2_parts = depart_time_2.replace(' ', '').split(':')
    depart_hour_2, depart_minute_2, depart_second_2 = map(int, depart_time_2_parts[:3])

    arrive_time_2_parts = arrive_time_2.replace(' ', '').split(':')
    arrive_hour_2, arrive_minute_2, arrive_second_2 = map(int, arrive_time_2_parts[:3])

    if len(arrive_time_2_parts) > 3:
        if '(+1)' in arrive_time_2_parts[3]:
            arrive_hour_2 += 24
        elif '(+2)' in arrive_time_2_parts[3]:
            arrive_hour_2 += 48

    depart_seconds_1 = depart_hour_1 * 3600 + depart_minute_1 * 60 + depart_second_1
    arrive_seconds_1 = arrive_hour_1 * 3600 + arrive_minute_1 * 60 + arrive_second_1

    fly_time_1 = arrive_seconds_1 - depart_seconds_1

    depart_seconds_2 = depart_hour_2 * 3600 + depart_minute_2 * 60 + depart_second_2
    arrive_seconds_2 = arrive_hour_2 * 3600 + arrive_minute_2 * 60 + arrive_second_2

    fly_time_2 = arrive_seconds_2 - depart_seconds_2

    if fly_time_1 == fly_time_2:
        whole_hour = fly_time_1 // 3600
        whole_minute = (fly_time_1 % 3600) // 60
        whole_second = fly_time_1 % 60
    else:
        fly_time = (fly_time_1 + fly_time_2) / 2
        whole_hour = fly_time // 3600
        whole_minute = (fly_time % 3600) // 60
        whole_second = fly_time % 60

    print('{:02d}:{:02d}:{:02d}\n'.format(whole_hour, whole_minute, whole_second))

    return
