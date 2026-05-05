# import os
# import requests
# from dotenv import load_dotenv
#
# # Load environment variables from a .env file
# load_dotenv()
#
# # Retrieve the BASE_URL from the environment
# BASE_URL = os.getenv("BASE_URL")
#
# def get(endpoint, headers=None, params=None):
#     url = f"{BASE_URL}{endpoint}"
#     response = requests.get(url, headers=headers, params=params)
#     return response
#
# def post(endpoint, headers=None, body=None):
#     url = f"{BASE_URL}{endpoint}"
#     response = requests.post(url, headers=headers, json=body)
#     return response
#
# def put(endpoint, headers=None, body=None):
#     url = f"{BASE_URL}{endpoint}"
#     response = requests.put(url, headers=headers, json=body)
#     return response
#
# def patch(endpoint, headers=None, body=None):
#     url = f"{BASE_URL}{endpoint}"
#     response = requests.patch(url, headers=headers, json=body)
#     return response
#
# def delete(endpoint, headers=None):
#     url = f"{BASE_URL}{endpoint}"
#     response = requests.delete(url, headers=headers)
#     return response


import requests
import os
import sys
from dotenv import load_dotenv

# Path fix to allow imports from parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from required.logger import get_logger

# Load environment variables
load_dotenv()
BASE_URL = os.getenv("BASE_URL")

# Initialize logger using the current module name
logger = get_logger(__name__)

def get(endpoint, headers=None, params=None):
    url = f"{BASE_URL}{endpoint}"
    logger.info(f"GET {url}")
    response = requests.get(url, headers=headers, params=params)
    logger.info(f"Response Status: {response.status_code}")
    logger.debug(f"Response Body: {response.text}")
    return response

def post(endpoint, headers=None, body=None):
    url = f"{BASE_URL}{endpoint}"
    logger.info(f"POST {url}")
    logger.debug(f"Request Body: {body}")
    response = requests.post(url, headers=headers, json=body)
    logger.info(f"Response Status: {response.status_code}")
    logger.debug(f"Response Body: {response.text}")
    return response

def put(endpoint, headers=None, body=None):
    url = f"{BASE_URL}{endpoint}"
    logger.info(f"PUT {url}")
    logger.debug(f"Request Body: {body}")
    response = requests.put(url, headers=headers, json=body)
    logger.info(f"Response Status: {response.status_code}")
    logger.debug(f"Response Body: {response.text}")
    return response

def patch(endpoint, headers=None, body=None):
    url = f"{BASE_URL}{endpoint}"
    logger.info(f"PATCH {url}")
    logger.debug(f"Request Body: {body}")
    response = requests.patch(url, headers=headers, json=body)
    logger.info(f"Response Status: {response.status_code}")
    logger.debug(f"Response Body: {response.text}")
    return response

def delete(endpoint, headers=None):
    url = f"{BASE_URL}{endpoint}"
    logger.info(f"DELETE {url}")
    response = requests.delete(url, headers=headers)
    logger.info(f"Response Status: {response.status_code}")
    logger.debug(f"Response Body: {response.text}")
    return response