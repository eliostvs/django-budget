SHELL := /bin/sh

PROJECT := django-budget
LOCALPATH := $(CURDIR)/$(PROJECT)
PYTHONPATH := $(LOCALPATH)/
SETTINGS := production
DJANGO_SETTINGS_MODULE = config.settings.$(SETTINGS)
DJANGO_POSTFIX := --settings=$(DJANGO_SETTINGS_MODULE) --pythonpath=.$(PYTHONPATH)
LOCAL_SETTINGS := local
DJANGO_LOCAL_SETTINGS_MODULE = config.settings.$(LOCAL_SETTINGS)
DJANGO_LOCAL_POSTFIX := --settings=$(DJANGO_LOCAL_SETTINGS_MODULE) --pythonpath=$(PYTHONPATH)
TEST_SETTINGS := test
DJANGO_TEST_SETTINGS_MODULE = config.settings.$(TEST_SETTINGS)
DJANGO_POSTFIX := --settings=$(DJANGO_SETTINGS_MODULE) --pythonpath=$(PYTHONPATH)
DJANGO_TEST_POSTFIX := --settings=$(DJANGO_TEST_SETTINGS_MODULE) --pythonpath=$(PYTHONPATH)
VERBOSITY := 1

.PHONY: collectstatic runserver localrunserver syncdb localsyncdb \
		shell clean test test.functional test.all report install lint

collectstatic:
	@python $(LOCALPATH)/manage.py collectstatic --noinput -c

runserver:
	@django-admin.py runserver $(DJANGO_POSTFIX)

localrunserver:
	@django-admin.py runserver $(DJANGO_LOCAL_POSTFIX)

syncdb:
	@django-admin.py syncdb $(DJANGO_POSTFIX)

localsyncdb:
	@django-admin.py syncdb $(DJANGO_LOCAL_POSTFIX)

shell:
	@django-admin.py shell_plus $(DJANGO_LOCAL_POSTFIX)

clean:
	@find . -name "*.pyc" -print0 | xargs -0 rm -rf
	@rm -rf htmlcov
	@rm -rf .coverage
	@rm -rf build
	@rm -rf dist
	@rm -rf src/*.egg-info
	@rm -rf *.orig

test: clean
	@django-admin.py test --verbosity=$(VERBOSITY) \
	$(APP) $(DJANGO_TEST_POSTFIX)

coverage: clean
	@coverage run $(LOCALPATH)/manage.py test --verbosity=$(VERBOSITY) \
	$(APP) $(DJANGO_TEST_POSTFIX)

test.functional: clean
	@django-admin.py test --verbosity=$(VERBOSITY) \
	--pattern="functional_*.py" $(APP) $(DJANGO_TEST_POSTFIX)

test.all: coverage test.functional

report:
	@coverage report -m

install: requirements/$(SETTINGS).txt
	@pip install -r requirements/$(SETTINGS).txt

lint:
	@flake8 $(LOCALPATH)
