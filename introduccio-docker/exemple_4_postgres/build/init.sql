-- Pots crear una taula, fer inserts... o crear un usuari i base de dades al teu gust
create table test(id serial primary key, name TEXT, timestamp timestamp default current_timestamp);
