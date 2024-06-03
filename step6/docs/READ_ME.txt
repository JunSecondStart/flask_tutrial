cp -r step5 step6
cd step6
touch db.py
vi db.py
:wq

touch schema.sql
vi schema.sql
:wq

cd flaskr
vi __init__.py
:wq

pip install flask　*いらないかも
. flaskr/venv/bin/activate
