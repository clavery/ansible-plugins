import subprocess

from ansible import utils, errors
import os
import codecs

class LookupModule(object):

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir

    def run(self, terms, inject=None, **kwargs):

        terms = utils.listify_lookup_plugin_terms(terms, self.basedir, inject)
        ret = []

        # this can happen if the variable contains a string, strictly not desired for lookup
        # plugins, but users may try it, so make it work.
        if not isinstance(terms, list):
            terms = [ terms ]

        for term in terms:
            basedir_path  = utils.path_dwim(self.basedir, term)
            relative_path = None
            playbook_path = None

            # Special handling of the file lookup, used primarily when the
            # lookup is done from a role. If the file isn't found in the
            # basedir of the current file, use dwim_relative to look in the
            # role/files/ directory, and finally the playbook directory
            # itself (which will be relative to the current working dir)
            if '_original_file' in inject:
                relative_path = utils.path_dwim_relative(inject['_original_file'], 'files', term, self.basedir, check=False)
            if 'playbook_dir' in inject:
                playbook_path = os.path.join(inject['playbook_dir'], term)

            for path in (basedir_path, relative_path, playbook_path):
                if path and os.path.exists(path):
                    gpg = subprocess.Popen(['gpg', "--batch", "-q", "-d", path],
                                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, _stderr = gpg.communicate()
                    if gpg.returncode != 0:
                        raise errors.AnsibleError("error calling gpg")
                    ret.append(stdout)
                    break
            else:
                raise errors.AnsibleError("could not locate file in lookup: %s" % term)

        return ret
