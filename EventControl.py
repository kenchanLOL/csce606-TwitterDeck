from Event import Event


def saveEventfromFrontend(location, time, content, user, dataAdapter):
    event = Event(0, location, time, content, user.ID)
    eventID = dataAdapter.saveEvent(event)
    event.ID = eventID
    return event