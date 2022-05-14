CREATE USER inatelloguser WITH PASSWORD 'inatelloguser' CREATEDB;
CREATE DATABASE log_db
    WITH 
    OWNER = inatelloguser
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;