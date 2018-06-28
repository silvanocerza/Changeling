import os
import shutil


def main():
    if "{{cookiecutter.use_django_rest_framework}}".lower() == "y":
        shutil.rmtree(os.path.join("django-{{cookicutter.project_slug}}", "api"))

    if "{{cookiecutter.add_frontend}}".lower() == "y":
        shutil.rmtree(os.path.join("django-{{cookicutter.project_slug}}", "frontend"))

    if "{{cookiecutter.license}}" != "GPLv3":
        os.remove("COPYING")

if __name__ == "__main__":
    main()