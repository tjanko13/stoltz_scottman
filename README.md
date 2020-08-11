# stoltz_scottman

# stoltz_scottman


Build your app
```
docker build -t flask-heroku:latest .
```

Run your app
```
docker run -d -p 5000:5000 flask-heroku
```

Use Heroku (only need to login once if you save credentials)

Only use the following if you have a command line interface setup (requires homebrew)
```
heroku container:login

heroku create scott-is-awesome-demo-app

heroku git:remote -a scott-is-awesome-demo-app

heroku container:push web --app scott-is-awesome-demo-app

heroku container:release web --app scott-is-awesome-demo-app
```


Subsequent times (use the `heroku container:login` if necessary). Commit files as normal. Then...
```
git push heroku master
heroku container:push web --app scott-is-awesome-demo-app
heroku container:release web --app scott-is-awesome-demo-app
```


Remove stop, remove, and wipe all Docker stuff from your machine. Note: This will clear everything and not just Docker images from the current directory.
```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker system prune -a
```