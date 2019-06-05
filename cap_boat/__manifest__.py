# coding: utf-8
# Part of CAPTIVEA. Odoo 12 EE.

{
    "name": "cap_boat",
    "version": "1.0",
    "author": "captivea",
    "summary": "Add boats, pontoons and cabins.",
    "depends": ["base",
                "cap_widget_color",
                "web_tree_dynamic_colored_field",
                "web_widget_x2many_2d_matrix"],
    "data": ["static/src/xml/assets.xml",
             "data/ir_model_access.xml",
             "data/cap_boat.xml",
             "data/cap_pontoon.xml",
             "data/cap_cabin.xml",
             "views/cap_cabin_mass_editing.xml",
             "views/cap_cabin_mass_reserving.xml",
             "views/cap_pontoon_mass_creating.xml",
             "data/ir_actions_act_window.xml",
             "views/cap_boat.xml",
             "views/cap_cabin.xml",
             "views/cap_pontoon.xml",
             "data/ir_ui_menu.xml"],
    "qweb": ["static/src/xml/cap_widget_cabins.xml"],
    "installable": True
}
