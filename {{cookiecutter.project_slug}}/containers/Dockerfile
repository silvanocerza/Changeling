FROM python:3.6

ARG DJANGO_ENV=production

ENV DJANGO_ENV=${DJANGO_ENV}
ENV DJANGO_SETTINGS_MODULE {{cookiecutter.project_slug}}.settings.dev
ENV DATABASE_URL postgres://devel:123456@postgres:5432/{{cookiecutter.project_slug}}

ENV UWSGI_HTTP 0.0.0.0:8000
ENV UWSGI_PROCESSES 2

COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install $(test "$DJANGO_ENV" == production || echo "--dev") --system --deploy --ignore-pipfile

EXPOSE 8000

CMD ["uwsgi", "--need-app", "--chdir", "django-{{cookiecutter.project_slug}}", "--py-autoreload", "1", \
     "--http", "8000", "--module", "{{cookiecutter.project_slug}}.wsgi", "--check-static", \
     "/app/django-{{cookiecutter.project_slug}}/", "--offload-threads", "4"]

