from openai import OpenAI
import json


"""
@params: API_KEY: string OpenAI API key to make the requests.
@returns: The OpenAI client if connected, False either
"""
def connect(API_KEY):
    client = OpenAI(api_key=API_KEY)
    if client is not None:
        return client
    else:
        return False


"""
Load the content of config file and return it
@params: config_file: string path of the config file, json format
@returns: dictionary conversion of the json config file
"""
def config(config_file, csv_path, titles, client):
    configs = {}
    with open(config_file) as file:
        configs = json.loads(file.read())
        file.close()

    if titles == "t":
        titles = configs.get("thread_title")
    else:
        titles = configs.get("csv_title")

    with open(csv_path, "w") as file:
        file.write(titles+"\n")
        file.close()

    client = connect(configs.get("api_key"))

    return configs, client