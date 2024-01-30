from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        unique_industries_type = set(
            industry["industry"]
            for industry in self.jobs_list
            if industry.get("industry")
        )
        return sorted(list(unique_industries_type))
