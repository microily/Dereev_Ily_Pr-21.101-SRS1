start_time = input('Введите время начала работы маршрута (в формате ЧЧ:ММ): ')
end_time = input('Введите время окончания работы маршрута (в формате ЧЧ:ММ): ')
duration = int(input('Введите протяженность маршрута в минутах (в одну сторону): '))
rest_time = int(input('Введите время отдыха на конечных остановках в минутах: '))
start_hour, start_minute =  map(int, start_time.split(':'))
end_hour, end_minute = map(int, end_time.split(':'))
start_total_minutes = start_hour * 60 + start_minute
end_total_minutes = end_hour * 60 + end_minute
current_minutes = start_total_minutes
print('Суточное расписание маршрута:')
while current_minutes <= end_total_minutes:
    current_hour = current_minutes // 60
    current_minute = current_minutes % 60
    current_time = f"{current_hour:02d}:{current_minute:02d}"
    current_minutes += duration + rest_time