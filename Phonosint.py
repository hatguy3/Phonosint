import phonenumbers as pnumb
from phonenumbers import parse, geocoder, carrier, timezone, PhoneNumberFormat, number_type

def banner():
    print("""
\033[95m __        __        __   __         ___ \033[0m
\033[95m|__) |__| /  \\ |\\ | /  \\ /__` | |\\ |  |  \033[93mv1.0\033[0m
\033[95m|    |  | \\__/ | \\| \\__/ .__/ | | \\|  |  \033[0m
          
| \033[104m#https://github.com/hatguy3\033[0m |""")

def get_number_info(number):
    parsed_number = parse(number)
    line_type = {
        pnumb.PhoneNumberType.FIXED_LINE: "Fixed line",
        pnumb.PhoneNumberType.MOBILE: "Mobile",
        pnumb.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed line or mobile",
        pnumb.PhoneNumberType.TOLL_FREE: "Toll free",
        pnumb.PhoneNumberType.PREMIUM_RATE: "Premium rate",
        pnumb.PhoneNumberType.SHARED_COST: "Shared cost",
        pnumb.PhoneNumberType.VOIP: "VoIP",
        pnumb.PhoneNumberType.PERSONAL_NUMBER: "Personal number",
        pnumb.PhoneNumberType.PAGER: "Pager",
        pnumb.PhoneNumberType.UAN: "UAN",
        pnumb.PhoneNumberType.VOICEMAIL: "Voicemail",
        pnumb.PhoneNumberType.UNKNOWN: "Unknown"
    }.get(pnumb.number_type(parsed_number), "Unknown")

    return {
        "Valid number": pnumb.is_valid_number(parsed_number),
        "International number": pnumb.format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL),
        "National format": pnumb.format_number(parsed_number, PhoneNumberFormat.NATIONAL),
        "Can be dialed internationally": pnumb.can_be_internationally_dialled(parsed_number),
        "Line Type": line_type,
        "Number type": number_type(parsed_number),
        "Location": geocoder.description_for_number(parsed_number, "en"),
        "Area code": pnumb.region_code_for_number(parsed_number),
        "Geographical number": pnumb.is_number_geographical(parsed_number),
        "Time zone": timezone.time_zones_for_number(parsed_number),
        "Specific carriers": pnumb.is_carrier_specific(parsed_number),
        "ISP": carrier.name_for_number(parsed_number, "en"),
    }

def print_number_info(info):
    for key, value in info.items():
        print(f"\033[92m{key} \033[0m: {value}")

if __name__ == "__main__":
    banner()
    number = input("\n\033[92mEnter a number \033[0m(\033[31m+CountryCode\033[0m) \033[0m: ")
    info = get_number_info(number)
    print_number_info(info)