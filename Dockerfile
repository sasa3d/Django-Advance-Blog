FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app 
COPY requirements.txt /app/
# 1. تنظیم میرور به صورت جهانی (Global) برای کل ایمیج
ENV PIP_INDEX_URL=https://mirror-pypi.runflare.com/simple
ENV PIP_TRUSTED_HOST=mirror-pypi.runflare.com
ENV PIP_DEFAULT_TIMEOUT=1000

# 2. حالا نصب پکیج‌ها (بدون نیاز به نوشتن آدرس میرور چون بالا ست شده)
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

    

COPY ./core /app
#CMD [ "python", "manage.py","runserver","0.0.0.0:8000" ]
