# django-sass-processor-dart-sass

This is a shim that makes [django-sass-processor](https://pypi.org/project/django-sass-processor/) use
[Dart Sass](https://sass-lang.com/dart-sass) rather than [libsass](https://sass-lang.com/libsass) because
libsass is deprecated.

This provides a replacement for `sass.py` provided by libsass and simply calls out to `sass` provided by Dart Sass.
Dart Sass must be [installed separately](https://sass-lang.com/install).

## Note: vanilla Dart Sass only

This does not support the custom functions provided by django-sass-processor through libsass. It only supports vanilla
Dart Sass.

## How to use it

This clashes with libsass, so remove libsass if you have it installed:

```
pip uninstall libsass
```

Install Dart Sass by following their [instructions](https://sass-lang.com/install).

Install this package:

```bash
pip install https://github.com/laws-africa/django-sass-processor-dart-sass
```

That's it. Install and use `django-sass-processor` as normal.

# Advanced usage

If you need to change the `sass` command, override it like so:

```python
from sass import dart_sass
dart_sass.sass_command = ['/special/sass']

# to use npm sass, use:
dart_sass.sass_command = ['npx', 'sass']
```

# Build and release

Build: `python3 -m build`

Release to Pypi: `python3 -m twine upload dist/*`
