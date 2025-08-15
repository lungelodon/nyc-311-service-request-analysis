```sql
-- SQL Script for NYC 311 Service Request Analysis

-- 1. Select all data from the service_requests table
SELECT * FROM service_requests;

-- 2. Count top 10 complaint types
SELECT
    Complaint_Type,
    COUNT(*) AS NumberOfRequests
FROM
    service_requests
GROUP BY
    Complaint_Type
ORDER BY
    NumberOfRequests DESC
LIMIT 10;

-- 3. Count complaints by borough
SELECT
    Borough,
    COUNT(*) AS NumberOfRequests
FROM
    service_requests
GROUP BY
    Borough
ORDER BY
    NumberOfRequests DESC;

-- 4. Calculate average resolution time by complaint type (conceptual, requires date functions)
SELECT
    Complaint_Type,
    AVG(JULIANDAY(Closed_Date) - JULIANDAY(Created_Date)) * 24 AS AverageResolutionHours
FROM
    service_requests
WHERE
    Closed_Date IS NOT NULL
GROUP BY
    Complaint_Type
ORDER BY
    AverageResolutionHours DESC;

-- 5. Find open requests older than 30 days
SELECT
    Unique_Key,
    Complaint_Type,
    Created_Date
FROM
    service_requests
WHERE
    Status = 'Open' AND JULIANDAY('now') - JULIANDAY(Created_Date) > 30;
```

