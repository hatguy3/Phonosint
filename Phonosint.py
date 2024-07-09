import phonenumbers as pnumb
from phonenumbers import parse, geocoder, carrier, timezone

def banner():
    print("""
\033[95m __        __        __   __         ___ \033[0m
\033[95m|__) |__| /  \\ |\\ | /  \\ /__` | |\\ |  |  \033[93mv1.0\033[0m
\033[95m|    |  | \\__/ | \\| \\__/ .__/ | | \\|  |  \033[0m
          
| \033[104m#https://github.com/hatguy3\033[0m |""")

def get_number_info(number):
    parsing = parse(number)
    return {
        "Info": parsing,
        "International format": pnumb.format_number(parsing, pnumb.PhoneNumberFormat.INTERNATIONAL),
        "National format": pnumb.format_number(parsing, pnumb.PhoneNumberFormat.NATIONAL),
        "Valid number": pnumb.is_valid_number(parsing),
        "Can be dialed internationally": pnumb.can_be_internationally_dialled(parsing),
        "Location": geocoder.description_for_number(parsing, 'en'),
        "Area code": pnumb.region_code_for_number(parsing),
        "Number type": pnumb.number_type(parsing),
        "Carrier operators": pnumb.is_carrier_specific(parsing),
        "ISP": carrier.name_for_number(parsing, 'en'),
        "Time zone": timezone.time_zones_for_number(parsing),
        "Geographical number": pnumb.is_number_geographical(parsing)
    }

def print_number_info(info):
    for key, value in info.items():
        print(f"\033[92m{key} \033[0m: {value}")

if __name__ == "__main__":
    banner()
    number = input("\n\033[92mEnter a number \033[0m(\033[mInclude Country Code\033[0m) \033[0m: ")
    info = get_number_info(number)
    print_number_info(info)