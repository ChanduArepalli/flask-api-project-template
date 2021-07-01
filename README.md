# flask-api-project

### Packages to be install

```shell
pip install flask==1.1.2
pip install flask-SQLAlchemy
pip install psycopg2
pip install flask-migrate
pip install flask-jwt-extended

```

#### Note

- Uninstall Flask globally if you are facing the issue `No module named 'flask_sqlalchemy'` even when you installed `flask-SQLAlchemy`


### Environment Variables

Ubuntu/ Mac
```shell
export SECRET_KEY='PRODUCTION-SECRET-KEY'
# Database
export DB_DATABASE='db_name'
export DB_USERNAME='user'
export DB_PASSWORD='password'
export DB_HOST='127.0.0.1'
export DB_PORT=5432
# JWT
export JWT_SECRET_KEY='PRODUCTION-JWT-SECRET-KEY'
```

Windows
```shell
SET SECRET_KEY=PRODUCTION-SECRET-KEY
# Database
SET DB_DATABASE=db_name
SET DB_USERNAME=user
SET DB_PASSWORD=password
SET DB_HOST=127.0.0.1
SET DB_PORT=5432
# JWT
SET JWT_SECRET_KEY=PRODUCTION-JWT-SECRET-KEY
```


### To Run the project

```shell
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
