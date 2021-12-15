bind = "0.0.0.0:8000"

# Access log - records incoming HTTP requests
accesslog = "Logging/gunicorn.access.log"
# Error log - records Gunicorn server goings-on
errorlog = "Logging/gunicorn.error.log"
# Whether to send Django output to the error log 
capture_output = True
# How verbose the Gunicorn error logs should be 
loglevel = "info"