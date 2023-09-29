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
        description='Real-ESRGAN aims at developing Practical Algorithms for General Image Restoration',
        long_description=readme(),
        long_description_content_type='text/markdown',
        author='Xintao Wang',
        author_email='xintao.wang@outlook.com',
        keywords='computer vision, pytorch, image restoration, super-resolution, esrgan, real-esrgan',
        url='https://github.com/xinntao/Real-ESRGAN',
        include_package_data=True,
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
        setup_requires=['cython', 'numpy'],
        install_requires=get_requirements(),
        zip_safe=False)
