import datetime
import os

# Get current time and system details
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
try:
  user = os.getlogin()
except OSError:
  user = os.environ.get("USER") or os.environ.get("USERNAME") or "Unknown"

# Create log message
log_message = f"Workflow check successful at {now} by user: {user}\n"

# Write to a log file
with open("workflow_log.txt", "a") as f:
  f.write(log_message)

print(log_message.strip())
#Done
