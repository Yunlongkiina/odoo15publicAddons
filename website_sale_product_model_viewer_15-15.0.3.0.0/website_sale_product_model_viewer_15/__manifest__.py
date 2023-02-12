# Copyright 2020 Lorenzo Battistini @ TAKOBI
# Copyright 2020 Andrea Piovesana @ Openindustry.it
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "eCommerce: Product model viewer",
    "summary": "3D model viewer for e-commerce products",
    "version": "15.0.3.0.0",
    "development_status": "Beta",
    "category": "Website",
    "website": "https://github.com/OCA/e-commerce",
    "author": "TAKOBI, Openindustry.it, Odoo Community Association (OCA)",
    "maintainers": ["eLBati"],
    "license": "AGPL-3",
    "depends": [
        "product_model_viewer_15",
        "website_sale",
    ],
    "assets": {
        "web.assets_backend": [
            "/website_sale_product_model_viewer_15/static/src/js/product_model_viewer.js",
        ],
    },
    "data": [
        "views/frontend_templates.xml",
    ],
    "application": False,
    "installable": True,
}
