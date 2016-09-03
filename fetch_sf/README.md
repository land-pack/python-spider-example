# Spider for Crazy Bet

###How to install ?

```
pip install -r requirements.txt
```
###How to run ?

First at first, run your mongodb server.

```
mongod
```
come in the main project dir ..
```
cd sf
```
Run the celery and register the task!

```
celery -A crawl.celeryapp -l info -c 5
python web/api.py
```
Run the test client

```
python test_post.py
```
To send a task manual,

```
python main.py
```

In the really production env, you can use `linux cron` to do it instead!








