from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        unique_max_salaries = {
            int(max_salary["max_salary"])
            for max_salary in self.jobs_list
            if max_salary.get("max_salary").isdigit()
        }
        return max(unique_max_salaries)

    def get_min_salary(self) -> int:
        unique_min_salaries = {
            int(min_salary["min_salary"])
            for min_salary in self.jobs_list
            if min_salary.get("min_salary").isdigit()
        }
        return min(unique_min_salaries)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        min_salary = job.get("min_salary")
        max_salary = job.get("max_salary")

        if min_salary is None or max_salary is None:
            raise ValueError("Ambos os salários devem estar presentes")

        if not (str(min_salary).isdigit() and str(max_salary).isdigit()):
            raise ValueError("os valores de salário precisam ser numéricos")

        if float(min_salary) > float(max_salary):
            raise ValueError("o salário mínimo é maior que o máximo")

        if not (str(salary).isdigit() or isinstance(salary, (int, float))):
            raise ValueError("Salary must be a number")

        return float(min_salary) <= float(salary) <= float(max_salary)

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
