import imp
from migrate.versioning import api
from app import db
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

v = api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
migration = SQLALCHEMY_MIGRATE_REPO + ('/versions/%03d_migration.py' % (v + 1))
tmp_model = imp.new_module('old_model')
old_model = api.create_model(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
exec(old_model,tmp_model.__dict__)
script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO,tmp_model.meta,db.metadata)
open(migration,"wt").write(script)
api.upgrade(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
print('迁移保存至' + migration)
print('当前数据库版本' + str(v))