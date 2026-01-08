from services.search import store_text, search_text

def store_endpoint():
    text = "Can I know policy of Cascade Clouds?"
    store_text(text, "query1")
    return "Data stored successfully"

def search_endpoint():
    query = "Cascade Clouds policy"
    return search_text(query)
