from setuptools import setup, find_packages

setup(
    name='probvis',
    version='1.0.0',
    #packages=['probvis', 'probvis.distributions', 'probvis.graphical_models'],
    packages=find_packages(exclude=['images', 'tests']),
    url='https://github.com/psanch21/prob-visualize',
    license='MIT License',
    author='Pablo Sanchez',
    author_email='pablo.sanchez-martin@tuebingen.mpg.de',
    description='Functions to visualize your data',
    python_requires='>=3.5',
)
