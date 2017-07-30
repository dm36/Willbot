from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class BugPlugin(WillPlugin):
     
     @hear("(?:ran into )?a bug", include_me=True)
     def log_all_bugs(self, message):
         # Awesome stuff
         self.reply(message, "Oh no I hate bugs!")
