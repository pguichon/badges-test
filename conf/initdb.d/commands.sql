CREATE USER sketchfab WITH PASSWORD 'sketchfab';
GRANT ALL PRIVILEGES ON DATABASE sketchfab to sketchfab;
ALTER DATABASE sketchfab OWNER TO sketchfab;
ALTER USER sketchfab CREATEDB;
