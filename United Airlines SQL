-- Calculated total handle time per call
SELECT 
    call_id, 
    (strftime('%s', call_end_datetime) - strftime('%s', call_start_datetime)) AS total_handle_time
FROM calls;

-- Calculated overall AHT
SELECT 
    SUM(strftime('%s', call_end_datetime) - strftime('%s', call_start_datetime)) / COUNT(call_id) AS AHT
FROM calls;

-- Calculated total waiting time per call 
SELECT 
    call_id, 
    (strftime('%s', agent_assigned_datetime) - strftime('%s', call_start_datetime)) AS total_waiting_time
FROM calls
WHERE agent_assigned_datetime IS NOT NULL;

-- Calculated overall AST
SELECT 
    SUM(strftime('%s', agent_assigned_datetime) - strftime('%s', call_start_datetime)) / COUNT(call_id) AS AST
FROM calls
WHERE agent_assigned_datetime IS NOT NULL;

-- Merged sentiment and call duration data
SELECT 
    s.call_id,
    s.customer_tone,
    s.agent_tone,
    s.average_sentiment,
    (strftime('%s', c.call_end_datetime) - strftime('%s', c.call_start_datetime)) AS total_handle_time
FROM sentiment_statistics s
JOIN calls c ON s.call_id = c.call_id;

-- Checked correlation between sentiment and handle time
SELECT 
    AVG((strftime('%s', call_end_datetime) - strftime('%s', call_start_datetime))) AS avg_handle_time,
    customer_tone, agent_tone
FROM sentiment_statistics s
JOIN calls c ON s.call_id = c.call_id
GROUP BY customer_tone, agent_tone;

-- Listed most frequent call reasons from the reason table
SELECT r.primary_call_reason, COUNT(c.call_id) AS frequency
FROM calls c
JOIN reason r ON c.call_id = r.call_id
GROUP BY r.primary_call_reason
ORDER BY frequency DESC;

-- Calculated the average handle time (AHT) for each primary call reason
WITH avg_aht AS (
    SELECT 
        AVG(strftime('%s', c.call_end_datetime) - strftime('%s', c.call_start_datetime)) AS overall_avg_aht
    FROM calls c
)
SELECT 
    r.primary_call_reason, 
    AVG(strftime('%s', c.call_end_datetime) - strftime('%s', c.call_start_datetime)) AS avg_handle_time
FROM calls c
JOIN reason r ON c.call_id = r.call_id
GROUP BY r.primary_call_reason
HAVING avg_handle_time > (SELECT overall_avg_aht FROM avg_aht);


-- Got the average handling time by primary call reason (focused on long AHT)
SELECT r.primary_call_reason, 
    COUNT(c.call_id) AS frequency,
    AVG(strftime('%s', c.call_end_datetime) - strftime('%s', c.call_start_datetime)) AS avg_handle_time
FROM calls c
JOIN reason r ON c.call_id = r.call_id
GROUP BY r.primary_call_reason
HAVING avg_handle_time > 1000 
ORDER BY avg_handle_time DESC;

-- Filtered calls by agent and customer tone that have the highest AHT
SELECT c.call_id, r.primary_call_reason, s.customer_tone, s.agent_tone,
    strftime('%s', c.call_end_datetime) - strftime('%s', c.call_start_datetime) AS handle_time
FROM calls c
JOIN reason r ON c.call_id = r.call_id
JOIN sentiment_statistics s ON c.call_id = s.call_id
WHERE (s.customer_tone = 'angry' OR s.agent_tone = 'angry')
ORDER BY handle_time DESC;


-- Identified frequent call reasons associated with negative customer sentiment that can be solved by IVR
SELECT r.primary_call_reason, 
    COUNT(c.call_id) AS frequency, 
    AVG(strftime('%s', c.call_end_datetime) - strftime('%s', c.call_start_datetime)) AS avg_handle_time,
    s.customer_tone
FROM calls c
JOIN reason r ON c.call_id = r.call_id
JOIN sentiment_statistics s ON c.call_id = s.call_id
WHERE s.customer_tone IN ('angry', 'frustrated') 
AND r.primary_call_reason IN ('Seating', 'Voluntary Change', 'Post-Flight')
GROUP BY r.primary_call_reason, s.customer_tone
ORDER BY frequency DESC;




