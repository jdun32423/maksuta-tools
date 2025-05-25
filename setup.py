from setuptools import setup, find_packages

setup(
    name='maksuta-tools',
    version='0.1',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    include_package_data=True,
    description='Колекція інструментів OSINT, генерації та кібербезпеки',
    author='jdun32423 (@zxc_defoltik)',
    license='MIT',
)
