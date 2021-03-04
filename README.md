# QA-Project

Basic API for interact with The Movie DB, Based on Serverless Framework.

Dependencies:
- Nodejs >= 10.x
- Python >= 3.7
- Serverless Framework >= 2.x.x
- API key form The Movie DB -> [here](https://www.themoviedb.org/)

### Install:
Create virtual environment for Python:
```bash
cd project-folder/ 
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt 
```
Install Severless dependencies:
```bash
npm install
```
### Deploy local: 
First set the API Key form The Movie DB on the terminal:
```bash
export API_KEY=MyApIKeY
```
Run this command:
```bash
sls offline
```
If all ok, on terminal you can see this urls:
```bash
   ...
   ┌──────────────────────────────────────────────────────────────────────────────────┐
   │                                                                                  │
   │   GET | http://localhost:3000/dev/requests-movie/{query}                         │
   │   POST | http://localhost:3000/2015-03-31/functions/search-movie/invocations     │
   │   GET | http://localhost:3000/dev/popular-movies                                 │
   │   POST | http://localhost:3000/2015-03-31/functions/popular-movies/invocations   │
   │                                                                                  │
   └──────────────────────────────────────────────────────────────────────────────────┘
   ...
```

### Deploy on AWS: 

Need an AWS account with minimum programmatically access. 

The deploy region are in eu-west-1, if you can change this go to serverless.yml
and change the region.

Set AWS profile:
```bash
export AWS_PROFILE=AWS-PROFILE-NAME # Available on the file ~/.aws/credentials 
```
First set the API Key form The Movie DB on the terminal:
```bash
export API_KEY=MyApIKeY
```
Run this command for deploy:
```bash
sls deploy
```
If all ok, on terminal you can see this message and interact with the API:
```bash
Service Information
service: movie-api
stage: dev
region: eu-west-1
stack: movie-api-dev
resources: 18
api keys:
  None
endpoints:
  GET - https://hbd7npb4x3.execute-api.eu-west-1.amazonaws.com/dev/requests-movie/{query}
  GET - https://hbd7npb4x3.execute-api.eu-west-1.amazonaws.com/dev/popular-movies
functions:
  search-movie: movie-api-dev-search-movie
  popular-movies: movie-api-dev-popular-movies
layers:
  None
```