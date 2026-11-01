# Codex Instructions

## General Rules
- Do not modify files unrelated to the requested task.
- Do not install new dependencies without asking.
- Do not introduce new frameworks without approval.
- Do not overengineer simple solutions.
- Prefer Python and existing project conventions.

## Code Changes
- Explain major architectural changes before implementing them.
- Preserve existing functionality unless explicitly requested.
- Do not remove existing functions without permission.
- Keep changes small and modular.
- No in-text comments needed.

## Database
- Do not delete or truncate database tables.
- Do not modify database schemas without approval.
- Do not execute destructive SQL commands.
- Do not overwrite existing data unnecessarily.

## Git
- Do not commit or push changes unless explicitly requested.
- Do not rewrite Git history.
- Do not delete branches.

## Security
- Never expose API keys or credentials.
- Do not commit .env files.
- Do not print secrets in logs.

## Testing Rules
- Run relevant tests after modifying code.
- Prefer targeted tests over the full test suite.
- Keep test output concise.
- Do not use verbose test flags unless debugging.
- Do not repeatedly retry the same failing test without changing the approach.
- Stop after 2 unsuccessful fix attempts and explain the issue.
- Mock external API calls and database operations in unit tests.
- Do not run tests that modify production data.
- Do not install dependencies without approval.
- Summarize test results and remaining failures.

## Protected Files
- Do not read, modify, or display the contents of .env files.
- Do not access credentials or API keys unless explicitly authorized.
- Use .env.example to understand required environment variables.
- Never commit secrets.
- Do not modify files listed in .gitignore unless explicitly requested.