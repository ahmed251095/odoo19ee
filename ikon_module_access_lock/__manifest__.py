{
    "name": "ikon Module List Lock",
    "version": "19.0.1.0.0",
    "category": "Technical",
    "license": "LGPL-3",
    "author": "ikon",
    "summary": "Only administrators may enumerate the installed module list",
    "description": """
ikon Module List Lock
=====================

By default every internal user can read ir.module.module over RPC and so
enumerate everything installed on the system. That ACL is granted by
``base_install_request`` -- an auto_install module that lets users request
an app installation -- not by ``base``.

Deactivating that ACL record would come back on ``-u base_install_request``,
and uninstalling an ``auto_install`` module just reinstalls it. So this
module adds two record rules of its own instead:

* base.group_user   -> domain [(0, '=', 1)]  : matches nothing
* base.group_system -> domain [(1, '=', 1)]  : matches everything

ir.rule ORs together the rules of every group a user belongs to, so an
administrator (a member of both groups) keeps full visibility while a
plain internal user gets an empty recordset.

A rule rather than an ACL revocation on purpose: users get [] instead of
an AccessError, so nothing crashes if some flow reads the model.

Server-side callers are unaffected: ir.module.module._get() returns a
sudo() recordset and _get_id() runs raw SQL, which is how
partner_autocomplete and account_edi_ubl_cii read it.

Scope note: this stops enumeration of the module list. It does not hide
which edition the server runs -- odoo.info.isEnterprise is computed in
the browser from the session, and /<module>/static/ paths are public.
    """,
    "depends": ["base"],
    "data": ["security/ir_rule.xml"],
    "installable": True,
    "auto_install": False,
    "application": False,
}
