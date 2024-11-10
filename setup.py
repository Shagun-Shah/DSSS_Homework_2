from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    description="A simple and interactive command-line math quiz game",
    author="Shagun Shah",
    author_email="shagun.shah2@fau.de",
    packages=find_packages(),
    install_requires=[],  # Add dependencies if any
    python_requires='>=3.6',  # Specify Python version requirement
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz"
        ]
    },
)