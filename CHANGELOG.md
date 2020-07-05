2020.07
-------------------------------------------------------------------------------

- added a wrapper for [linkit](https://github.com/dreipol/linkit) with djangocms-blog support, located at `backend.plugins.link`
- added backend.site_config example

### Documentation

- updated backend.md

2020.06
-------------------------------------------------------------------------------

- added [djangocms-socialshare](https://gitlab.com/what-digital/djangocms-socialshare) - a plugin for customizable rendering of sharing and social links icons
- added [djangocms-algolia](https://gitlab.com/victor.yunenko/djangocms-algolia)
- added [linkit](https://github.com/dreipol/linkit) that must be used for all links from now on
- fixed the `login with divio` feature that used to raise an "email duplicate error" ([divio/aldryn-sso#66](https://github.com/divio/aldryn-sso/issues/66))
- fixed the freezing of page after 5-10 CMS edits
- fixed django-cms (or aldryn-django) local caching issue

### Breaking Changes

- replaced `backend.articles` with djangocms-blog
- moved out `backend.tests.test_pages` into djangocms-helpers 2.2
- moved `backend.plugins.default` to `backend.plugins` for simplification
- deleted `bs4_card_columns`, because it appears that it requires styles and we've haven't seen a request from the client to style it
