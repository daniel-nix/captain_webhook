prefix_var = "p!"
admin_list = [489561787717648394, 497582475091116042, 331431342438875137]
moderator_list = [453380154501234688, 101063847904841728, 108792533823320064, 533775630458683393, 421338370757754880, 666466785771520020, 301912018707808257, 356996895366840321, 147529721893224448]
topic_message = "{0}"
log_channel = 702588387390914651
from secret import token_const # token_const must be your token


class bot_config:
    def __init__(self, token, prefix, admins, default_topic):
        self.prefix = prefix
        self.logs = log_channel
        self.token = token
        self.admins = admins
        self.moderators = moderator_list
        self.default_topic_message = default_topic
        
        
def get_config():
    return bot_config(token= token_const, prefix=prefix_var, admins=admin_list, default_topic=topic_message)
