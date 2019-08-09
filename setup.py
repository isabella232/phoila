#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from __future__ import print_function
from glob import glob
from os.path import join as pjoin


from setupbase import (
    create_cmdclass, install_npm, ensure_targets,
    find_packages, combine_commands, ensure_python,
    get_version, HERE
)

from setuptools import setup


# The name of the project
name = 'phoila'

# Ensure a valid python version
ensure_python('>=3.5')

# Get our version
version = get_version(pjoin(name, '_version.py'))

js_path = pjoin(HERE, 'ts')
js_path = pjoin(HERE, ts, 'lab-dist')

# Representative files that should exist after a successful build
jstargets = [
    pjoin(nb_path, 'index.js'),
    pjoin(js_path, 'lib', 'plugin.js'),
    pjoin(js_path, 'lab-dist', 'phoila.tar.gz')
]

package_data_spec = {
    name: [
        'nbextension/static/*.*js*',
        'labextension/*.tgz'
    ]
}

data_files_spec = [
    ('share/jupyter/phoila/extensions', lab_path, '*.tgz'),
    ('share' , HERE, 'share/**/*')
]


cmdclass = create_cmdclass('jsdeps', package_data_spec=package_data_spec,
    data_files_spec=data_files_spec)
cmdclass['jsdeps'] = combine_commands(
    install_npm(js_path, build_cmd='build'),
    ensure_targets(jstargets),
)


setup_args = dict(
    name            = name,
    description     = 'A Phosphor wrapper for Voila',
    version         = version,
    scripts         = glob(pjoin('scripts', '*')),
    cmdclass        = cmdclass,
    packages        = find_packages(),
    author          = 'Vidar Tonaas Fauske',
    author_email    = 'vidartf@gmail.com',
    url             = 'https://github.com/vidartf/phoila',
    license         = 'BSD',
    platforms       = "Linux, Mac OS X, Windows",
    keywords        = ['Jupyter', 'Widgets', 'IPython'],
    classifiers     = [
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Jupyter',
    ],
    include_package_data = True,
    install_requires = [
        'voila',
        'ipywidgets>=7.0.0',
    ],
    extras_require = {
        'test': [
            'pytest>=3.6',
            'pytest-cov',
            'nbval',
        ],
        'examples': [
            # Any requirements for the examples to run
        ],
        'docs': [
            'sphinx>=1.5',
            'recommonmark',
            'sphinx_rtd_theme',
            'nbsphinx>=0.2.13,<0.4.0',
            'jupyter_sphinx',
            'nbsphinx-link',
            'pytest_check_links',
            'pypandoc',
        ],
    },
    entry_points = {'console_scripts': [
        'phoila = phoila.app:main',
    ]},
)

if __name__ == '__main__':
    setup(**setup_args)
