from odoo import fields, models


class EstatePropertyType(models.Model):
    # --Private Attributes--
    _name = "estate.property.type"
    _description = "estate property type model"
    _order = "name"

    # --Field Declaration--
    name = fields.Char("Name", required=True)
    sequence = fields.Integer("Sequence", default=10)

# Relational (for inline view)
    property_ids = fields.One2many(
        "estate.property", "property_type_id", string="Properties")
