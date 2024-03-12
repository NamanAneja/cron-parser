from setuptools import setup
import os


base_dir = os.path.abspath(os.path.dirname(__file__))
setup(
    name="cron-parser",
    author="Naman Aneja",
    description="A simple cron expression parser",
    entry_points={
        "console_scripts": [
            "cron-parser = main:cli"
        ]
    },
    python_requires='>=3.6',
)