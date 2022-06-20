"""Sopel DUM-E package."""

from sopel import module
from sopel.bot import SopelWrapper
from sopel.config import Config
from sopel.trigger import Trigger


def configure(config: Config):
    """Configure the plugin."""


def setup(bot: SopelWrapper):
    """Set up the bot."""


@module.commands('helloworld')
def hello_world(bot: SopelWrapper, trigger: Trigger):
    """Respond to a simple command."""
    bot.say('Hello, world!')
