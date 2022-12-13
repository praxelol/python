import os
import time
import threading
import tracemalloc
tracemalloc.start()
import discord
#from discord_rpc import Client, Request
from discord.ext import commands

# Set the client ID for the Discord application
CLIENT_ID = "1050140950313320558"
CLIENT_SECRET = "KTN_t-gCwDLnqyLkNS_cgr050jCJVFbD"
# Set the path to the After Effects executable
AE_PATH = "C:/Program Files/Adobe/Adobe After Effects 2019/Support Files/AfterFX.exe"

# Create an instance of the Discord RPC client
rpc_client = commands.Bot(command_prefix='!', intents=discord.Intents.none())


# Connect the client to Discord
rpc_client.run(CLIENT_ID,CLIENT_SECRET)

# Define a function to update the Discord presence
def update_presence():
  # Get the name of the current After Effects project
  ae_project_name = os.environ.get("AE_CURRENT_FILE_NAME", "No project")

  # Set the presence details
  presence = {
    "details": "Editing: " + ae_project_name,
    "state": "Working on effects",
    "start": int(time.time()),
    "large_image_key": "after_effects_kbir",
    "large_image_text": "After Effects",
    "small_image_key": "after_effects_sghir",
    "small_image_text": "Working on effects"
  }

  # Update the presence with the new details
  rpc_client.set_activity(presence)

# Define a function to check if After Effects is running
def check_ae_running():
  # Use the `tasklist` command to get a list of running processes
  output = os.popen("tasklist").read()

  # Check if the "AfterFX.exe" process is in the list of running processes
  if "AfterFX.exe" in output:
    # If After Effects is running, update the Discord presence
    update_presence()
  else:
    # If After Effects is not running, clear the Discord presence
    rpc_client.clear_activity()

# Create a thread to run the `check_ae_running` function periodically
thread = threading.Thread(target=check_ae_running)

