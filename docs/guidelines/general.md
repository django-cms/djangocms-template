### Adding new packages and apps

Don't add your project custom package within the existing template package, eg
```
INSTALLED_APPS.extend([
    # django

    'allauth',
    'allauth.account',
    [...]

    'mypackage',

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
    [...]

    'mypackage',
)]
```

Same goes for every other file, package.json. requirements.in, etc.

This allows people who merge in the latest updates from djangocms-template repository avoid merge confilicts.
It also clearly indicates where your custom extension start.

### Translations

- `python manage.py makemessages -l {lang_code} --no-wrap`
