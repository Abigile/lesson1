def get_vat(payment):
  vat = payment / 100 * 18
  return vat

result = get_vat(71.6)
print('Сумма ндс: {}'.format(result))