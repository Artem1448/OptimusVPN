use optimusvpn;

create table clients (
     clientId INT NOT NULL UNIQUE PRIMARY KEY,
     balance INT,
     days INT,
     regDate DATETIME,
     periodIsActive BOOLEAN DEFAULT FALSE,
     promocode VARCHAR(20) DEFAULT 'empty',
     refLink VARCHAR(100) DEFAULT 'empty'
);

create table replenishments (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    amount INT,
    datePay DATETIME,
    clientId INT NOT NULL,
    FOREIGN KEY (clientId) REFERENCES clients(clientId)
);

create table payments (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    labelRate ENUM('1month','2months','3months','6months','1year') NOT NULL,
    price INT NOT NULL,
    clientId INT NOT NULL,
    FOREIGN KEY (clientId) REFERENCES clients(clientId)
)



