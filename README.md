# Python-PostgreSQL

> Python Flask practice project for learning PostgreSQL.

[Udemy course](https://learn.udacity.com/courses/ud197)

`docker/compose.yml`: Docker compose file for Postgresql and web administration tools.\
`python/`: Python project.\
`arhive/`: Original files from course.\
`logIntoDB.sh`: Will connect to the **forum** database in Postgresql using `PSQL`.  

## Python
- `projectSetup.sh`: Create Python v-env.
- `venvActivationCMD.sh`: Will print the command required to activate the v-env.
- `installDeps.sh`: Will install the dependencies in the `requirements.txt` file.

## Docker
I replaced the `Vagrant` VM part with Docker to practice working with containers too.\
The `docker-compose` file will start a **Postgresql** server listening on local port `5432` and two web administration tools.

Several `volumes` are also created to persist database and web administration tool data.

### Postgresql

> The internal docker network ip for the server is `172.16.238.10`. **Make sure to use this IP when connecting through the web tools.**  
> Connections from the host computer can me made to `localhost`.

```
Default username: postgres
Default password: password
```

### PGAdmin
> Feature rich web administration tool. [Website](https://www.pgadmin.org/)

Will listen on local port `8000`.

```
Default username: user@mail.net
Default password: password
```
**Note:** these values can be changed in `docker/compose.yml`.

### Adminer
> Simple and lightweight web administration tool. [Docker Hub](https://hub.docker.com/_/adminer)

Will listen on local port `8080`.

**Use server details to log in.**

***