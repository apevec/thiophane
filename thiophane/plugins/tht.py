# -*- coding: utf-8 -*-

"""THT plugin

Plugin for application of Puppet manifests from tripleo-heat-templates
on deployment hosts.
"""

from kanzo.core.puppet import update_manifest

#------------------------- deployment planning steps --------------------------#
THT_CONTROLLER_STEP_COUNT = 6

def controller_deployment_steps(config, info, messages):
    # create single-fragment manifest from controller manifest in tripleo-heat-templates
    update_manifest('controller_manifest', 'overcloud_controller.pp')

    manifests = []
    for tht_step in range(THT_CONTROLLER_STEP_COUNT):
        # each tht manifest is run several times over and over again with added
        # Puppet code, so we have to mimic this behaviour
        for host in config['hosts/controller_hosts']:
            marker = 'controller_{host}_{tht_step}'.format(**locals())
            prereqs = [
                'controller_{host}_{prev}'.format(host=host, prev=tht_step - 1)
            ]
            # TO-DO: generate manifest
            manifest_name = 'controller_manifest'
            update_manifest(name, path, context=None):
            manifests.append(
                host, manifest_name, marker, prereqs, hiera_name
            )
    return manifests


#-------------------------------- plugin data ---------------------------------#
# TODO: automagically generate configuration from Heat template YAML
CONFIGURATION = [
]
MODULES = []
RESOURCES = []
INITIALIZATION = []
PREPARATION = []
DEPLOYMENT = []
CLEANUP = []
