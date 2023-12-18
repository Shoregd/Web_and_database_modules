DROP TABLE IF EXISTS peeps;
DROP SEQUENCE IF EXISTS peeps_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name text,
    email text
);
CREATE TABLE peeps(
    id SERIAL PRIMARY KEY,
    message text,
    post_date date,
    post_time time,
    user_id int,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade
);


