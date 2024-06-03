cp -r step6 step7
cd step7
cd flaskr
touch auth.py
vi auth.py
:wq

色々編集

python
import flask
flask.__version__
exit()
flask --version
pwd
/Users/fujitajunya/Desktop/dev/flaskProject/step7/flaskr
. venv/bin/activate


(venv) fujitajunya@admin step7 % export FLASK_ENV=development
(venv) fujitajunya@admin step7 % flask --app flaskr run