from celery import shared_task

from .models import Collect


@shared_task
def deactivate_collect(collect_id):
    """
    Деактивирует определённый сбор по id, если он активен.
    """
    try:
        collect = Collect.objects.get(id=collect_id)
        if collect.is_active:
            collect.is_active = False
            collect.save()
            return f'Сбор {collect_id} больше не активен'
        return f'Сбор {collect_id} был деактивирован ранее'
    except Collect.DoesNotExist:
        return f'Сбор {collect_id} не найден'
