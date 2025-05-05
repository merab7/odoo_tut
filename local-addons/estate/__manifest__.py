{
    "name": "Real Estate",
    "category": "Sales",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/property_type.xml",
        "views/property_tags_view.xml",
        "views/estate_property_views.xml",
        "views/estate_menu.xml",

        #Date files
        #"data/property_type.xml"
        'data/estate.property.type.csv'
    ],
    "demo":[
        "demo/property_tag.xml"
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
