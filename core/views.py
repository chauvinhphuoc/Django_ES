from django.shortcuts import render
from elasticsearch import Elasticsearch, ElasticsearchException

import psycopg2
from psycopg2.extras import DictCursor
import os


def search_es(search_string):
    es = Elasticsearch()
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
    res = es.search(index="news_headlines", body=query)
    hits = res['hits']['hits']
    context = {"hits": hits}

    return context


def search_db(search_string):
    try:
        conn = psycopg2.connect(f'dbname={os.getenv("dbname")} user={os.getenv("user")} password={os.getenv("password")}')
        cur = conn.cursor(cursor_factory=DictCursor)
        cur.execute(f'SELECT * FROM mytable WHERE headline IN {[search_string]}')
        hits = cur.fetchone()
        print(hits)
        context = {"hits": hits}
        return context
    except Exception as e:
        print(e)


def home(request):
    search_string = request.GET.get("search")
    if not search_string:
        context = {}
    else:
        try:
            context = search_es(search_string)
        except Exception:
            try:
                context = search_db(search_string)
            except Exception:
                context = {'error': "Server Error"}

    return render(request, 'core/search.html', context)
