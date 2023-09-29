import os

from setuptools import setup, find_packages


def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content


def get_requirements(filename='requirements_inference.txt'):
    here = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(here, filename), 'r') as f:
        requires = [line.replace('\n', '') for line in f.readlines()]
    return requires


if __name__ == '__main__':
    setup(
        name='robust_video_matting',
        version="0.0.1",
        description='Realtime Robust Video Matting',
        long_description=readme(),
        long_description_content_type='text/markdown',
        author='thegenerativegeneration',
        author_email='',
        keywords='computer vision, pytorch, video matting',
        url='https://github.com/thegenerativegeneration/RobustVideoMatting',
        packages=find_packages(),
        classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
        ],
        license='GPLv3',
        install_requires=get_requirements()
    )
