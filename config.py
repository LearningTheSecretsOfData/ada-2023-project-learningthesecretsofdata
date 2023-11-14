from os.path import join, dirname
from dotenv import dotenv_values

# Config object that store environment variables from .env file
config = {
    **dotenv_values(join(dirname(__file__), '.env'))
}
