from setuptools import setup

setup(
    name="cron-parser",
    author="Naman Aneja",
    description="A simple cron expression parser",
    entry_points={
        "console_scripts": [
            "cron-parser = src.cli:cli"
        ]
    },
    python_requires='>=3.6',
)