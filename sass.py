import subprocess
from os.path import splitext
from tempfile import NamedTemporaryFile


class DartSass:
    """ A shim that replaces libsass with Dart Sass, primarily aimed at django-sass-processor.
    """
    sass_command = ['sass']

    def compile(self, filename, include_paths, **kwargs):
        # build up include paths
        includes = [['-I', x] for x in include_paths]
        includes = [p for pp in includes for p in pp]

        outfname = splitext(filename)[0] + '.css'
        with open(outfname, 'w+') as outf:
            cmd = self.sass_command + [
                filename + ":" + outf.name,
                *includes,
            ]

            try:
                subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                raise CompileError(e.stdout.decode('utf-8'))

            content = outf.read()
            with open(outf.name + '.map', 'rb') as f:
                sourcemap = f.read()

        if 'source_map_filename' in kwargs:
            return content, sourcemap

        return content


class SassFunction:
    def __init__(self, *args, **kwargs):
        pass


class CompileError(ValueError):
    pass


dart_sass = DartSass()
compile = dart_sass.compile
