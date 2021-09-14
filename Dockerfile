FROM python:3.9.0

WORKDIR /home/

RUN echo 'Amu Mal'

RUN git clone https://github.com/timgotango/gis_4ban_1.git

WORKDIR /home/gis_4ban_1/

RUN echo "SECRET_KEY=django-insecure-xtsf-7km3luqo(gjlej6nay-t7denaip7rlhine^84^6h%(49^" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "gis_4ban_1.wsgi", "--bind", "0.0.0.0:8000"]