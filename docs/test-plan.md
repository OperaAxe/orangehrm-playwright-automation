# OrangeHRM automation test plan

## Objective

Validate core, externally observable user journeys in the public OrangeHRM Open Source demo using repeatable browser automation.

## Target

- Application: OrangeHRM Open Source demo
- URL: https://opensource-demo.orangehrmlive.com/
- Observed version label: OrangeHRM OS 5.9
- Initial live inspection: 3 November 2026

The demo is shared and mutable. Data, credentials, page content, and availability may change without notice.

## In scope

1. Login page loads with username/password inputs, masked password input, Login action, and displayed public demo credential hints.
2. Valid demo credentials authenticate successfully and open the Dashboard.
3. The Dashboard shows its primary navigation and the widgets observed during the live smoke pass.
4. Directory search supports employee-name autocomplete and returns the expected Linda Anderson record.

## Out of scope

- Creating, editing, or deleting employees or users.
- Submitting, approving, or rejecting leave requests.
- Clocking in/out or modifying timesheets and attendance.
- Changing configuration, access permissions, or system settings.
- Security testing, load testing, and penetration testing.

## Test data

The login defaults are copied from the public credentials displayed on the OrangeHRM demo login screen (Admin / admin123). The Directory test searches for the existing demo employee Linda Anderson and does not alter the record.

## Execution approach

- Python + pytest for test organisation and assertions.
- Playwright for browser interaction.
- Fresh browser page/context per test using the pytest-playwright fixtures.
- GitHub Actions runs the smoke suite on pushes, pull requests, and manual dispatch.

## Evidence and triage

Capture the failing assertion, URL, browser output, and relevant screenshot/trace if a run fails. Do not classify a timeout or public-demo outage as a product bug until the failure is reproduced and isolated.
