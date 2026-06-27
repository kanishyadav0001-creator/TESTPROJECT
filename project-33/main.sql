CREATE TABLE IF NOT EXISTS Hacker_news (
    sno TEXT ,
    news_channal TEXT,
    news_title TEXT,
    news_rating REAL,
    news TEXT
);

INSERT INTO Hacker_news (sno, news_channal, news_title, news_rating, news)
VALUES
('1','ZEE News','Hacker news',4.9,'*******************************************************************'),
('2','AAJ TAK','Cyber Security news',4.1,'************************************************************'),
('3', 'REPUBLIC BHARAT','Cyber news',3.8,'************************************************************'),
('4','INDIA NEWS','Hackers is not save',3,'***********************************************************'),
('5','ABP News','Hacker Alert',3.5,'******************************************************************');


SELECT * FROM Hacker_news ;

