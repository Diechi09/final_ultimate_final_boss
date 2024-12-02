import json
from .models import Restaurant, Menu, MenuSection, MenuItem, DietaryRestriction, ProcessingLog
from datetime import datetime

def save_structured_data_to_db(structured_data):
    try:
        for restaurant in structured_data["Restaurant"]:
            Restaurant.objects.update_or_create(
                id=restaurant[0],
                defaults={"name": restaurant[1], "location": restaurant[2]},
            )

        for menu in structured_data["Menu"]:
            Menu.objects.update_or_create(
                id=menu[0],
                defaults={
                    "restaurant_id": menu[1],
                    "version": menu[2],
                    "date": menu[3],
                },
            )

        for section in structured_data["MenuSection"]:
            MenuSection.objects.update_or_create(
                id=section[0],
                defaults={
                    "menu_id": section[1],
                    "section_name": section[2],
                    "order": section[3],
                },
            )

        for item in structured_data["MenuItem"]:
            MenuItem.objects.update_or_create(
                id=item[0],
                defaults={
                    "section_id": item[1],
                    "name": item[2],
                    "description": item[3],
                    "price": item[4],
                    "dietary_restriction_id": item[5],
                },
            )

        for restriction in structured_data["DietaryRestriction"]:
            DietaryRestriction.objects.update_or_create(
                id=restriction[0], defaults={"label": restriction[1]}
            )

        for menu in structured_data["Menu"]:
            ProcessingLog.objects.create(
                menu_id=menu[0],
                status="successful",
                error_message=None,
                timestamp=datetime.now(),
            )

        return True

    except Exception as e:
        print(f"Error saving data to the database: {e}")
        return False