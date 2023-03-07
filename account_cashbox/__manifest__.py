# © 2022 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# © 2023 ADHOC SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Cashbox management",
    "summary": "Introduces concept of point of payment and accounting journal sessions",
    "version": "16.0.1.0.1",
    "category": "Accounting",
    "website": "www.adhoc.com.ar",
    "author": "juanpgarza, ADHOC SA",
    "license": "AGPL-3",
    "depends": [
        "account_payment_group",
        # la dependencia con payment group es solo para forzar utilizar el metodo parcheado
        # _compute_available_journal_ids. En v17 depreciariamos payment group y ya no seria necesario
        # ademas, al depender de payment group, por ahora no implementamos los wizard de payment register
        # ya que los mismos no se usan con payment group
        ],
    "demo": [
        'demo/point_of_payment_demo.xml',
    ],
    "data": [
        'security/pop_security.xml',
        'security/ir.model.access.csv',
        'views/pop_session_views.xml',
        'views/pop_config_views.xml',
        'views/res_users_views.xml',
        'views/account_payment.xml',
        # 'views/templates.xml',
        'wizards/pop_payment_import.xml',
        ],
    "installable": True,
    "application": True,
}