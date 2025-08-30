import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard

if __name__ == '__main__':

    total_count = Passcard.objects.count()
    active_passcards = Passcard.objects.filter(is_active=True)
    active_count = active_passcards.count()


    print('Всего пропусков:', total_count)
    print('Активных пропусков:', active_count)
    

    if active_count > 0:
        first_passcard = active_passcards.first()
        print('\nИнформация о первом активном пропуске:')
        print('owner_name:', first_passcard.owner_name)
        print('passcode:', first_passcard.passcode)
        print('created_at:', first_passcard.created_at)
        print('is_active:', first_passcard.is_active)