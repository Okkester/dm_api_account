from setuptools import setup, find_packages

REQUIRES = [
    'requests',
    'allure-pytest',
    'pydantic',
    'structlog'
]

setup(
    name='dm_api_account',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/Okkester/dm_api_account.git',
    license='MIT',
    author='d.anofriev',
    author_email='-',
    install_requires=REQUIRES,
    description='Account client with allure and logger'
)
