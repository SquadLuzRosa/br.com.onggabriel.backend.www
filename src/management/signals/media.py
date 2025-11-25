from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from ..models import ManagementMedia


@receiver(pre_save, sender=ManagementMedia)
def delete_old_file_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    if old.file and old.file != instance.file:
        if old.file.storage.exists(old.file.path):
            old.file.storage.delete(old.file.path)


@receiver(post_delete, sender=ManagementMedia)
def delete_file_on_delete(sender, instance, **kwargs):
    if instance.file and instance.file.storage.exists(instance.file.path):
        instance.file.storage.delete(instance.file.path)
