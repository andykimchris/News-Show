def get_top_headlines(headlines):
    head_list = []
    for headline in headlines:
        id = headline['source']['id']
        if id not in head_list:
            head_list.append(id)

    return head_list


def get_top_sources(sources, headlines):
    source_list = []
    for source in sources:
        id = source['id']
        if id in headlines:
            source_list.append(source)

    return source_list
