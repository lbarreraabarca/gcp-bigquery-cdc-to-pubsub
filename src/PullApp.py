from com.data.factory.adapters.PubSubOperator import PubSubOperator
from com.data.factory.utils.Env import Env


def process():
    env = Env()
    pub_sub = PubSubOperator(env.pub_sub.project_id)
    pub_sub.get_connection()
    pub_sub.pull(env.pub_sub.subscription_name)


process()
