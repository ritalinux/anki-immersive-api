from v1.utils import get_randon_id
from v1.utils.errors import CardRequiredFieldError, CardMissingFieldsError

import genanki

class BaseTemplate:
    def __init__(self, css=None, card_header=None):
        self.name = str()
        self.name_is_required = True
        
        self.card_header = card_header or str()
        self.card_header_is_required = False
        
        self.css_is_required = False
        self.css = (css or str()) + """
            .card {
                font-family: arial;
                font-size: 20px;
                text-align: center;
                color: black;
                background-color: white;
            }
        """

        self.output_front_fields = list()
        self.output_front_fields_is_required = True

        self.output_back_fields = list()
        self.output_back_is_required = True

        self.dt_name_is_required = True
        self.dt_qfmt_is_required = True
        self.dt_afmt_is_required = True
        self.default_template = {
            'name': 'Tpl: ' + self.name,
            'qfmt': None,
            'afmt': None,
        }

    def make_template(self):
        if self.name_is_required and not self.name:
            raise CardRequiredFieldError(
                f"Attribute 'name' not implemented in {self.__class__}"
            )

        if self.card_header_is_required and not self.card_header:
            raise CardRequiredFieldError(
                f"Attribute 'card_header' not implemented in {self.__class__}"
            )

        if self.css_is_required and not self.css:
            raise CardRequiredFieldError(
                f"Attribute 'css' not implemented in {self.__class__}"
            )

        if self.output_front_fields_is_required and not self.output_front_fields:
            raise CardRequiredFieldError(
                f"Attribute 'fields' not implemented in {self.__class__}"
            )

        if self.output_back_is_required and not self.output_back_fields:
            raise CardRequiredFieldError(
                f"Attribute 'fields' not implemented in {self.__class__}"
            )

        if self.dt_name_is_required and not self.default_template.get('name'):
            raise CardRequiredFieldError(
                f"Attribute 'default_template.name' not implemented in {self.__class__}"
            )

        if self.dt_qfmt_is_required and not self.default_template.get('qfmt'):
            raise CardRequiredFieldError(
                f"Attribute 'default_template.qfmt' not implemented in {self.__class__}"
            )

        if self.dt_afmt_is_required and not self.default_template.get('afmt'):
            raise CardRequiredFieldError(
                f"Attribute 'default_template.afmt' not implemented in {self.__class__}"
            )

        self.default_template['afmt'] = self.card_header + '\n' + self.default_template['afmt']

        for field in self.output_front_fields:
            if not field in self.default_template['qfmt']:
                raise CardMissingFieldsError(f"Missing field {field} in {self.__class__.__name__} front side generation.")

        for field in self.output_back_fields:
            if not field in self.default_template['afmt']:
                raise CardMissingFieldsError(f"Missing field {field} in {self.__class__.__name__} back side generation.")
        
        fields = []
        [fields.append(f) for f in self.output_front_fields if f not in fields]
        [fields.append(f) for f in self.output_back_fields if f not in fields]
        fields = [{'name': f} for f in fields]

        return genanki.Model(
            get_randon_id(),
            self.name,
            css=self.css,
            fields=fields,
            templates=[self.default_template]
        )