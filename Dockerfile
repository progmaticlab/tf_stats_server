source ~/venvs/tf_stats_server_venv/bin/activate
cd /home/deremeev/repos/tf_stats_server/
pip install -r requirements.txt 
# django-admin startproject contrail_stats_server
cd tf_stats_server/
# django-admin startapp rest_api
python manage.py migrate
python manage.py makemigrations rest_api
python manage.py migrate