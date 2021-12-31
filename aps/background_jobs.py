from django.core.checks import messages
from django.db import transaction 
from apscheduler.schedulers.background import BackgroundScheduler
from saros.models import SarosLog
from aps.models import APS

@transaction.atomic 
def delete_inactive_aps():
    SarosLog.objects.create(message=f"Deletion of inactive aps job initialized.")
    aps = APS.objects.filter(active=False)
    SarosLog.objects.create(message=f"Total {aps.count()} to be removed.")
    try:
        aps.delete()
    except Exception as exception:
        SarosLog.objects.create(message=f"Failed to delete!")
        return None 
    SarosLog.objects.create(message=f"Deletion complete!")

def start():
    schedule = BackgroundScheduler()
    schedule.add_job(delete_inactive_aps, "cron", minute=1, max_instances=1)
    schedule.start()
