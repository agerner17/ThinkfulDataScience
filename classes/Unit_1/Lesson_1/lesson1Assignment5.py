from datetime import datetime
import logging

def log_handler(msg):
    """Sends msg to the logging platform"""
    date = str(datetime.now())
    msg = date + " - " + msg
    return logging.info(msg)

def log(msg):
    """A convenience function. Adds msg to the logs with log_handler"""
    msg = str(msg)
    print("Message logged: " + msg)
    return log_handler(msg)

def addition(a, b):
    """Adds two numbers and logs the result"""
    x = a + b
    log("Adding {0} and {1} = {2}.".format(a, b, x))
    return x

addition(1, 2)
addition(2, 3)
addition(5, addition(3, 5))