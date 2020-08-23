def add_count_down_to_events(events):

    events_with_count_down = []

    for event in events:
        event_dict = {
            'event_creator': event.event_creator,
            'title': event.title,
            'information': event.information,
            'header_image': event.header_image,
            'participants': event.participants,
            'event_date': event.event_date,
            'count_down': '1 Day'
        }

        events_with_count_down.append(event_dict)

        


    return events_with_count_down