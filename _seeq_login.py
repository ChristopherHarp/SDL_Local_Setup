import json
import os

from seeq import spy


def ensure_login():
    """Ensures the user is logged into Seeq, only if necessary."""
    if "Not logged in" in str(spy.session):
        # Get the absolute path to the credentials.json file in the project root
        credentials_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "credentials.json"
        )

        try:
            with open(credentials_path, "r") as f:
                credentials = json.load(f)  # Load credentials file
        except FileNotFoundError:
            raise FileNotFoundError(f"❌ Missing credentials file: {credentials_path}")

        # Get the customer instance from the environment variable (set in __init__.py)
        customer_instance = os.getenv(
            "SEEQ_CUSTOMER", "develop"
        )  # Default to "develop"

        if customer_instance not in credentials:
            raise ValueError(
                f"❌ No credentials found for customer: {customer_instance}"
            )

        # Load the selected customer's credentials
        customer_creds = credentials[customer_instance]
        url = customer_creds["server"]
        access_key = customer_creds["access_key"]
        password = customer_creds["password"]

        # Perform Seeq login
        spy.login(
            url=url,  # Pass correct URL
            username=access_key,  # Access key (assuming it's the username field)
            password=password,  # Password
            force=True,
            quiet=True,
        )
        print(spy.session)


# Automatically check login on import
ensure_login()
