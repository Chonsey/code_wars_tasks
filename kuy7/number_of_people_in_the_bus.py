def number(bus_stops):
    num_bus_stops = []
    start = 0
    bus_stops.append(start)
    for i in bus_stops:
        if isinstance(i, (list, tuple)) and len(i) == 2:
            seli = i[0]
            usli = i[1]
            start += seli - usli
    return start 
