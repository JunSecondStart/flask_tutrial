mkdir step5
cd step5
mkdir docs
touch READ_ME.txt
vi READ_ME.txt
:wq

cd ..
pwd
ls

mkdir flaskr
ls
cd flaskr
touch __init__.py
vi __init__.py
(1回目の再現の時はコピペでOK)
:wq

flask --version
python --version
python3 -m venv venv
. venv/bin/activate
pip install flask
flask --version

cd ..
flask --app flaskr --debug run
http://127.0.0.1:5000
をブラウザで開き、Hello World!で成功