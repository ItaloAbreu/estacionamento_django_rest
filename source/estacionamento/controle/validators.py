from django.core.validators import RegexValidator

validate_plate = RegexValidator(
	r"^[a-zA-Z][a-zA-Z][a-zA-Z]\-[0-9][0-9][0-9][0-9]$",
	'Insira uma placa no formato AAA-9999'
)