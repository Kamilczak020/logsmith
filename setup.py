import setuptools

with open('README.md', 'r') as reader:
  long_description = reader.read()

setuptools.setup(
  name = 'logsmith',
  version = '0.0.1',
  author = 'Kamil Solecki',
  author_email = 'kamilczak020@gmail.com',
  description = 'A beautiful, functional logger for all your logging needs.',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/Kamilczak020/logsmith',
  packages = setuptools.find_packages(),
  classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)