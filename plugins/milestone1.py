from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
import requests

class Milestone(WillPlugin):

    @hear("!ls", include_me=True)
    def say_deployment(self, message):
        r = requests.get("http://10.60.66.28:8080/deployments/")
        json_packet = r.json()
        for deployment in json_packet:
		time_started = deployment["time_start"]
        	version = deployment["version"]
        	environment = deployment["environment"]
        	self.reply(message, time_started + " " + version + " " + environment)
