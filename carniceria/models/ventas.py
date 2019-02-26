from odoo import models, fields, api, _


class Ventas(models.Model):
    _name = 'carniceria.ventas'
    cod = fields.Char('COD', required=True)
    fecha_venta = fields.Date('Fecha Venta', required=True)
    descripcion = fields.Char('Descripcion', required=True)
    cliente = fields.Many2one('carniceria.clientes', 'Clientes', required=True)
    carnes = fields.Many2one('carniceria.carnes', 'Carnes', required=True)
    precio = fields.Integer()
    cantidad = fields.Integer('Cantidad', required=True)
    total = fields.Float(string='Total', compute='_total')

    def name_get(self):
        res = []
        for record in self:
            name = record.cod
            res.append((record.id, name))
        return res

    @api.one
    @api.depends('cantidad')
    def _total(self):
        self.precio = self.articulo.precio
        self.total = self.articulo.precio * self.cantidad
