from setuptools import setup

setup(
    name='WolframAlphaDiscordBot',
    version='1.1',
    packages=['WADiscordBot'],
    url='https://github.com/The-Bow-Hunter/WolframAlphaDiscordBot',
    license='MIT',
    author='Tom Mucke',
    author_email='tom.mucke@web.de',
    description='Easy to use and understand Wolfram Alpha Discord Bot using the Wolfram simple API',
    install_requires=['discord.py',
                      'requests'],
    python_requires='>=3.5.3'
)
