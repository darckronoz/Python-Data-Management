
from sqlalchemy import create_engine
import pandas as pd

engine  = create_engine('mariadb://root:123@localhost/hr')

querys = []

querys.append('select FIRST_NAME, LAST_NAME, SALARY from employees')
querys.append('select FIRST_NAME, LAST_NAME, SALARY from employees where SALARY > 10000')
querys.append("select FIRST_NAME, LAST_NAME, SALARY from employees order by SALARY desc")
querys.append("select FIRST_NAME, LAST_NAME, SALARY from employees order by SALARY asc")
querys.append("select FIRST_NAME from employees where FIRST_NAME like 'L%%'")
querys.append('select count(*) from employees')
querys.append('SELECT e.department_id, department_name, COUNT(*) FROM employees e INNER JOIN departments d ON d.department_id = e.department_id GROUP BY e.department_id, department_name')
querys.append('SELECT salary, first_name from employees where salary in(select max(salary) from employees)')
querys.append(' SELECT salary, first_name from employees where salary in(select min(salary) from employees)')
querys.append('select truncate(avg(salary), 2) as promedio from employees')
querys.append('select truncate(avg(salary), 2) as promedio, department_name from employees e inner join departments d on e.department_id = d.department_id group by e.department_id, department_name')
querys.append("select to_char(hire_date, 'mm') as month, count(*) as employees from employees group by to_char(hire_date, 'mm') order by to_char(hire_date, 'mm')")
querys.append("select FIRST_NAME from employees  where lower(FIRST_NAME) like 'st%%'")
querys.append("select FIRST_NAME from employees where FIRST_NAME like '%%s'")
querys.append("select em.FIRST_NAME from employees em  where instr(lower(em.FIRST_NAME),'mar') > 0")
querys.append("select em.FIRST_NAME from employees em  where lower(em.FIRST_NAME) REGEXP'[i, o, u]+s'")

df = pd.read_sql_query(querys[15], engine)
print(df)