from django.contrib.auth import get_user_model # type: ignore
from django.http import JsonResponse # type: ignore
import requests # type: ignore

def create_subadmin(username, password):
    User = get_user_model()
    user = User.objects.create_user(username=username, password=password)
    user.is_staff = True
    user.is_superuser = False
    user.is_subadmin = True
    user.save()
    return user

def is_superadmin(user):
    return user.is_authenticated and user.is_superuser

def fetch_data_from_google_sheets():
    try:
        url="https://script.google.com/macros/s/AKfycbwXaP_FH_flHgAGMRjaKO7lkeWia6EbjoZ5-6OQxssQD7UAuwNAh59tbmB0F3FYD15f/exec"
        response = requests.get(url,timeout=9000)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        return JsonResponse({'error': f'HTTP error occurred: {err}', 'status_code': response.status_code})
    except ValueError:
        return JsonResponse({'error': 'Unable to decode response as JSON.', 'response_text': response.text})

def send_data_to_google_sheets(first_name,last_name,email,country_code,phone_number,password,sheetname):
    url="https://script.google.com/macros/s/AKfycbwXaP_FH_flHgAGMRjaKO7lkeWia6EbjoZ5-6OQxssQD7UAuwNAh59tbmB0F3FYD15f/exec"
    details = {
        "firstname": first_name,
        "lastname":last_name,
        "email": email, 
        "country_code":country_code,
        "phoneNumber": phone_number,
        "password":password,
        "sheetName":sheetname
    }
    response = requests.post(url, json=details, timeout=9000)
    res = response.text
    return JsonResponse({'message': res} , safe = False)

def send_data_to_google_sheet2(companyname,officialmale,country_code,mobilenumber,password,linkedinprofile,company_person_name,agreed_to_terms,sheetname):
    url="https://script.google.com/macros/s/AKfycbwXaP_FH_flHgAGMRjaKO7lkeWia6EbjoZ5-6OQxssQD7UAuwNAh59tbmB0F3FYD15f/exec"
    details = {
                "companyname":companyname,
                "officialmail":officialmale,
                "countrycode":country_code,
                "mobilenumber":mobilenumber,
                "password":password,
                "linkedInProfile":linkedinprofile,
                "companypersonname":company_person_name,
                "agreedtoterms":agreed_to_terms,
                "sheetName":sheetname
    }
    response = requests.post(url, json=details, timeout=9000)
    res = response.text
    return JsonResponse({'message': res} , safe = False)

def send_data_to_google_sheet3(university,officialmale,country_code,mobilenumber,password,linkedinprofile,college_person_name,agreed_to_terms,sheetname):
    url="https://script.google.com/macros/s/AKfycbwXaP_FH_flHgAGMRjaKO7lkeWia6EbjoZ5-6OQxssQD7UAuwNAh59tbmB0F3FYD15f/exec"
    details = {
                "university":university,
                "officialmail":officialmale,
                "countrycode":country_code,
                "mobilenumber":mobilenumber,
                "password":password,
                "linkedinProfile":linkedinprofile,
                "collegepersonname":college_person_name,
                "agreedtoterms":agreed_to_terms,
                "sheetName":sheetname
    }

    response = requests.post(url, json=details,timeout=9000)
    res = response.text
    return JsonResponse({'message': res} , safe = False)

def send_data_to_google_sheet4(consultant_name,official_email,country_code,mobile_number,password,linkedin_profile,consultant_person_name,agreed_to_terms,sheetName):
    url="https://script.google.com/macros/s/AKfycbwXaP_FH_flHgAGMRjaKO7lkeWia6EbjoZ5-6OQxssQD7UAuwNAh59tbmB0F3FYD15f/exec"
    details = {
                'name': consultant_name,
                'email': official_email,
                'countrycode':country_code,
                'mobileNumber': mobile_number,
                'password': password,
                'linkedinProfile': linkedin_profile,
                "consultantpersonname":consultant_person_name,
                "agreedtoterms":agreed_to_terms,
                'sheetName':sheetName
            }

    response = requests.post(url, json=details, timeout=9000)
    res = response.text
    return JsonResponse({'message': res} , safe = False)
