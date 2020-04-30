This is a state of the art DjangoCMS template. It's used in at least 9 live projects at the moment.

This project adheres to the following coding guidelines - https://gitlab.com/what-digital/tech-docs/-/tree/master/coding-guidelines

### Intro

The project contains two main branches:
- `divio` - the main branch adapted for divio.com support
- `master` - the secondary branch for native linux servers, mostly adapted for what.digital ansible deployments, right now it's isn't officially supported.

The main features:
- production-ready plugins setup (galleries, google maps, blog, multi-columns & responsive content, etc)
- latest webpack version configuration with typescript and scss support, including a highly performant real-time compilation
- latest fixes for DjangoCMS and its core ecosystem critical issues, that haven't been deployed on the mainstream yet (for details see djangocms-helpers package and settings)

### Guidelines

- [general](/docs/guidelines/general.md)
- [frontend](/docs/guidelines/frontend.md)
- [backend](/docs/guidelines/backend.md)
