from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
class Command(BaseCommand):
    help = 'Create user roles and assign permissions'
    def handle(self, *args, **kwargs):
        # set roles
        coordinator_group, created = Group.objects.get_or_create(name='Coordinator')
        member_group, created = Group.objects.get_or_create(name='Member')
        # set permissions
        publish_permission = Permission.objects.get(codename='can_publish_trail')
        view_permission = Permission.objects.get(codename='can_view_trail')
        # set permissions to groups
        coordinator_group.permissions.add(publish_permission,view_permission)
        member_group.permissions.add(view_permission)
        self.stdout.write(self.style.SUCCESS('Successfully set up the roles!'))