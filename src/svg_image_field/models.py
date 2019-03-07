# import the File class to inherit from
from filer.models.filemodels import File
import os


class SvgImageFile(File):
    @classmethod
    def matches_file_type(cls, iname, ifile, request):
#        iext = os.path.splitext(iname)[1].lower()
#        return iext in ['.jpg', '.jpeg', '.png', '.gif', '.svg']
        return True  # I match all files...