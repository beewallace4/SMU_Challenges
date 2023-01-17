-- Queries

-- 1) List the following details of each employee: 
-- employee number, last name, first name, sex, and salary.
Select
	e.emp_no as employee_number, 
	e.last_name, 
	e.first_name, 
	e.sex, 
	s.salary
From 
	employees e
	join salaries s on e.emp_no = s.emp_no
	order by e.last_name asc
	limit 40;

-- 2) List first name, last name, and hire date
-- for employees who were hired in 1986.
Select  
 	e.first_name,
 	e.last_name,
 	e.hire_date
From 
	employees as e
Where 
	e.hire_date between '1986-01-01' and '1986-12-31'
Order by e.hire_date desc;

-- 3) List the manager of each department 
-- with the following information:
-- department number, department name,
-- the manager's employee number, 
-- last name, first name.

Select 
	dm.dept_no as department_number,
	d.dept_name as department_name,
	dm.emp_no as manager_employee_number,
	e.last_name, 
	e.first_name 
From 
	employees as e
	join dept_manager as dm on e.emp_no = dm.emp_no
	join departments as d on d.dept_no = dm.dept_no;

-- 4) List the department of each employee with the following information: 
-- employee number, last name, first name, and department name.

Select 
	e.emp_no as employee_number,
	e.last_name,
	e.first_name,
	d.dept_name as department_name
From 
	employees as e
	join dept_emp as de on e.emp_no = de.emp_no
	join departments as d on d.dept_no = de.dept_no;

-- 5) List first name, last name, and sex for employees 
-- whose first name is "Hercules" and last names begin with "B."

Select 
  e.first_name,
  e.last_name, 
  e.sex
From employees as e
Where e.first_name = 'Hercules' and e.last_name like 'B%';

-- 6) List all employees in the Sales department, 
-- including their employee number, last name, first name, 
-- and department name.

Select 
	de.emp_no as employee_number,
	e.last_name, 
	e.first_name,
	d.dept_name as department_name
From 
	employees as e
	join dept_emp as de on e.emp_no = de.emp_no
	join departments as d on d.dept_no = de.dept_no
Where 
	d.dept_name = 'Sales';

-- 7) List all employees in the Sales and Development departments,
-- including their employee number, last name, first name, 
-- and department name.

Select 
	de.emp_no as employee_number,
	e.last_name, 
	e.first_name,
	d.dept_name as department_number
From 
	employees as e
	join dept_emp as de on e.emp_no = de.emp_no
	join departments as d on d.dept_no = de.dept_no
Where 
	d.dept_name in ('Sales', 'Development');

-- 8) List the frequency count of employee last names 
-- (i.e., how many employees share each last name) 
-- in descending order.

Select
	e.last_name,
	Count(*) as num_emps
From 
	employees e
Group by
	e.last_name
Order by num_emps desc
Limit 40;





















