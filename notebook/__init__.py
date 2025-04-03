import os
import sys

# 🔹 Set the customer instance here
DEFAULT_CUSTOMER = "develop"  # Change to "customer1", "customer2", etc.

# Ensure the correct customer is used
if "SEEQ_CUSTOMER" not in os.environ:
    os.environ["SEEQ_CUSTOMER"] = DEFAULT_CUSTOMER

# Determine the project root dynamically
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, ".."))

# Ensure the project root is in sys.path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now you should be able to import _seeq_login
try:
    import _seeq_login
except ImportError as e:
    print(
        "⚠️ Warning: `_seeq_login.py` not found. Ensure it exists in the project root."
    )
