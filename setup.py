from setuptools import setup, find_packages

# Basic setup configuration for the fingerboard bot project
setup(
    name="fingerboard_bot",
    version="1.0.0",
    description="A Telegram bot to search for fingerboard decks using Google Custom Search API",
    packages=find_packages(),
    install_requires=[
        "python-telegram-bot==20.0",
        "requests==2.31.0"
    ],
    python_requires=">=3.7",
)
