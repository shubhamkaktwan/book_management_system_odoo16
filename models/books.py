from odoo import fields,models,api

class BookDetails(models.Model):
    _name = "book.books"
    _description = "Books Record"
    _rec_name = "abc"

    name = fields.Char(string="Book Name",required=True)
    book_id = fields.Char(string="Book ID",readonly=True)
    copies = fields.Integer(string="No. of copies")
    author = fields.Char(string="Author")
    description = fields.Char(string="Description")
    available = fields.Boolean(string="Available" , default=True)
    partner_id = fields.Many2one('res.partner', string='Assign To : ')
    image = fields.Image(string="Image")
    status = fields.Selection([('Pending','Pending'),('Draft','Draft'),('Submitted','Submitted'),('Approved','Approved')], string="Status",default="Pending")
    his_ids = fields.One2many('book.history','his_id')
    abc=fields.Char(string="abc")


    @api.model
    def create(self, vals):
        vals['book_id'] = self.env['ir.sequence'].next_by_code('book.books')
        res = super(BookDetails, self).create(vals)
        return res

 