# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import odoo  # noqa: F401

# ----------------------------------------------------------
# Monkey patch release to set the edition as 'enterprise'
# ----------------------------------------------------------
# PATCHED: the edition marker is deliberately not applied, so odoo.release keeps
# the Community values shipped by the package (19, 0, 0, 'final', 0, '').
# This single file is the only source of the '+e' suffix, so commenting it out
# makes every channel report Community at once: session_info,
# /web/webclient/version_info, XML-RPC version(), the Settings page, and
# odoo.info.isEnterprise in the web client (computed from
# server_version_info.slice(-1)[0] === "e").
#
# Known consequences:
#  - google_gmail / microsoft_outlook raise "Please configure your Gmail
#    credentials." instead of using Odoo's IAP relay (mixins check
#    release.version_info[-1] != 'e'). Set client_id/client_secret to avoid it.
#  - publisher_warranty reports release.version to odoo.com, so it now sends
#    19.0-<date> instead of 19.0+e-<date>.
#  - The Settings page shows "Upgrade to Enterprise" prompts on features that
#    are in fact installed.
#
# To revert: uncomment the three statements below.
#
# odoo.release.version_info = odoo.release.version_info[:5] + ('e',)
# if '+e' not in odoo.release.version:     # not already patched by packaging
#     odoo.release.version = '{0}+e{1}{2}'.format(*odoo.release.version.partition('-'))
#
# odoo.service.common.RPC_VERSION_1.update(
#     server_version=odoo.release.version,
#     server_version_info=odoo.release.version_info)
