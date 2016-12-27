# coding:utf-8

from peewee import *
import datetime

db = SqliteDatabase('posts.db')

class Post(Model):
    id = PrimaryKeyField()
    date = DateTimeField(default = datetime.datetime.now)
    title = CharField(unique = True)
    text = TextField()

    class Meta:
        database = db

def initialize_db():
    db.connect()
    db.create_tables([Post], safe=True)

if __name__ == '__main__':
    db.connect()

    # p = Post.create(title='First article', text='hello world')
    # p = Post.create(title='Second article', text='hello world 2')

    posts = Post.select()
    for p in posts:
        print(p.title)

    dct = Post.select().dicts().get()
    print(dct)
    db.close()
