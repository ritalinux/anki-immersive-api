from v1.utils import get_randon_id
from v1.utils.errors import CardRequiredFieldError

import genanki

class BaseTemplate:
    def __init__(self, css=None, card_header=None):
        self.name = str()
        self.name_is_required = True
        
        self.card_header = card_header or str()
        self.card_header_is_required = False
        
        self.css_is_required = False
        self.css = css or """
            .card {
                font-family: arial;
                font-size: 20px;
                text-align: center;
                color: black;
                background-color: white;
            }
        """
        self.fields_is_required = True
        self.fields = list()

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

        if self.fields_is_required and not self.fields:
            raise CardRequiredFieldError(
                f"Attribute 'fields' not implemented in {self.__class__}"
            )

        if self.dt_qfmt_is_required and not self.default_template.get('qfmt'):
            raise CardRequiredFieldError(
                f"Attribute 'default_template.qfmt' not implemented in {self.__class__}"
            )

        if self.dt_afmt_is_required and not self.default_template.get('afmt'):
            raise CardRequiredFieldError(
                f"Attribute 'default_template.afmt' not implemented in {self.__class__}"
            )

        return genanki.Model(
            get_randon_id(),
            self.name,
            css=self.css,
            fields=self.fields,
            templates=[self.default_template]
        )