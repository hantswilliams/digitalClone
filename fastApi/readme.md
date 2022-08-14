# Using Fast API 

## instructions to run 
- `uvicorn main:app --reload` 
- or use the `startDev.sh` script 
- can find interactive docs at `/docs` provided by swagger 
- can find interactive docs at `/redoc` provided by ReDoc 
- on local machine, currently using: `pyenv shell 3.8.6` environment 


## launching for 'production' purposes with gunicorn: 
- `gunicorn -w 2 -b :8080 -t 300 -k uvicorn.workers.UvicornWorker —-log-config log.ini --reload main:app` 
- or use the `startProduction.sh` script 