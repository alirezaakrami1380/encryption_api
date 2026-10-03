from peewee import SqliteDatabase
from config import Config

db = SqliteDatabase(Config.DATABASE)