# Logging Functions for OS-Setup

# import
import datetime

# Start new log
def log_start():
    # Create log
    try:
        current_time = str(datetime.datetime.now())
        log_name = str(current_time + " - OS-Setup.log")
        log_name = log_name.replace(":", ".")
        active_log = open(log_name, "a+")
        starting_lines = "---------- OS-Setup Log ---------- \n" + current_time + " - Log Start \n"
        active_log.write(starting_lines)
    except:
        print("WARNING: Unable to start and/or write to log, logging will be unavailable")
    finally:
        active_log.close()
    return(log_name)

# Add warning to log
# Desc: Adds a warning to the log, optionally writes to terminal (default True)
def log_warn(log_name, message, write_term = True):
    current_time = str(datetime.datetime.now())
    try:
        active_log = open(log_name, "a+")
        active_log.write(current_time + " - WARNING: " + message + "\n")
    except:
        1 + 1
    finally:
        active_log.close()
        if write_term == True:
            print("WARNING: " + message)

# Exit with error and log
# Desc: Exit with a fatal error, incl. log_name and message, always writes to terminal
def log_fatal(log_name, message):
    current_time = str(datetime.datetime.now())
    try:
        active_log = open(log_name, "a+")
        active_log.write(current_time + " - Fatal Error: " + message + "\n")
    except:
        1 + 1
    finally:
        active_log.close()
        exit("Fatal Error: " + message)

# Log event
# Desc: Adds an event to the log, optionally writes event to terminal (default false)
def log_event(log_name, message, write_term = False):
    current_time = str(datetime.datetime.now())
    try:
        active_log = open(log_name, "a+")
        active_log.write(current_time + " - Event: " + message + "\n")
    except:
        1 + 1
    finally:
        active_log.close()
        # Print to terminal if selected
        if write_term == True:
            print("Event: " + message)

# Log exit
# Desc: Logs an intended exit of the program, always writes to terminal
def log_exit(log_name, message):
    current_time = str(datetime.datetime.now())
    try:
        active_log = open(log_name, "a+")
        active_log.write(current_time + " - Exit: " + message + "\n")
    except:
        1 + 1
    finally:
        active_log.close()
        exit("Exit: " + message)