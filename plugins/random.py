from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class RandomPlugin(WillPlugin):
     @randomly(start_hour='10', end_hour='17', day_of_week="mon-fri", num_times_per_day=5)
     def walkmaster(self):
         self.say("@all time for a walk!")
