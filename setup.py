from setuptools import setup


with open('README.md', encoding='utf-8') as f:
    readme = f.read()


setup(
    name='tom-the-bomb',
    url='https://github.com/jay3332/tom-the-bomb',
    project_urls={
        "Issue tracker": "https://github.com/jay3332/tom-the-bomb/issues",
    },
    version='2039845.245908.234598',
    packages=[
        'tom_the_bomb'
    ],
    license='MIT',
    description='the bomb the tom the bomb tom the bomb the bomb the tom',
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    python_requires='>=3.7.0',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
