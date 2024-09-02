-- Create table
CREATE TABLE IF NOT EXISTS images (
    id SERIAL PRIMARY KEY,
    image BYTEA NOT NULL
);

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON TABLE images TO myuser;

-- Grant usage privilege on the schema
GRANT USAGE, CREATE ON SCHEMA public TO myuser;

-- Grant select privilege on sequence
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON SEQUENCES TO myuser;