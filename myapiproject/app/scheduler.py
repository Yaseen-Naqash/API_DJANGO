# myapp/scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from pytz import timezone
import atexit
from .tasks import myCustomFunction, run_daily_at_8am

def start():
    scheduler = BackgroundScheduler()

    # Interval Task: Every 10 minutes
    scheduler.add_job(
        myCustomFunction,
        trigger=IntervalTrigger(seconds=10),
        id='interval_10min',
        replace_existing=True
    )

    # Cron Task: Every day at 8:00 AM
    scheduler.add_job(
        run_daily_at_8am,
        trigger=CronTrigger(hour=8, minute=0, timezone=timezone('Asia/Tehran')),
        id='cron_8am',
        replace_existing=True
    )
    # CronTrigger(day_of_week='mon', hour=6, minute=15)
    # You can fine-tune your schedule like this:
    # 
    #     Field	        Meaning	        Example
    #     year	        2025,2026	    year=2025
    #     month	        1–12	        month=5
    #     day	        1–31	        day=1
    #     week	        1–53	        week=23
    #     day_of_week	0–6 (Mon–Sun)	day_of_week='mon-fri'
    #     hour	        0–23	        hour=8
    #     minute	    0–59	        minute=0
    #     second	    0–59	        second=0

    scheduler.start()
    print("🔁 Scheduler started with both interval and cron tasks")

    atexit.register(lambda: scheduler.shutdown())
