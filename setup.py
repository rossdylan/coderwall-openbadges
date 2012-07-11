import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


requires = [
    'tahrir-api',
    'coderwall'
    ]

setup(name='coderwall-openbadges',
      version='0.1.0',
      description='Award coderwall badges as openbadges',
      long_description=README,
      license="AGPLv3+",
      classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        ],
      author='Ross Delinger',
      author_email='rdelinge@redhat.com',
      url='http://github.com/rossdylan/coderwall-openbadges',
      packages=['coderwall_openbadges'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""
      [console_scripts]
      cw2ob = coderwall_openbadges:main
      """
      )

