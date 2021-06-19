---
@InProceedings{kula2019releasing,
  author    = {Kula, Elvan and Rastogi, Ayushi and Huijgens, Hennie and Deursen, Arie van and Gousios, Georgios},
  booktitle = {Proceedings of the 2019 27th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering},
  title     = {Releasing fast and slow: an exploratory case study at ING},
  year      = {2019},
  pages     = {785--795},
  groups    = {forward_1, mantyla2015rapid, daCosta2016impact, hemmati2015prioritizing, khomh2015understanding, clark2014moving, selected, Other Studies},
}
---

# RQ1. What characterizes a rapid release cycle?

The authors used the mean of the distribution of release frequencies of the projects in ING, a large multinational financial organization with about 54,000 employees and over 37 million customers. They considered 3 weeks a rapid release.

# RQ2. What are the implications of adopting a rapid release cycle?

 1. Rapid teams perceive to be, and in reality are, more commonly delayed than their non-rapid counterparts.
   
 2. Dependencies, especially in infrastructure, and testing are the top mentioned delay factors in rapid releases.

 3. Developers perceive the smaller changes and rapid feedback in rapid releases to improve code quality

 4. The developers reported experiencing an increased deadline pressure in rapid release, which negatively affects the code quality, leads to an increase in workarounds and poor implementation choices. They also reported that rapid release cut the overall time spent on refactoring and regression testing.

 5.The cyclomatic complexity and coding issues are significantly lower in the rapid release cycle, which corresponds with the perception of developers that it gets easier to review and refactor code in a rapid release cycle.

 6. The branch coverage is significantly higher in the rapid release cycle. This result corresponds with the perception that the test process becomes more continuous and allows for more complete testing of new features.
   
 7.  The code churn is significantly higher for the rapid release cycle, indicating that there is a higher coding activity in rapid teams than in traditional teams.
   
 8. There is no significant difference between the comment density and SLOC of RRs and TRs.

# RQ3. What metrics do the studies use to compare rapid and traditional releases?

  - Coding Standard Violations: the number of times the source code violates a coding rule. 
  - Branch Coverage: the average coverage by tests of branches in all files contained in a release.
  - Comment Density: the percentage of comment lines in the source code. 
  - Code Churn: the number of changed lines of code between two consecutive releases.
  - Release delay: the difference between the planned release date and actual release date.

# RQ4. How do the studies mine release information?

The authors extracted the SonarQube measurements of releases. They classified the releases as traditional or rapid based on the time interval between their release date and the start date of the development phase.

Since SonarQube does not account for differences in project size, they normalized the metrics by dividing them by Source Lines of Code (SLOC): the total number of lines of source code contained in a release. Also, they normalized code churn by dividing it by the time interval between the release date and the start date of the development phase.

They also extracted log data from ServiceNow, a backlog management tool used by most teams at ING.

# RQ5. How do the studies evaluate their findings?

The authors conducted a mixed-methods study, consisting of a survey with 461 engineers, and a statistical analysis of 2 years (2016-2018) of code quality data for 611 teams.

They performed a statistical test (Mann-Whitney U test and Cliff’s delta) of the metrics between the group of rapid and traditional releases.

# RQ6. What corpus do the studies use to compare rapid and traditional releases?

  - Survey with 461 engineers from ING;
  - 2 years of code quality data for 611 teams from ING (433 rapid teams and  178 non-rapid teams)
  - Major releases of 3048 software projects.
