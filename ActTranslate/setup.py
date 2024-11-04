from setuptools import setup, find_packages

setup(
    name='ActTranslate',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your script needs, e.g., 'numpy', 'pandas'
        'requests',
        'josn',
        'googletrans==4.0.0-rc1'
    ],
    author='Siraj Dal',
    author_email='siraj.d.actowiz@gmail.com',
    description='A lightweight package for translating text between languages, similar to Google Translate, with simple API integration and easy-to-use functions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.6',  # Specify the Python version requirement
)
