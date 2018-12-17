# Simple rest API using flask

- Run `scripts/deploy.sh <username> <imagename> <tag>` to build docker image
- Run `scripts/run.sh <username> <imagename> <tag>` to run that image locally

To test the POST method use the node script `scripts/make_request.js`, the command line arguments are numbers to be summed.

For example:
```bash
node scripts/make_request.js 2 4 90.3
```
returns
```bash
result = 96.3
```

Use debug=True for development locally
Use debug=False for deployment using Docker image via nginx


