from apscheduler.schedulers.background import BackgroundScheduler
from . import views


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(views.delete_images, trigger='cron', month='1-12', day='1', hour=0, minute=0)
    scheduler.add_job(views.calculate_storage, trigger='cron', day='1-7', hour=12, minute=0)
    scheduler.start()



