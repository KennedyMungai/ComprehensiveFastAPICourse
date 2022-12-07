-- Active: 1670320493036@@127.0.0.1@3306@fastapicoursedb
-- ------------------------------------------
-- ------------------------------------------
-- A simple insert statement for the Posts table
-- ------------------------------------------
-- ------------------------------------------
INSERT INTO Posts (title, content)
VALUES(
        "The first title",
        " pariatur voluptatem officia. Sed iure odio eaque, quidem sunt officiis quam debitis, inventore enim sequi tempore, aperiam ducimus accusantium ullam. Veritatis vel porro reiciendis voluptatum repellendus autem incidunt quidem?"
    );
-- ------------------------------------------
-- ------------------------------------------
-- Select all the data from the Posts table
-- ------------------------------------------
-- ------------------------------------------
SELECT *
FROM `Posts`