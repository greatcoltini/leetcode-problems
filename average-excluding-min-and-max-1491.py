from decimal import Decimal

class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        # remove min and max salaries
        max_salary = max(salary)
        min_salary = min(salary)
        
        salary.remove(max_salary)
        salary.remove(min_salary)
        
        salary_total = 0
        counter = 0
        
        for individual in salary:
            counter += 1
            salary_total += individual
            print(salary_total)
        
        salary_avg = Decimal(salary_total) / Decimal(counter)
        
        return salary_avg
        
        