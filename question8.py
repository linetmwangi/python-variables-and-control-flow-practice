def get_day_week(day_number):
    # dictionary
    days = {
        1: 'monday',
        2: 'tuesday',
        3: 'wednesday',
        4: 'thursday',
        5: 'friday',
        6: 'saturday',  # corrected spelling
        7: 'sunday',
    }
    return days.get(int(day_number), "invalid number")

print(get_day_week(7))

