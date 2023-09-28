CREATE TABLE your_table_name (
	uid   int,
	subject_id int,
	score int
);

INSERT INTO your_table_name VALUES (1001, 01, 90),
(1001, 02, 90),
(1001, 03, 90),
(1002, 01, 85),
(1002, 02, 85),
(1002, 03, 95),
(1003, 01, 70),
(1003, 02, 70);

SELECT * FROM your_table_name;




WITH SubjectAverages AS (
    SELECT
        subject_id,
        AVG(score) AS avg_score
    FROM
        your_table_name
    GROUP BY
        subject_id
)

/*select a.*, b.avg_score
from your_table_name a
JOIN SubjectAverages b on a.subject_id = b.subject_id where a.score > b.avg_score;
*/

select c.uid from 
(select a.*, b.avg_score
from your_table_name a
JOIN SubjectAverages b on a.subject_id = b.subject_id where a.score > b.avg_score) c
group by c.uid having count(DISTINCT c.subject_id) = (select count(DISTINCT subject_id) from your_table_name where uid = c.uid);


/*

WITH SubjectAverages AS (
    SELECT
        subject_id,
        AVG(score) AS avg_score
    FROM
        your_table_name
    GROUP BY
        subject_id
)

select c.uid from 
(select a.*, b.avg_score, a.score- b.avg_score as diff
from your_table_name a
JOIN SubjectAverages b on a.subject_id = b.subject_id) c
group by c.uid having min(c.diff) > 0;

/*

WITH SubjectAverages AS (
    SELECT
        subject_id,
        AVG(score) AS avg_score
    FROM
        your_table_name
    GROUP BY
        subject_id
)

    SELECT DISTINCT
    uid
FROM
    your_table_name AS s
WHERE
    uid NOT IN (
        SELECT
            uid
        FROM
            your_table_name AS s1
        LEFT JOIN
            SubjectAverages AS sa
        ON
            s1.subject_id = sa.subject_id
        WHERE
            s1.score <= sa.avg_score
    );
    */
    
    /*
    WITH SubjectAverages AS (
    SELECT
        subject_id,
        AVG(score) AS avg_score
    FROM
        your_table_name
    GROUP BY
        subject_id
)

SELECT DISTINCT
    uid
FROM
    your_table_name AS s
WHERE
    NOT EXISTS (
        SELECT
            subject_id
        FROM
            SubjectAverages AS sa
        WHERE
            sa.subject_id = s.subject_id
            AND s.score <= sa.avg_score
    )
AND
    uid IN (
        SELECT DISTINCT
            uid
        FROM
            your_table_name
    );
*/
