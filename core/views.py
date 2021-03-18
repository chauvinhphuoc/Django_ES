from django.shortcuts import render
from elasticsearch import Elasticsearch


es = Elasticsearch()


def search_es(search_string):
    query = {
        "query": {
            "multi_match": {
                "query": search_string,
                "fields": [
                    "category",
                    "headline",
                    "authors",
                    "short_description"
                ]
            }
        }
    }
    res = es.search(index="news_headlines", body=query, track_total_hits=True)

    return res


# def search_db(search_string):
#     try:
#         conn = psycopg2.connect(f'dbname={os.getenv("dbname")} user={os.getenv("user")} password={os.getenv("password")}')
#         cur = conn.cursor(cursor_factory=DictCursor)
#         cur.execute(f'SELECT * FROM mytable WHERE headline IN {[search_string]}')
#         hits = cur.fetchone()
#         print(hits)
#         context = {"hits": hits}
#         return context
#     except Exception as e:
#         print(e)


def home(request):
    search_string = request.GET.get("search")
    if not search_string:
        context = {}
    else:
        try:
            res = search_es(search_string)
            hits = res['hits']['hits']
            total_hits = res['hits']['total']['value']
            context = {"hits": hits, 'total_hits': total_hits}
        except Exception as e:
            context = {'error': e}

    return render(request, 'core/search.html', context)
