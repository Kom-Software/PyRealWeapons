from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='PyRealWeapons',
  version='0.1.0',
  author='timpo14',
  author_email='tamerlanusmaximus@=@gmail.com',
  description='Python package with description a many real weapons.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/Kom-Software/PyRealWeapons',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='weapons',
  project_urls={
    'GitHub': 'https://github.com/Kom-Software/PyRealWeapons'
  },
  python_requires='>=3.6'
)