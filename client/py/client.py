import os
import logging
import requests
import time


def get_bool_env_var(var_name, default=False):
  """
  Reads a boolean value from an environment variable.

  Args:
    var_name: The name of the environment variable.
    default: The default value to return if the variable is not set or cannot be parsed.

  Returns:
    The boolean value of the environment variable, or the default value if there is an error.
  """

  try:
    value = os.environ.get(var_name)
    if value is None:
      return default
    return value.lower() in ['true', '1']
  except ValueError:
    return default


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    server = os.environ.get("SERVER", "0.0.0.0")
    port = int(os.environ.get("PORT", 8000))
    count = int(os.environ.get("NUM_REQUESTS", 100))
    should_sleep = get_bool_env_var("RUN_IN_SERVER", False)

    url = f"http://{server}:{port}/hello"

    for i in range(count):
        resp = requests.get(url)
        logging.info(resp.json())

    if should_sleep:
        time.sleep(86400 * 7)