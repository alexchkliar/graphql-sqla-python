docker build -t image-name .
docker run -p 5000:5000 --name container-name image-name
docker stop container-name

http://localhost:5000/graphql
Simply stop container from GUI if you want to stop the server

PostgreSQL:
psql -U alexchkliar -d postgres
