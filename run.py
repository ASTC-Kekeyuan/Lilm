from main import *

socket.run(app, port=80, host="0.0.0.0",
           use_reloader=False, debug=False, log_output=True)
