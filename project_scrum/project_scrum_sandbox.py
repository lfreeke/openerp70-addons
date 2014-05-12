# -*- coding: utf-8 -*-
from osv import fields, osv
from tools.translate import _



class projectScrumSandbox(osv.osv):
    _name = 'project.scrum.sandbox'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    
    _columns = {
        'role_id': fields.many2one('project.scrum.role', "As", required=True,),
        'name' : fields.char('I want', size=128, required=True),
        'for_then' : fields.char('For', size=128, required=True),
        'project_id': fields.many2one('project.project', "Project", required=True, domain=[('is_scrum', '=', True)]),
        'developer_id': fields.many2one('res.users', 'Developer'),
        'note':fields.text('Note', translate=False, ),
        'priority_id': fields.many2one('project.scrum.priority', "Priority",help="Priority of the request."),
    }
    
    def _get_default_role_id(self, cr, uid, ctx={}):
        role = ctx.get('default_role_id_name', False)
        if type(role) is int:
            return [role]
        elif isinstance(role, basestring):
            return self.pool.get('project.scrum.role').search(cr, uid, [('name', '=', role)])
        return role

    def _get_default_project_id(self, cr, uid, ctx={}):
        proj = ctx.get('default_project_id_name', False)
        if type(proj) is int:
            return [proj]
        elif isinstance(proj, basestring):
            return self.pool.get("project.project").search(cr, uid, [('name', '=', proj)])
        return proj

    _defaults = {
        'developer_id': lambda self, cr, uid, context: uid,
        'project_id': _get_default_project_id,
        'role_id': _get_default_role_id,
    }
