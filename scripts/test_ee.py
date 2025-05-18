import ee
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get project ID from environment
project_id = os.getenv("GEE_PROJECT")

# Initialize Earth Engine with project ID
ee.Initialize(project=project_id)

print("Earth Engine is initialized with project:", project_id)
