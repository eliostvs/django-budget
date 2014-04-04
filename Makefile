SHELL := /bin/sh

PROJECT := django_budget

LOCALPATH := $(CURDIR)/django-budget
PYTHONPATH := $(LOCALPATH)/
SETTINGS := production
DJANGO_SETTINGS_MODULE = $(PROJECT).settings.$(SETTINGS)
DJANGO_POSTFIX := --settings=$(DJANGO_SETTINGS_MODULE) --pythonpath=.$(PYTHONPATH)
LOCAL_SETTINGS := local
DJANGO_LOCAL_SETTINGS_MODULE = $(PROJECT).settings.$(LOCAL_SETTINGS)
DJANGO_LOCAL_POSTFIX := --settings=$(DJANGO_LOCAL_SETTINGS_MODULE) --pythonpath=$(PYTHONPATH)
TEST_SETTINGS := test
DJANGO_TEST_SETTINGS_MODULE = $(PROJECT).settings.$(TEST_SETTINGS)
DJANGO_POSTFIX := --settings=$(DJANGO_SETTINGS_MODULE) --pythonpath=$(PYTHONPATH)
DJANGO_TEST_POSTFIX := --settings=$(DJANGO_TEST_SETTINGS_MODULE) --pythonpath=$(PYTHONPATH)
PYTHON_BIN := $(VIRTUAL_ENV)/bin
VERBOSITY := 1

.PHONY: showenv collectstatic runserver localrunserver syncdb localsyncdb cmd shell clean test test.functional test.all report install

showenv:
	@echo 'Environment:'
	@echo '-----------------------'
	@$(PYTHON_BIN)/python -c "import sys; print 'sys.path:', sys.path"
	@echo 'PYTHONPATH:' $(PYTHONPATH)
	@echo 'PROJECT:' $(PROJECT)
	@echo 'DJANGO_SETTINGS_MODULE:' $(DJANGO_SETTINGS_MODULE)
	@echo 'DJANGO_LOCAL_SETTINGS_MODULE:' $(DJANGO_LOCAL_SETTINGS_MODULE)
	@echo 'DJANGO_TEST_SETTINGS_MODULE:' $(DJANGO_TEST_SETTINGS_MODULE)

collectstatic:
	$(PYTHON_BIN)/python $(LOCALPATH)/manage.py collectstatic --noinput -c

runserver:
	$(PYTHON_BIN)/django-admin.py runserver $(DJANGO_POSTFIX)

localrunserver:
	$(PYTHON_BIN)/django-admin.py runserver $(DJANGO_LOCAL_POSTFIX)

syncdb:
	$(PYTHON_BIN)/django-admin.py syncdb $(DJANGO_POSTFIX)

localsyncdb:
	$(PYTHON_BIN)/django-admin.py syncdb $(DJANGO_LOCAL_POSTFIX)

cmd:
	$(PYTHON_BIN)/django-admin.py $(CMD) $(DJANGO_POSTFIX)

shell:
	$(PYTHON_BIN)/django-admin.py shell_plus $(DJANGO_LOCAL_POSTFIX)

clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf build
	-rm -rf dist
	-rm -rf src/*.egg-info
	-rm -rf *.orig

test: clean
	$(PYTHON_BIN)/coverage run --source=$(LOCALPATH) --omit="*/admin.py,*/tests_*,*/functional_*,*/django_budget/*,*/manage.py" $(PYTHON_BIN)/django-admin.py test --verbosity=$(VERBOSITY) $(APP) $(DJANGO_TEST_POSTFIX)

test.functional: clean
	$(PYTHON_BIN)/django-admin.py test --verbosity=$(VERBOSITY) --pattern="functional_*.py" $(APP) $(DJANGO_TEST_POSTFIX)

test.all: test test.functional

report:
	$(PYTHON_BIN)/coverage report -m

install: requirements/$(SETTINGS).txt
	pip install -r requirements/$(SETTINGS).txt
