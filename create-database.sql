CREATE TABLE IF NOT EXISTS "user" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(64) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(128) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS "post" (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    body TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES "user" (id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_post_created_at ON "post" (created_at);
CREATE INDEX IF NOT EXISTS idx_post_user_id ON "post" (user_id);

CREATE TABLE IF NOT EXISTS "comment" (
    id SERIAL PRIMARY KEY,
    body TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES "user" (id) ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES "post" (id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_comment_created_at ON "comment" (created_at);
CREATE INDEX IF NOT EXISTS idx_comment_user_id ON "comment" (user_id);
CREATE INDEX IF NOT EXISTS idx_comment_post_id ON "comment" (post_id);

-- Insert admin user (password: adminpass)
INSERT INTO "user" (username, email, password_hash, is_admin, created_at)
VALUES 
('admin', 'admin@example.com', 'pbkdf2:sha256:600000$g1uMlxQHu9J3Jv0p$b2ca26b7c86c35e8d6a2e4b7c5d8a5a6e4c3b2a1d0c9b8a7f6e5d4c3b2a1d0c9', TRUE, NOW() - INTERVAL '30 days');

-- Insert regular users (password: userpass)
INSERT INTO "user" (username, email, password_hash, is_admin, created_at)
VALUES 
('johndoe', 'john@example.com', 'pbkdf2:sha256:600000$g1uMlxQHu9J3Jv0p$b2ca26b7c86c35e8d6a2e4b7c5d8a5a6e4c3b2a1d0c9b8a7f6e5d4c3b2a1d0c9', FALSE, NOW() - INTERVAL '25 days'),
('janedoe', 'jane@example.com', 'pbkdf2:sha256:600000$g1uMlxQHu9J3Jv0p$b2ca26b7c86c35e8d6a2e4b7c5d8a5a6e4c3b2a1d0c9b8a7f6e5d4c3b2a1d0c9', FALSE, NOW() - INTERVAL '20 days'),
('bobsmith', 'bob@example.com', 'pbkdf2:sha256:600000$g1uMlxQHu9J3Jv0p$b2ca26b7c86c35e8d6a2e4b7c5d8a5a6e4c3b2a1d0c9b8a7f6e5d4c3b2a1d0c9', FALSE, NOW() - INTERVAL '15 days'),
('alicejones', 'alice@example.com', 'pbkdf2:sha256:600000$g1uMlxQHu9J3Jv0p$b2ca26b7c86c35e8d6a2e4b7c5d8a5a6e4c3b2a1d0c9b8a7f6e5d4c3b2a1d0c9', FALSE, NOW() - INTERVAL '10 days');

-- Note: In a real application, you would use proper password hashing through the application code
-- These are placeholder hashes for demonstration purposes