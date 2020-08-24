from datetime import date

def add_count_down_to_events(events):

    todays_date = date.today()
    

    events_with_count_down = []

    for event in events:
        event_date = date(event.event_date.year, event.event_date.month, event.event_date.day)
        time_between = event_date - todays_date
        days_between = time_between.days

        event_dict = {
            'id': event.id,
            'event_creator': event.event_creator,
            'title': event.title,
            'information': event.information,
            'header_image': event.header_image,
            'participants': event.participants,
            'event_date': event.event_date,
            'count_down': '{} Days'.format(str(days_between)),
        }

        events_with_count_down.append(event_dict)

        


    return events_with_count_down