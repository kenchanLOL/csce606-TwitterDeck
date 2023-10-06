from Query import Query


def saveQueryfromFrontend(content, Event, dataAdapter):
    query = Query(0, content, Event.ID)
    queryID = dataAdapter.saveQuery(query)
    query.ID = queryID
    return query