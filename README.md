# PAI solution for case "MFC" - Hackathon SPb 2023

Python console app that using AI models: Yake! and SpaCy, solves MFC problem - MFC employees can't search answers for clients requests in automatic mode. Packed with Docker.

### Features
   * Implemented flexible search settings. By running the database_edtior.py file with properly configured parameters: setting the number of keywords to search, how we search for the most "similar" set of keywords, we can adjust the relevancy of the issue
### Prerequisites

#### Docker

  * Docker engine v1.13 or higher. See [https://docs.docker.com/engine/installation](https://docs.docker.com/engine/installation)

### How to run

#### 1. Open Project Directory and Build Docker Image

    docker build -t pai-solution-spb .

#### 2. Run

    docker run -i pai-solution-spb

### Alternative way to run

#### 1. Get the Docker Image from remote

    docker pull bialger/pai-solution-spb .

#### 2. Run

    docker run -i bialger/pai-solution-spb

## Authors - PAI

**Maksim Ryzhevnin, Alexander Bigulov, Egor Smirnov, Vyacheslav Atamanyuk, Vladimir Chumakov**
