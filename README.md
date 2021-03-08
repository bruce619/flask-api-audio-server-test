A REST Web API that simulates the behavior of an audio file server.

Requirements: One of three audio files is allowed \
1. song
2. podcast
3. audiobook

Technologies:\
Flask \
PostgreSQL 

Steps: 
1. in /app_config/config.py replace SQLALCHEMY_DATABASE_URI value with your own db
2. in /api_models/models.py directory uncomment #db.create_all() and run script once to create db tables. or go to open shell in project directory, import db from app_config.app and run db.create_all(). 
3. in project directory run python routers.py terminal/cmd
   
API METHODS:
1. GET Method : base_uri/audioFileType
2. GET Method : base_uri/audioFileType/audioFileId
3. POST Method : base_uri/
4. PUT Method : base_uri/audioFileType/audioFileId
5. DELETE Method : base_uri/audioFileType/audioFileId

NB: no trailing slash for GET, PUT, DELETE api end points
