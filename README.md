# Image Editing

This service contains an image editing service.

It also contains a Dockerized Jupyter Notebook environment, just in case you only have Docker installed and don't have Python.

Sections 2 and 3 assume you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed. As of 2022-12-10, Docker Desktop is free for individual users.

## Section 1: Contents

```
.
├── data          # Persistent data
├── devsecops     # Deployment, environment, and operations code
│   └── local     # Local deployment code
├── documentation # Human-readable documentation
└── src           # Application code
```

## Section 2: Instantiation

### 2.1: Local

1. Open Docker Desktop and start the Docker Engine.
2. Open a command line terminal.
3. Change directories to the directory that contains this [README.md](README.md) file.
4. Run this command:
    ```
    docker-compose -f devsecops/local/docker-compose.yml up
    ```

## Section 3: Access

### 3.1: Local

#### 3.1.A: From Local Machine

1. Open a web browser.
2. Go to this web address:
    ```
    http://localhost:230/?token=nsl
    ```
3. Click on the 'Click Me' Jupyter notebook listed.