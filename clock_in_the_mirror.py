def mirror_time_func(mirror_time: str) -> tuple:
    while True:
        while mirror_time == '':
            mirror_time = input("Empty input. Please enter time- hh:mm ")
        try:
            separator = mirror_time[2]
            mirror_hour = int(mirror_time[:2])
            mirror_minutes = int(mirror_time[3::])

            while separator != ':' or mirror_hour > 12 or mirror_minutes > 60 \
                    or len(mirror_time[3::]) != 2 or mirror_time == '':
                mirror_time = input("Reenter time- hh:mm ")
                if mirror_time != '':
                    separator = mirror_time[2]
                    mirror_hour = int(mirror_time[:2])
                    mirror_minutes = int(mirror_time[3:])
            break
        except ValueError:
            mirror_time = input("Reenter time.e.g. 02:08 ")
    return mirror_hour, mirror_minutes


# -------------------------------------------------------------------
def clock_in_the_mirror():
    times = mirror_time_func(input("Please enter mirror time- hh:mm "))
    mirror_minutes = int(times[1])
    mirror_hour = int(times[0])

    if mirror_minutes > 0 and mirror_hour == 12:
        real_time = 'Real time is {:02d}:{:02d}'.format(12 - 1,
                                                        60 - mirror_minutes)
    elif mirror_minutes > 0 and mirror_hour < 11:
        real_time = 'Real time is {:02d}:{:02d}'.format(11 - mirror_hour,
                                                        60 - mirror_minutes)
    elif mirror_minutes > 0 and mirror_hour == 11:
        real_time = 'Real time is 12:{:02d}'.format(60 - mirror_minutes)
    elif mirror_minutes == 0 and mirror_hour < 12:
        real_time = 'Real time is: {:02d}:00'.format(12 - mirror_hour)
    else:
        real_time = 'Real time is 12:00'
    return real_time


if __name__ == "__main__":
    print(clock_in_the_mirror())
