#!/usr/bin/env python
import os
import sys

from distutils.core import setup
from distutils.dir_util import mkpath
from distutils.sysconfig import PREFIX

# Define package directories
datadir = os.path.join(PREFIX, 'share/moulinette')
libdir = os.path.join(PREFIX, 'lib/moulinette')
localedir = os.path.join(datadir, 'locale')
cachedir = '/var/cache/moulinette'

# Extend installation
locale_files = []
if "install" in sys.argv:
    # Evaluate locale files
    for f in os.listdir('src/locales'):
        if f.endswith('.json'):
            locale_files.append('src/locales/%s' % f)

    # Generate package.py
    package = open('src/moulinette/package.py.in').read()
    package = package.replace('%PKGDATADIR%', datadir) \
                  .replace('%PKGLIBDIR%', libdir) \
                  .replace('%PKGLOCALEDIR%', localedir) \
                  .replace('%PKGCACHEDIR%', cachedir)
    with open('src/moulinette/package.py', 'w') as f:
        f.write(package)

    # Create needed directories
#    mkpath(libdir, mode=0755, verbose=1)
#    mkpath(os.path.join(datadir, 'actionsmap'), mode=0755, verbose=1)


setup(name='Moulinette',
      version='2.0.0',
      description='',
      author='Yunohost Team',
      author_email='yunohost@yunohost.org',
      url='http://yunohost.org',
      license='AGPL',
      packages=['moulinette',
                'moulinette.authenticators',
                'moulinette.interfaces'],
      package_dir={'': 'src'},
      data_files=[(localedir, locale_files)]
      )
