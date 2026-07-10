# Task

An Apache-style access log is available at `/app/access.log`.

Analyze the log and create a JSON file named `/app/report.json`.

The JSON object **must contain exactly these three fields**:

```json
{
  "total_requests": <integer>,
  "unique_ips": <integer>,
  "top_path": "<string>"
}
```

## Definitions

- **total_requests**: Total number of non-empty log entries in `access.log`.
- **unique_ips**: Number of distinct client IP addresses (the first field on each log line).
- **top_path**: The request path that appears most frequently in the log (for example, `/index.html`). If there is a tie, return any one of the most frequent paths.

## Success Criteria

1. A file named `/app/report.json` is created.
2. The file contains valid JSON with exactly the keys:
   - `total_requests`
   - `unique_ips`
   - `top_path`
3. `total_requests` equals the number of requests in `/app/access.log`.
4. `unique_ips` equals the number of distinct client IP addresses in `/app/access.log`.
5. `top_path` equals the most frequently requested path in `/app/access.log`.
