from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class MorningPlugin(WillPlugin):

    @respond_to("^good morning", include_me=True)
    def good_morning(self, message):
        self.reply(message, "swag!")
    
