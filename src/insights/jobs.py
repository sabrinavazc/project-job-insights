from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, "r", encoding="utf-8") as filejobs:
            jobs_reader = csv.DictReader(
                filejobs, delimiter=",", quotechar='"'
            )
            self.jobs_list = list(jobs_reader)

        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        unique_job_types = set(
            job["job_type"] for job in self.jobs_list if job.get("job_type")
        )
        return sorted(list(unique_job_types))

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
