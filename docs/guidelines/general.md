### Adding new packages and apps

Add your project custom packages to the end of the list of packages.

'my_package' was added correctly:

```
INSTALLED_APPS = [
    # django

    'allauth',
    'allauth.account',
    'gtm',
    'solo',
    'my_package',
]
```

'my_package' was NOT added correctly:
```
INSTALLED_APPS = [
    # django

    'allauth',
    'allauth.account',
    'my_package',
    'gtm',
    'solo',
]
```

Same goes for every other file, package.json. requirements.in, etc.

This allows people who merge in the latest updates from djangocms-template repository avoid merge conflicts or at least see clearly where you've changed the default template.
