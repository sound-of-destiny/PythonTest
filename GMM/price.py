from elasticsearch import Elasticsearch
import pymysql
import numpy as np
import pandas as pd

conn= pymysql.connect(
        host='127.0.0.1',
        port = 3306,
        user='root',
        passwd='root',
        db ='supnuevo_statistics',

        charset='UTF8'
    )
cur = conn.cursor()
sql = "SELECT codigo FROM supnuevo_statistics.supnuevo_common_commodity where modifyTime > 20180101"
cur.execute(sql)
codigoList = cur.fetchall()

es = Elasticsearch([
            {'host': '202.194.14.106', 'port': 9200},
        ])

for codigo in codigoList:
    res = es.search(index="supnuevo-now-price", body={
  "aggs": {
      "2": {
          "terms": {
          "field": "price",
          "size": 10000000,
          "order": {
          "_term": "asc"
          }
        }
      }
  },
  "size": 0,
  "_source": {
    "excludes": []
  },
  "stored_fields": [
    "*"
  ],
  "script_fields": {},
  "docvalue_fields": [
    "@timestamp"
  ],
  "query": {
    "bool": {
      "must": [
        {
          "match_all": {}
        },
        {
          "range": {
            "@timestamp": {
              "gte": 1526140800000,
              "lte": 1532879999999,
              "format": "epoch_millis"
            }
          }
        },
        {
          "match_phrase": {
            "codigo": {
              "query": codigo[0]
            }
          }
        }
      ],
      "filter": [],
      "should": [],
      "must_not": []
    }
    }
  })

    result = res['aggregations']['2']['buckets']
    sql2 = "SELECT commodityId FROM supnuevo_statistics.supnuevo_common_commodity where codigo = '" + codigo[0] + "'"
    cur.execute(sql2)   
    commodityId = cur.fetchone()
    for c in result:
        key = c.get('key')
        count = c.get('doc_count')
        isql = "insert into supnuevo_statistics.supnuevo_now_price_count_all (commodityId,codigo,nowprice,count) values (%d,'%s',%s,%d)" % (commodityId[0],codigo[0],key,count)
        cur.execute(isql)
        conn.commit()

conn.close()
    