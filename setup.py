import io
import json
from setuptools import setup


with open('package.json') as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")

setup(
    name=package_name,
    version=package["version"],
    author=package['author'].split('<')[0].strip(),
    author_email=package['author'].split('<')[1].strip(),
    url=package['homepage'],
    project_urls={
        'Documentation': package['homepage'],
        'Download': 'https://github.com/DhiraPT/dash-handsontable/tags',
        'Issue Tracker': package['bugs']['url'],
        'Source': package['homepage'],
    },
    packages=[package_name],
    include_package_data=True,
    license=package['license'],
    description=package.get('description', package_name),
    long_description=io.open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    install_requires=['dash>=2.5.1'],
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Dash',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: User Interfaces',
    ],
)
