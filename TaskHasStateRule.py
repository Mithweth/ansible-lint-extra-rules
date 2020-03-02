from ansiblelint import AnsibleLintRule
from ansible.plugins.loader import module_loader, fragment_loader
from ansible.utils import plugin_docs

class TaskHasStateRule(AnsibleLintRule):
    id = '599'
    shortdesc = "Tasks must have a \"state\" argument"
    description = (
        'The ``state`` parameter is optional to a lot of modules. '
        'Whether ``state=present`` or ``state=absent``, it’s always '
        'best to leave that parameter in your playbooks to make it clear, '
        'especially as some modules support additional states.'
    )
    severity = 'LOW'
    tags = ['task', 'readability']
    version_added = 'historic'

    def matchtask(self, file, task):
        in_path = module_loader.find_plugin(task['action']["__ansible_module__"])
        oc, a, _, _ = plugin_docs.get_docstring(in_path, fragment_loader)
        return ('state' in oc['options'].keys() and 'state' not in task['action'])

