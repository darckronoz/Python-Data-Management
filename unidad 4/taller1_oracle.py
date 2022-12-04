from sqlalchemy import create_engine
import cx_Oracle
import pandas as pd


#important: instant client library solution.
oracle_instant_client_path = "C:\oracle_instant_client\instant_client_12.2\instantclient_21_3"
cx_Oracle.init_oracle_client(lib_dir=oracle_instant_client_path)
engine = create_engine("oracle://hr:123@localhost/orcl")

querys = ['select FIRST_NAME, LAST_NAME, SALARY from employees',
          'select FIRST_NAME, LAST_NAME, SALARY from employees where SALARY > 10000',
          "select FIRST_NAME, LAST_NAME, SALARY from employees order by SALARY desc",
          "select FIRST_NAME, LAST_NAME, SALARY from employees order by SALARY asc",
          "select FIRST_NAME from employees where FIRST_NAME like 'L%%'", 'select count(*) from employees',
          'SELECT e.department_id, department_name, COUNT(*) FROM employees e INNER JOIN departments d ON '
          'd.department_id = e.department_id GROUP BY e.department_id, department_name',
          'SELECT salary, first_name from employees where salary in(select max(salary) from employees)',
          ' SELECT salary, first_name from employees where salary in(select min(salary) from employees)',
          'select trunc(avg(salary), 2) as promedio from employees',
          'select trunc(avg(salary), 2) as promedio, department_name from employees e inner join departments d on '
          'e.department_id = d.department_id group by e.department_id, department_name',
          "select to_char(hire_date, 'mm') as month, count(*) as employees from employees group by to_char(hire_date, "
          "'mm') order by to_char(hire_date, 'mm')",
          "select FIRST_NAME from employees  where lower(FIRST_NAME) like 'st%%'",
          "select FIRST_NAME from employees where FIRST_NAME like '%%s'",
          "select em.FIRST_NAME from employees em  where instr(lower(em.FIRST_NAME),'mar') > 0",
          "select em.FIRST_NAME from employees em  where REGEXP_LIKE(lower(em.FIRST_NAME), '[i, o, u]+s')"]

df = pd.read_sql_query(querys[2], engine)
print(df)
