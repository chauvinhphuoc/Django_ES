# Setup
## PostgreSQL database config
### - Download PostgreSQL based on your OS: [Link](https://www.postgresql.org/download/)
### - Create a super user named `postgres` and password `123456`
### - Create a database named `mydb` and one table `mytable`
### - Import this dataset to your database: [Link](https://www.dropbox.com/s/35c3t80stwa3tyz/mydataset.json?dl=0)
## Elasticsearch config
### - Download Elasticsearch based on your OS: [Link](https://www.elastic.co/fr/start)
### - Start Elasticsearch: `bin/elasticsearch`
### - Create an index called `news_headlines` by using curl, postman or kibana:
*Using curl* `curl -XPUT "http://localhost:9200/news_headlines`
## Synching PostgreSQL database into Elasticsearch using Logstash
### - Ensure Elasticsearch and PostgreSQL server are open during this time
### - Download Logstash: [Link](https://www.elastic.co/fr/downloads/logstash)
### - Download jdbc driver for PostgreSQL: [Link](https://jdbc.postgresql.org/download.html) and put into this folder:
`logstash/logstash-core/lib/jars`
### - Download this config file and put into `bin/logstash`: [Link](https://www.dropbox.com/s/chyj5x4hja1dnvf/pipline.conf?dl=0)
### - Run logstash with -f option pointing to your configuration file
`bin/logstash -f pipeline.conf`
## Django config
### - Create a virtual environment and install required packages:
`pip install -r requirements.txt`
## Running
- Ensure Elasticsearch and PostgreSQL server are open during this time
- From the root directory: `python manage.py runserver`
