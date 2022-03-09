# This is a dummyfile for deployment on Heroku.
# See https://devcenter.heroku.com/articles/django-assets
# It says:
# Django won’t automatically create the target directory (STATIC_ROOT) that collectstatic uses, if it isn’t available. You may need to create this directory in your codebase, so it will be available when collectstatic is run. Git does not support empty file directories, so you will have to create a file inside that directory as well.

# assumption by Sam:
# You probably don't need the dummyfile anymore once you collect static files in advance (locally, before deployment) or after cloning a repository