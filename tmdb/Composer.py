from dataclasses import dataclass


@dataclass
class Composer:
    """
    Data class that represent a composer
    """
    id: str
    name: str
    birthday: str = None
    gender: int = None
    homepage: str = None
    place_of_birth: str = None
    # First appearance of composer in movie credits
    date_first_appearance: str = None
