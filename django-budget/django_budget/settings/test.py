from .base import *

########## TEST SETTINGS

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
# http://stackoverflow.com/questions/9673842/default-language-via-settings-not-respected-during-testing
# https://code.djangoproject.com/ticket/15143
LANGUAGE_CODE = 'en'

########## IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

########## TEMPLATE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#template-string-if-invalid
TEMPLATE_STRING_IF_INVALID = 'INVALID VARIABLE: (%s)'

# http://django-crispy-forms.readthedocs.org/en/latest/crispy_tag_forms.html#make-crispy-forms-fail-loud
CRISPY_FAIL_SILENTLY = not DEBUG
########## END TEMPLATE CONFIGURATION
