import os, sys
pardir = os.path.dirname(os.path.dirname(os.path.abspath((__file__))))
sys.path.append(pardir)
sys.dont_write_bytecode = True

import uvicorn
from routers import api

if __name__ == '__main__':
    uvicorn.run("app:api", host='0.0.0.0', port=8000, debug=True, reload=True)
    