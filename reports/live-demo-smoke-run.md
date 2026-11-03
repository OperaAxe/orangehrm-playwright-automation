# OrangeHRM live-demo smoke run

**Date:** 3 November 2026  
**Target:** https://opensource-demo.orangehrmlive.com/  
**Observed footer/version:** OrangeHRM OS 5.9  
**Execution:** Hosted browser interaction against the live public demo

## Results observed

| Check | Result | Evidence |
|:--|:--:|:--|
| Login page loads | PASS | Login heading, Username and Password inputs, Login button, and public demo credential hints were visible |
| Valid login | PASS | Public demo credentials opened /web/index.php/dashboard/index |
| Dashboard shell | PASS | Dashboard heading, side navigation, and six observed dashboard widgets loaded |
| Directory page | PASS | Directory page opened; Employee Name autocomplete, Job Title and Location filters, Reset and Search buttons appeared |
| Directory initial data | PASS | Page displayed 49 records before filtering |
| Directory name search | PASS | Selecting the Linda Anderson autocomplete suggestion and searching returned (1) Record Found and a single Linda Anderson card |

## Dashboard observations

The live dashboard displayed:

- Time at Work
- My Actions
- Quick Launch
- Employees on Leave Today
- Employee Distribution by Sub Unit
- Employee Distribution by Location

The side navigation included Admin, PIM, Leave, Time, My Info, Performance, Dashboard, Directory, and Maintenance.

## Notes and limitations

- This is a record of the observed live browser smoke pass, not a claim that the committed local pytest suite had already been executed in that same session.
- The demo is shared; record counts and employee names can change.
- The test pass was read-only after login. No employee, attendance, leave, or configuration data was created or modified.
- The repeatable Playwright checks are in tests/ and are wired to GitHub Actions. Use the workflow badge in the repository README to see the latest CI execution.
