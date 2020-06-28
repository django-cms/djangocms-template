### Adding new packages and apps

Don't add your project custom package within the existing template package, eg here `my_package` was added incorrectly:
```
INSTALLED_APPS.extend([
    # django

    'allauth',
    'allauth.account',
    '{my_package}',
    'gtm',
    'solo',
)]
```

Add them at the bottom of the list instead, eg
```
INSTALLED_APPS.extend([
    # django

    'allauth',
    'allauth.account',
    'gtm',
    'solo',
    'my_package',
)]
```

Same goes for every other file, package.json. requirements.in, etc.

This allows people who merge in the latest updates from djangocms-template repository avoid merge conflicts or at least see clearly where you've changed the default template.
