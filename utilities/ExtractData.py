import re


def extract_formatted_data(text):
    id_numbers = list(set(re.findall(r'\d{11}', text)))
    first_id_number = id_numbers[0] if id_numbers else None
    date_of_birth = find_date_of_birth(text)
    name = extract_name_using_dob(text, date_of_birth)

    return {
        'id_numbers_front': first_id_number,
        'name_front': name,
        'date_of_birth_front': date_of_birth
    }


def find_date_of_birth(text):
    dob_regex = r'\d{4}/\d{2}/\d{2}'
    match = re.search(dob_regex, text)
    return match.group(0) if match else None


def extract_name_using_dob(text, date_of_birth):
    if date_of_birth:
        pattern = fr'\u200f(.*?)\u200e\n+{date_of_birth}'
        match = re.search(pattern, text)
        return match.group(1).strip() if match else None
    return None
