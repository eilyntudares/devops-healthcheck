import time
import json
from datetime import datetime, UTC   # ✅ updated import

import requests
import yaml


def load_services(config_path: str = "services.yaml") -> list:
    """Load services from YAML file."""
    with open(config_path, "r") as f:
        data = yaml.safe_load(f)

    # Expect a top-level key "services" with a list
    return data.get("services", [])


def check_service(service: dict) -> dict:
    """
    Check a single service.
    Expected keys:
      - name
      - url
      - expected_status
      - max_latency_ms
    """
    name = service.get("name", "unknown")
    url = service.get("url")
    expected_status = service.get("expected_status", 200)
    max_latency_ms = service.get("max_latency_ms", 1000)

    start = time.monotonic()
    status_code = None
    error = None

    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
    except Exception as e:
        error = str(e)

    latency_ms = (time.monotonic() - start) * 1000

    healthy = (
        error is None
        and status_code == expected_status
        and latency_ms <= max_latency_ms
    )

    return {
        "name": name,
        "url": url,
        "status_code": status_code,
        "expected_status": expected_status,
        "latency_ms": round(latency_ms, 2),
        "max_latency_ms": max_latency_ms,
        "healthy": healthy,
        "error": error,
    }


def run_healthcheck():
    services = load_services()
    results = [check_service(s) for s in services]

    report = {
        "checked_at": datetime.now(UTC).isoformat(),   # ✅ correct usage
        "summary": {
            "total": len(results),
            "healthy": sum(1 for r in results if r["healthy"]),
            "unhealthy": sum(1 for r in results if not r["healthy"]),
        },
        "services": results,
    }

    # Save report as JSON
    with open("health_report.json", "w") as f:
        json.dump(report, f, indent=2)

    # Also print a quick summary to the console
    print(f"Checked {report['summary']['total']} services.")
    print(f"Healthy:   {report['summary']['healthy']}")
    print(f"Unhealthy: {report['summary']['unhealthy']}")


if __name__ == "__main__":
    run_healthcheck()
