# Repository for 'We are Plants' website

## Dockerized: Django backend, Vue js frontend, Nginx sever.

### Branch Structure:
#### master:
version of code used for production.
  
#### dev:
version of code used for development.
  
#### feature/*:
  version of code for current feature development.
  
  
  
### Pipelines:
#### Integration:
CI pipeline in github actions runs when feature branch is updated or pull request is made to the dev branch.

#### Deployment:
CD pipeline in github actions runs when dev branch is updated or pull request is made to the master branch.\
CD pipeline pushes the latest docker images to github packages.\



### Build:
#### For Development:
run 'docker-compose --build up' to run backend and frontend in containers with live update and debug enabled.

#### For Production:
run 'docker-compose -f docker-compose.prod.yaml up'\
the production docker-compose file pulls docker images for the backend and server from github packages, ready for deployment.

