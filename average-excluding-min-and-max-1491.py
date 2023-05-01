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
        
        salary_avg = salary_total / counter
        
        return salary_avg
        
        