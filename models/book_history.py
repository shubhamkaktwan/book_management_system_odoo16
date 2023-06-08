from odoo import api,fields,models

# import logger
# import logging
# _logger = logging.getLogger(__name__)

class BookHistory(models.Model):
    _name = "book.history"
    _description = "Books History Record"


    starting_date = fields.Date(string="From")
    ending_date = fields.Date(string="To")
   
    his_id=fields.Many2one('book.books',string='Book Name')
    # author_id= fields.Char(related='history_id.author', string='author')
    no_of_days = fields.Char(string='Days' )
    efg=fields.Char(string="efg")
    