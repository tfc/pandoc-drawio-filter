from setuptools import setup, find_packages

setup(
    name="pandoc-drawio-filter",
    version="1.0",
    author="Jacek Galowicz",
    url="https://github.com/tfc/pandoc-drawio-filter",
    description="Pandoc filter that converts *.drawio images to PDF",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pandoc-drawio = pandoc_drawio_filter.pandoc_drawio_filter:main"
        ]
    },
)
