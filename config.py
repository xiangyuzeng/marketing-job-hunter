import os
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "jobs.db"

# Turso / libsql settings (set env vars for cloud deployment)
TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL", "")
TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN", "")

# Detect serverless environment (Vercel sets VERCEL=1)
IS_SERVERLESS = bool(TURSO_DATABASE_URL) or bool(os.environ.get("VERCEL", ""))

# Job search settings
SEARCH_TERMS = [
    "Marketing Manager",
    "Digital Marketing",
    "Content Marketing",
    "Marketing Analyst",
    "Brand Manager",
    "Marketing Coordinator",
    "Growth Marketing",
    "SEO Specialist",
    "SEM Specialist",
    "Social Media Manager",
    "Email Marketing",
    "Marketing Operations",
    "Demand Generation",
    "Product Marketing",
]
SITES = ["indeed", "linkedin", "glassdoor", "google", "zip_recruiter"]
IS_REMOTE = True
HOURS_OLD = 336  # 14 days
RESULTS_WANTED = 50  # per search term per site
COUNTRY_INDEED = "USA"
LOCATION = "USA"

# Title filtering — reject jobs that are clearly irrelevant
TITLE_EXCLUDE_PATTERNS = [
    r"software\s+engineer",
    r"developer",
    r"data\s+scientist",
    r"devops",
    r"sre",
    r"site\s+reliability",
    r"database",
    r"dba",
    r"network\s+engineer",
    r"security\s+analyst",
    r"cybersecurity",
    r"sys\s*admin",
    r"machine\s+learning",
    r"ml\s+engineer",
    r"ai\s+engineer",
    r"frontend",
    r"backend",
    r"full[\s\-]?stack",
    r"qa\s+engineer",
    r"penetration\s+test",
    r"help\s+desk",
    r"graphic\s+design",
    r"scrum\s+master",
    r"recruiter",
]

# Title keywords that always indicate a relevant job
TITLE_INCLUDE_KEYWORDS = [
    "marketing", "brand", "content", "seo", "sem",
    "social media", "digital", "growth", "demand gen",
    "email marketing", "campaign", "analytics", "advertising",
    "ppc", "copywriting", "creative", "communications",
    "media", "public relations", "pr", "influencer",
    "market research", "product marketing", "marketing ops",
    "lifecycle", "retention", "acquisition",
]

# Scheduler settings
REFRESH_INTERVAL_HOURS = 4

# Email notification settings (optional — set env vars to enable)
GMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS", "")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "")
NOTIFY_EMAIL = os.environ.get("NOTIFY_EMAIL", "")

# Dashboard URL (for email notifications)
DASHBOARD_URL = os.environ.get("DASHBOARD_URL", "")

# Server settings
HOST = "0.0.0.0"
PORT = 8889
