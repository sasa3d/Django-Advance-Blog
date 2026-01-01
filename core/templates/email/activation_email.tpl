{% extends "mail_templated/base.tpl" %}

{% block subject %}
 Accont Activation {% comment %}{{ name }} {% endcomment %}
{% endblock %}

{% block html %}
This is an <strong>html of my first email for تست </strong> message.

http://127.0.0.1:8000/accounts/api/v1/activate/confirm/{{token}}
{% endblock %}

{% block txt %}
{% endblock %}