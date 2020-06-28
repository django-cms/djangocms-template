2020.06
-------------------------------------------------------------------------------

- fixed the `login with divio` feature that used to raise an "email duplicate error" ([divio/aldryn-sso#66](https://github.com/divio/aldryn-sso/issues/66))
- added [djangocms-socialshare](https://gitlab.com/what-digital/djangocms-socialshare) - a plugin for customizable rendering of sharing and social links icons
- added [djangocms-algolia](https://gitlab.com/victor.yunenko/djangocms-algolia)

### Breaking Changes

- replaced `backend.articles` with djangocms-blog
- moved out `backend.tests.test_pages` into djangocms-helpers 2.2
