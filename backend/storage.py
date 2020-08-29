import os
from urllib.parse import unquote
from urllib.parse import urlsplit
from urllib.parse import urlunsplit

from aldryn_django.storage import GZippedStaticFilesMixin
from django.contrib.staticfiles.storage import ManifestStaticFilesStorage


class NonStrictManifestGZippedStaticFilesStorage(GZippedStaticFilesMixin, ManifestStaticFilesStorage):
    manifest_strict = False

    def hashed_name(self, name, content=None, filename=None):
        """
        Override the hashed_name() in order to skip missing files. Otherwise collectstatic files eg
        if an external library points to a file that doesn't exist.
        All the code is identical to the parent, except the removal of `if not self.exists(filename)` clause.
        """
        # `filename` is the name of file to hash if `content` isn't given.
        # `name` is the base name to construct the new hashed filename from.
        parsed_name = urlsplit(unquote(name))
        clean_name = parsed_name.path.strip()
        filename = (filename and urlsplit(unquote(filename)).path.strip()) or clean_name
        opened = content is None
        if opened:
            try:
                content = self.open(filename)
            except IOError:
                # Handle directory paths and fragments
                return name
        try:
            file_hash = self.file_hash(clean_name, content)
        finally:
            if opened:
                content.close()
        path, filename = os.path.split(clean_name)
        root, ext = os.path.splitext(filename)
        if file_hash is not None:
            file_hash = ".%s" % file_hash
        hashed_name = os.path.join(path, "%s%s%s" %
                                   (root, file_hash, ext))
        unparsed_name = list(parsed_name)
        unparsed_name[2] = hashed_name
        # Special casing for a @font-face hack, like url(myfont.eot?#iefix")
        # http://www.fontspring.com/blog/the-new-bulletproof-font-face-syntax
        if '?#' in name and not unparsed_name[3]:
            unparsed_name[2] += '?'
        return urlunsplit(unparsed_name)
