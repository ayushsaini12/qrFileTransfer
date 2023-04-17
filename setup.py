import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='qr-filetransfer',
    version='2.6.1',
    author='Ayush Saini',
    author_email='ayushsaini469@gmail.com',
    description='Transfer files over WiFi between your computer and your smartphone from the terminal',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ayushsaini12/qrFileTransfer.git',
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': ['qr-filetransfer = qr_filetransfer:main']},
    install_requires=['qrcode', 'colorama; platform_system == "Windows"'],
    extras_require={'extras': ['netifaces']}
)
