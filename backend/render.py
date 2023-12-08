from jinja2 import Environment, FileSystemLoader
# from .. backend import Event
# from backend.DataAdapter import DataAdapter

def render_home(events_obj, fname = "backend/templates/home_render.html"):
    events = [
        e.__dict__ for e in events_obj
    ]
    context = {
        "events": events
    }
    environment = Environment(loader=FileSystemLoader("backend/templates/"))
    template = environment.get_template("home.html")
    # for event in events:
        # filename = f"message_{event['name'].lower()}.txt"
    content = template.render(context)
    with open(fname, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {fname}")
    return content

def render_deck(all_tweets, fname = "backend/templates/deck_render.html"):
    context = {
        "all_tweets": all_tweets,
    }
    environment = Environment(loader=FileSystemLoader("backend/templates/"))
    template = environment.get_template("deck.html")
    # for event in events:
        # filename = f"message_{event['name'].lower()}.txt"
    content = template.render(context)
    with open(fname, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {fname}")
    return content

# if __name__ == "__main__":
    # dataAdapter =  DataAdapter("backend/TwitterDeck.db")
    # events = dataAdapter.loadEventByUser(1)
    # print(len(events))
    # content = render_home(events)
    
    # queries = dataAdapter.loadQueryByEvent(3)
    # all_tweets = []
    # for query in queries:
    #     tweetIDs = dataAdapter.loadTweetIDByQuery(query.ID)
    #     tweets = []
    #     for tweetID in tweetIDs:
    #         tweets.append(dataAdapter.loadTweet(tweetID).__dict__ )
    #     all_tweets.append({"tweets":tweets})
    # render_deck(all_tweets)
    # print(query)
    # print(content)