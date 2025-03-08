# 1.overall average softskill score each year.

select count(*),avg(ss.average_softskill),s.course_batch,s.graduation_year from Students s  
join soft_skills ss on s.student_id=ss.student_id group by s.graduation_year,s.course_batch 
order by s.graduation_year;

# 2.Distribution of soft skill scores .
select s.student_id,s.name,s.phone,s.email,s.course_batch,s.graduation_year,ss.communication,
ss.teamwork,ss.presentation,ss.leadership,ss.critical_thinking,ss.interpersonal_skills,
ss.average_softskill from Students s  join soft_skills ss on s.student_id=ss.student_id 
order by s.course_batch,s.graduation_year;

# 3.Top performing students in programming .
 SELECT s.student_id,s.name,s.course_batch,s.phone,s.email, language, problems_solved, 
 assessments_completed, mini_projects, certifications_earned, latest_project_score,
 (problems_solved * 0.3 + assessments_completed * 0.2 + mini_projects * 0.2 + 
 certifications_earned * 0.2 + latest_project_score * 0.1) AS performance_score
  FROM programming p inner join students s on p.student_id=s.student_id
  ORDER BY performance_score DESC LIMIT 10;
  
# 4.exceptionally high or low average soft skill scores using 1.5 stddev .
SELECT s.student_id,s.name,s.course_batch,s.phone,s.email, ss .average_softskill
FROM soft_skills ss inner join students s on ss.student_id=s.student_id
WHERE average_softskill > (SELECT AVG(average_softskill) + 1.5 * STDDEV(average_softskill) FROM soft_skills)
OR average_softskill < (SELECT AVG(average_softskill) - 1.5 * STDDEV(average_softskill) FROM soft_skills)
ORDER BY average_softskill DESC;

# 5.Average for each soft skill.
	SELECT 'Communication' AS skill, AVG(communication) AS avg_score FROM soft_skills
	UNION ALL
	SELECT 'Teamwork', AVG(teamwork) FROM soft_skills
	UNION ALL
	SELECT 'Presentation', AVG(presentation) FROM soft_skills
	UNION ALL
	SELECT 'Leadership', AVG(leadership) FROM soft_skills
	UNION ALL
	SELECT 'Critical Thinking', AVG(critical_thinking) FROM soft_skills
	UNION ALL
	SELECT 'Interpersonal Skills', AVG(interpersonal_skills) FROM soft_skills
	ORDER BY avg_score DESC;
    
# 6.Top 5 Companies Hiring the Most Students.
  SELECT company_name, COUNT(*) AS students_placed FROM placements
  WHERE placement_status = 'Placed'
  GROUP BY company_name
  ORDER BY students_placed DESC
  LIMIT 5;

# 7.students ready for placement.
select s.student_id,s.name,s.phone,s.email,s.course_batch,s.graduation_year,ss.communication,
ss.teamwork,ss.presentation,ss.leadership,ss.critical_thinking,ss.interpersonal_skills,
ss.average_softskill from students s join placements p on s.student_id=p.student_id and placement_status='Not Ready' 
join soft_skills ss on ss.student_id=p.student_id and ss.average_softskill>60 
join programming pp on ss.student_id=pp.student_id and pp.problems_solved>=350 order by ss.average_softskill desc ;

# 8.Enrollment per year and batch.
 select count(*) as no_of_student,enrollment_year,course_batch from students
 group by enrollment_year,course_batch order by enrollment_year;

# 9.Impact of internships ,Mock Interview Scores on Placement
SELECT internships_completed, 
ROUND(AVG(mock_interview_score), 2) AS avg_mock_score,
COUNT(*) AS total_students,
SUM(CASE WHEN placement_status = 'Placed' THEN 1 ELSE 0 END) AS placed_students,
(SUM(CASE WHEN placement_status = 'Placed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS placement_rate
FROM placements
GROUP BY internships_completed
ORDER BY internships_completed DESC;

# 10.Top programming students.
SELECT s.student_id,s.name,s.course_batch,s.phone,s.email,p. problems_solved
FROM programming p inner join students s on s.student_id=p.student_id
WHERE problems_solved > (SELECT AVG(problems_solved) + STDDEV(problems_solved) FROM programming)
ORDER BY problems_solved DESC;
  
  
  
  
  
  