{% extends "mail_templated/base.tpl" %}

{% block subject %}
 Accont Activation {% comment %}{{ name }} {% endcomment %}
{% endblock %}

{% block html %}
{% comment %} This is an <strong>html of my first email for تست </strong> message.
<img src="https://www.djangoproject.com/m/img/logos/django-logo-positive.png" alt="Django Logo">
<img src="https://tse2.mm.bing.net/th/id/OIP.LtT854-wcVIt16WOhiT9TgAAAA?rs=1&pid=ImgDetMain&o=7&rm=3">  {% endcomment %}
{{token}}
{% endblock %}

{% block txt %}
{% endblock %}