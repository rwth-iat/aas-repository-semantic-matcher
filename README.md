# AAS Repository Semantic Matcher

This is a proof-of-concept implementation for a simple semantic matcher for an AAS Repository.

Here's what it does:
- It connects to an existing AAS Repository Server
- It queries and indexes all the `semanticIDs` of the Submodels stored in that Repository Server
- It returns the semantically equivalent `semanticIDs` in a specific format needed for `Submodel Conformance Checking`

## How to run

### Option 1: Via Python Script
In order to run this script directly, you first need to install the dependencies: 

> [!note]
> We advise you to create a virtual environment to install the dependencies and run the script.

```bash
pip install -r requirements.txt
```

Then, you can run the script via: 

```bash
python aas_repository_semantic_matcher/matcher.py "http://localhost:8080/api/v3.0" 
```
where `"http://localhost:8080/api/v3.0"` is the endpoint of the AAS Repository Server.

### Option 2: Via Docker
In order to run the script via Docker, you first need to build the container from the `Dockerfile`:

```bash
sudo docker build -t aas_repository_matcher .
```

Hereby, `aas_repository_matcher` is the name you want to give the image. 

Then, you can run a container based on this image: 

```bash
sudo docker run -e REPOSITORY_ENDPOINT="http://host.docker.internal:8080/api/v3.0" aas_repository_matcher
```
where `REPOSITORY_ENDPOINT` specifies the endpoint of the AAS Repository Server and
`aas_repository_matcher` is the name you gave the image in the command above.

> [!note]
> Your `http://localhost` on the Docker Host is accessible via `http://host.docker.internal` inside the container,
> so you need to adapt the endpoint accordingly. All other endpoints e.g. `https://iat.rwth-aachen.de` 
> should work without adjustment. 
