import shelve

def load_chat_history(database):
    with shelve.open(database) as db:
        return db.get("messages", [])
    

def load_chat_summary(database):
    with shelve.open(database) as db:
        response=db.get("summaries", [])
        return response
    

def generating_summary(messages,top_k,database):
    response=[] 
    for message in reversed(messages):
        response.append(message)
        if len(response)>top_k:
            break
    save_summaries(response,database)
    return response


def save_summaries(summary,database):
    with shelve.open(database) as db:
        db['summaries']=summary


def save_chat_history(messages,database):
    with shelve.open(database) as db:
        db["messages"] = messages


