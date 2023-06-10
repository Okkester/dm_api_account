from setuptools import setup

REQUIRES = [
    'requests',
    'allure-pytest'
]

setup(
    name='dm_api_account',
    version='0.0.1',
    packages=['dm_api_account'],
    url='https://github.com/Okkester/dm_api_account.git',
    license='MIT',
    author='d.anofriev',
    author_email='-',
    install_requires=REQUIRES,
    description='dm_api_account with allure and logger'
)
