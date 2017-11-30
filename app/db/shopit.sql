USE shopit;

DROP TABLE IF EXISTS user;
CREATE TABLE user
(
    id                  varchar(255) NOT NULl,
    username            varchar(20) NOT NULL,    # main email address serve as username
    ip                  varchar(20) NOT NULL,
    device              varchar(50) NOT NULL,

    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS auth;
CREATE TABLE auth
(
    id                  varchar(255) NOT NULL,
    email               varchar(20)  NOT NULL,
    credential          varchar(1000),
    FOREIGN KEY (id)
    REFERENCES user(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    
    PRIMARY KEY (id, email)
);

DROP TABLE IF EXISTS `order`;
CREATE TABLE `order`
(
    id                  varchar(255) NOT NULL,
    email               varchar(20)  NOT NULL,
    last_order          datetime,
    FOREIGN KEY (id)
    REFERENCES user(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    
    PRIMARY KEY (id, email)
);
