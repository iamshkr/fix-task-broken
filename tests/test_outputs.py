import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load_report():
    with REPORT.open() as f:
        return json.load(f)


def test_report_exists():
    """Success criterion: The agent saves its findings to /app/report.json."""
    assert REPORT.exists(), "report.json was not created"


def test_report_contains_required_fields():
    """Success criterion: The report is valid JSON containing total_requests, unique_ips, and top_path."""
    report = load_report()
    assert set(report.keys()) == {
        "total_requests",
        "unique_ips",
        "top_path",
    }


def test_total_requests():
    """Success criterion: total_requests equals the number of requests in access.log."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success criterion: unique_ips equals the number of unique client IP addresses."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Success criterion: top_path is the most frequently requested path."""
    report = load_report()
    assert report["top_path"] == "/index.html"
