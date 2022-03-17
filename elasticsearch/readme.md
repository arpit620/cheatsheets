
Cluster > Node > Index > Type > Documents > Shard/ Replica

Format:

<REST verb> <Index> <Type> <ID>
PUT sales order 123
GET sales order 123
DELETE sales

######

Cluster health: 
GET _cat/health?v
GET _cat/nodes?v
GET _cat/indices?v

PUT /sales

PUT /sales/order/123
{
    "orderID": "123",
    "orderAmount": "500"
}

GET /sales/order/123

DELETE sales


######

Bulk Data Loading:
/buld
new-line json data
Index, create, update, delete
--data-binary

GET /my-test
GET /my-test/my-type/1


POST _bulk
{
    data
}

######

Different data types:
Core
Complex
Geo
Specialized


######

GET _cat/indices/logstash-*
GET _cat/indices/accsec-*

######

Return everything:
GET bank/account/_search

GET bank/account/_search
{
    "query": {
        "match": {
            "FIELD": "TEXT"
        }
    }
}

GET bank/account/_search
{
    "query": {
        "match": {
            "state": "CA"
        }
    }
}

##

GET bank/account/_search
{
    "query": {
        "bool": {
            "must": [
                {"match": {
                    "state": "CA"
                }},
                { "match": {
                    "state": "Techade"
                }}
            ]
        }
    }
}

##

GET bank/account/_search
{
    "query": {
        "bool": {
            "must_not": [
                {"match": {
                    "state": "CA"
                }},
                { "match": {
                    "state": "Techade"
                }}
            ]
        }
    }
}


##

GET bank/account/_search
{
    "query": {
        "bool": {
            "should": [
                {"match": {
                    "state": "CA"
                }},
                { "match": {
                    "lastname": {"query": "Smith", "boost": 3}
                }}
            ]
        }
    }
}

#############


# Terms query works only for numeric field
# And not for strings...
GET /_search
{
  "query": {
    "term": {
      "account_number": 516 
    }
  }
}

GET /_search
{
  "query": {
    "terms": {
      "account_number": [516, 812]
    }
  }
}


GET /_search
{
  "query": {
    "range": {
      "account_number": {
          "gte" : 516,
          "lte" : 851,
          "boost" : 2
      }
    }
  }
}

GET /_search
{
  "query": {
    "range": {
      "age": {
          "gte" : 35
      }
    }
  }
}


##################

Text processing:

GET bank/_analyze
{
    "tokenizer": "standard",
    "text": "The Moon is Made of Cheese Some Say"
}

GET bank/_analyze
{
    "tokenizer": "uax_url_email",
    "text": "xyz@example.com login at http://google.com attempt"
}


##################

Aggregations: 

GET bank/account/_search
{
    
}





