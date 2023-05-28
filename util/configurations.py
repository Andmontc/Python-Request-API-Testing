import configparser

def getConfig():
    config = configparser.ConfigParser()
    config.read('Util/properties.ini')
    return config
