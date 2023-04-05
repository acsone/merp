import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-merp",
    description="Meta package for merp Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-clear_groups_on_change',
        'odoo13-addon-outgoing_routing',
        'odoo13-addon-product_multiple_barcodes',
        'odoo13-addon-two_factor_otp_auth',
        'odoo13-addon-ventor_base',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 13.0',
    ]
)
