import sys
import django
from django.conf import settings
from django.test.runner import DiscoverRunner

if not settings.configured:
    settings.configure(
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [],
                'APP_DIRS': True,
            },
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=(
            'pagination',
        ),
        SITE_ID=1,
        SECRET_KEY='this-is-just-for-tests-so-not-that-secret',
        ROOT_URLCONF='',
    )

if __name__ == "__main__":
    django.setup()
    test_runner = DiscoverRunner(verbosity=1)
    failures = test_runner.run_tests(['pagination'])
    if failures:
        sys.exit(failures)
