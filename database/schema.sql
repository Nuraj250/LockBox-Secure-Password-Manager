CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique identifier for each password entry
    website TEXT,  -- Stores the website or service name
    username TEXT,  -- Stores the username or email associated with the account
    password TEXT  -- Stores the encrypted password for the account
);
