echo "BUILD START"

python -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear

echo "BUILD END1111111111"